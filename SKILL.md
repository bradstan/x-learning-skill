# X-Learning Skill

将 X（Twitter）收藏转化为结构化学习笔记，自动归档到 Obsidian vault。

## 解决什么问题

每天在 X 上刷到大量有价值的深度内容，但：
- 收藏后基本不会再看
- 笔记散落在各处，无法系统化检索
- 想回顾时找不到重点

X-Learning 自动完成：分析 → 分类 → 归档 → 检索友好

## 功能

### 智能分类
根据内容关键词自动归类：
| 关键词 | 目标文件夹 |
|--------|-----------|
| Agent、AI、自动化、MCP、OpenClaw、龙虾 | `agent进化/` |
| 期权、交易、K线、量化、风控 | `投资交易类/` |
| 小红书、内容、营销、爆款 | `内容创作类/` |

### 标题提取与清洗
原始文件名：
```
xxx111god-这几天在鼓捣_永续 Agent_，受到...-20260222.md
```
自动转为：
```
2月22日这几天在鼓捣永续 Agent.md
```

### 自动归档
- 检测今日新文章
- 提取标题
- 分类
- 移动到 vault

### 定时运行
Cron job `学习内容扫描`：10:00, 14:00, 18:00, 22:00

## 配置

### 1. 路径设置
编辑 `scripts/x-learning-process.py`：
```python
UNREAD_DIR = Path.home() / "Documents" / "未读"
VAULT_DIR = Path.home() / "Documents" / "FLUX学习笔记"
```

### 2. Vault 结构
```
FLUX学习笔记/
├── agent进化/
├── 内容创作类/
└── 投资交易类/
```

## 使用

```bash
# 手动处理
python3 scripts/x-learning-process.py

# 预览模式（不移动）
python3 scripts/x-learning-process.py --dry
```

对话触发：
```
User: 处理今天的 X 收藏
Agent: 扫描到 2 篇新文章，已归档
```

## 分类规则自定义

```python
CATEGORIES = {
    "agent进化": ["agent", "ai", "自动化", "mcp"],
    "投资交易类": ["期权", "交易", "k线"],
    "内容创作类": ["小红书", "内容", "营销"]
}
```

## 依赖

- Python 3.8+
- 无外部包

## 工作流

```
X 收藏 → x-bookmarks-watch.py 分析 → 未读/ 
       → x-learning-process.py 分类+归档 
       → FLUX学习笔记/{类别}/
```
