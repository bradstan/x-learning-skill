#!/usr/bin/env python3
"""
X-Learning Processor
将 ~/Documents/未读/ 中的 X 收藏分析文章移动到 FLUX学习笔记 vault 对应 folder

流程：
1. 扫描未读目录中的 X 收藏分析文件
2. 提取原文标题
3. 重命名为规范格式：X月X日+原文标题
4. 分类并移动到对应 folder
"""

import os
import shutil
import re
from datetime import datetime
from pathlib import Path

UNREAD_DIR = Path.home() / "Documents" / "未读"
VAULT_DIR = Path.home() / "Documents" / "FLUX学习笔记"

# 分类规则
CATEGORIES = {
    "agent进化": [
        "agent", "ai", "自动化", "永续", "部署", "openclaw", "mcp", 
        "lobster", "龙虾", "vps", "服务器", "workflow", "工作流",
        "prompt", "提示词", "llm", "gpt", "claude", "模型"
    ],
    "投资交易类": [
        "期权", "交易", "投资", "股票", "k线", "量化", "风控", 
        "持仓", "止盈", "止损", "特斯拉", "tsla", "标的",
        "波动率", "iv", "delta", "gamma", "theta", "vega"
    ],
    "内容创作类": [
        "内容", "小红书", "文案", "视频", "营销", "创作", 
        "爆款", "流量", "粉丝", "转化", "标题", "封面",
        "算法", "推荐", "seo"
    ]
}

def extract_title_from_content(content: str) -> str | None:
    """从分析文件中提取原文标题"""
    # 方式1：从"输入文件"行提取
    # 格式: 输入文件: xxx111god-这几天在鼓捣_永续 Agent_，受到...-20260222.md
    input_match = re.search(r'输入文件:\s*[\w-]+-(.+?)-\d{8}', content)
    if input_match:
        title = input_match.group(1)
        # 清理标题
        title = title.replace('_', ' ').strip()
        # 去掉末尾的时间戳残留
        title = re.sub(r'-\d{6}$', '', title)
        return title
    
    # 方式2：从第一个 H1 标题提取
    h1_match = re.search(r'^#\s+(.+?)的X收藏分析', content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()
    
    return None

def clean_title(title: str, max_len: int = 50) -> str:
    """清理标题，限制长度"""
    # 移除特殊字符
    title = re.sub(r'[\\/:*?"<>|]', '', title)
    # 替换下划线为空格
    title = title.replace('_', ' ')
    # 压缩空格
    title = re.sub(r'\s+', ' ', title).strip()
    # 限制长度
    if len(title) > max_len:
        title = title[:max_len].rsplit(' ', 1)[0]
    return title

def classify_content(content: str) -> str:
    """根据内容关键词分类"""
    content_lower = content.lower()
    scores = {cat: 0 for cat in CATEGORIES}
    
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in content_lower:
                scores[category] += 1
    
    # 返回得分最高的类别
    max_score = max(scores.values())
    if max_score == 0:
        return "agent进化"  # 默认
    
    for cat, score in scores.items():
        if score == max_score:
            return cat
    
    return "agent进化"

def get_today_prefix() -> str:
    """获取今天的中文日期前缀，如 '2月23日'"""
    now = datetime.now()
    return f"{now.month}月{now.day}日"

def process_new_articles(dry_run: bool = False) -> list:
    """处理今天的新文章"""
    today_prefix = get_today_prefix()
    results = []
    
    if not UNREAD_DIR.exists():
        print(f"❌ 未读目录不存在: {UNREAD_DIR}")
        return results
    
    # 找到今天的文件（支持两种命名格式）
    for file in UNREAD_DIR.glob(f"{today_prefix}*.md"):
        if "X收藏分析" in file.name or "翻译版" in file.name:
            # 读取文件内容进行分类和提取标题
            try:
                content = file.read_text(encoding='utf-8')
                category = classify_content(content)
                title = extract_title_from_content(content)
            except Exception as e:
                category = "agent进化"
                title = None
            
            # 生成新文件名
            if title:
                new_name = f"{today_prefix}{clean_title(title)}.md"
            else:
                # 保持原名
                new_name = file.name
            
            target_dir = VAULT_DIR / category
            target_path = target_dir / new_name
            
            results.append({
                "file": file.name,
                "new_name": new_name,
                "category": category,
                "source": str(file),
                "target": str(target_path),
                "title": title
            })
            
            if not dry_run:
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file), str(target_path))
                print(f"✅ {new_name} → {category}/")
            else:
                print(f"[DRY] {new_name} → {category}/")
    
    return results

if __name__ == "__main__":
    import sys
    dry_run = "--dry" in sys.argv
    
    print(f"📂 扫描: {UNREAD_DIR}")
    print(f"📤 目标: {VAULT_DIR}")
    print(f"📅 日期: {get_today_prefix()}")
    print("-" * 40)
    
    results = process_new_articles(dry_run)
    
    if not results:
        print("没有找到今天的新文章")
    else:
        print(f"\n处理完成：{len(results)} 篇文章")
        for r in results:
            if r['title']:
                print(f"  📄 标题: {r['title']}")
