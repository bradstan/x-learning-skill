# X-Learning Skill for OpenClaw

将 X（Twitter）收藏转化为结构化学习笔记，自动归档到 Obsidian vault。

## 解决什么问题

每天在 X 上刷到大量有价值的深度内容，但：
- 收藏后基本不会再看
- 笔记散落在各处，无法系统化检索
- 想回顾时找不到重点

X-Learning 自动完成：分析 → 分类 → 归档 → 检索友好

## 核心功能

### 1. 智能分类
根据内容关键词自动归类到对应文件夹：
- **agent进化** — AI Agent、自动化、工作流、OpenClaw、MCP
- **投资交易类** — 期权、股票、量化、K线、风控
- **内容创作类** — 小红书、抖音、内容营销、爆款分析

### 2. 标题提取与清洗
原始文件名往往很长很乱：
```
xxx111god-这几天在鼓捣_永续 Agent_，受到 @MatthewBerman...-20260222.md
```
自动提取并格式化为：
```
2月22日这几天在鼓捣永续 Agent.md
```

### 3. 自动归档
无需手动移动文件，脚本自动：
- 检测今日新文章
- 提取标题
- 分类
- 移动到 vault 对应文件夹

### 4. 集成工作流
配合 cron job 实现全自动：
- 每 6 小时扫描一次（10:00, 14:00, 18:00, 22:00）
- 分析 X 收藏 → 生成分析笔记 → 自动归档
- 全程无需人工干预

## 使用场景

```
场景1：手动处理
$ python3 scripts/x-learning-process.py
✅ 2月23日极简方案让龙虾帮你盯K线图.md → agent进化/
✅ 2月23日这几天在鼓捣永续 Agent.md → agent进化/

场景2：对话触发
User: 处理今天的 X 收藏
Agent: 扫描到 2 篇文章，已归档到 FLUX学习笔记
```

## 安装

```bash
# 克隆技能
git clone https://github.com/bradstan/x-learning-skill.git ~/.openclaw/workspace/skills/x-learning

# 或使用 ClawHub（即将支持）
openclaw skill install x-learning
```

## 配置

修改 `scripts/x-learning-process.py` 中的路径：

```python
UNREAD_DIR = Path.home() / "Documents" / "未读"      # X 收藏分析文件目录
VAULT_DIR = Path.home() / "Documents" / "FLUX学习笔记" # 目标 Obsidian vault
```

创建 vault 文件夹结构：
```
FLUX学习笔记/
├── agent进化/      # AI、自动化、Agent 相关
├── 内容创作类/     # 内容营销、创作
└── 投资交易类/     # 交易、投资
```

## 自定义分类规则

编辑 `CATEGORIES` 字典：

```python
CATEGORIES = {
    "agent进化": ["agent", "ai", "自动化", "mcp", "openclaw"],
    "投资交易类": ["期权", "交易", "k线", "量化"],
    "内容创作类": ["小红书", "内容", "营销", "爆款"]
}
```

## 依赖

- Python 3.8+
- 无外部包依赖

## 工作流示意

```
X 收藏
   ↓
x-bookmarks-watch.py（定时抓取+AI分析）
   ↓
~/Documents/未读/（生成分析笔记）
   ↓
x-learning-process.py（提取标题+分类+归档）
   ↓
~/Documents/FLUX学习笔记/{类别}/（结构化存储）
   ↓
Obsidian 中搜索回顾
```

## License

MIT

---

**配合使用效果更佳：**
- [x-bookmarks-watch](https://github.com/bradstan/x-bookmarks-watch) — X 收藏监控 + AI 分析
- [OpenClaw](https://github.com/openclaw/openclaw) — AI Agent 框架
