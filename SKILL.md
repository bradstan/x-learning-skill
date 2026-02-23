# X-Learning Skill

Transform X (Twitter) bookmarks into structured learning notes in your Obsidian vault.

## What it does

1. **Scans** your inbox folder for new X bookmark analysis files
2. **Extracts** original article titles
3. **Renames** files with clean format: `MM月DD日 + Title`
4. **Classifies** content into categories (AI/Trading/Content)
5. **Moves** files to appropriate vault folders

## Setup

### 1. Configure paths

Edit the script to match your setup:

```python
UNREAD_DIR = Path.home() / "Documents" / "未读"  # Your inbox folder
VAULT_DIR = Path.home() / "Documents" / "FLUX学习笔记"  # Your Obsidian vault
```

### 2. Create vault structure

```
YourVault/
├── agent进化/      # AI, automation, agents
├── 内容创作类/     # Content creation, marketing
└── 投资交易类/     # Trading, investing
```

### 3. (Optional) Add to cron

```bash
# Run every 6 hours
0 10,14,18,22 * * * python3 /path/to/x-learning-process.py
```

## Usage

### Manual processing

```bash
python3 scripts/x-learning-process.py

# Preview mode (don't actually move files)
python3 scripts/x-learning-process.py --dry
```

### Via conversation

```
User: 处理今天的 X 收藏
Agent: [Scans, classifies, and archives new articles]
```

## Classification Rules

| Keywords | Target Folder |
|----------|---------------|
| Agent, AI, automation, deployment, MCP | `agent进化/` |
| Options, trading, investing, K-line | `投资交易类/` |
| Content, marketing, XHS, video | `内容创作类/` |
| Uncertain | `agent进化/` (default) |

## File Naming

**Before**: `xxx111god-这几天在鼓捣_永续 Agent_-20260222.md`
**After**: `2月22日这几天在鼓捣永续 Agent.md`

## Dependencies

- Python 3.8+
- No external packages required

## Workflow Integration

This skill works best with:
1. **X bookmark monitoring** (`x-bookmarks-watch.py`)
2. **AI analysis** (generates analysis files)
3. **This processor** (archives to vault)

---

## 自定义配置

修改 `scripts/x-learning-process.py` 中的 `CATEGORIES` 字典来调整分类规则：

```python
CATEGORIES = {
    "agent进化": ["agent", "ai", "自动化", ...],
    "投资交易类": ["期权", "交易", ...],
    "内容创作类": ["内容", "小红书", ...]
}
```
