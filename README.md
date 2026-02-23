# X-Learning Skill for OpenClaw

Transform X (Twitter) bookmarks into structured learning notes in your Obsidian vault.

## Features

- 📥 **Auto-scan**: Detects new analysis files in your inbox
- 🏷️ **Smart classification**: Categorizes content by keywords
- ✏️ **Title extraction**: Cleans up messy filenames
- 📁 **Auto-archive**: Moves files to appropriate vault folders

## Quick Start

```bash
# Clone or download this skill
git clone https://github.com/bradstan/x-learning-skill.git

# Run the processor
python3 scripts/x-learning-process.py

# Preview mode
python3 scripts/x-learning-process.py --dry
```

## Configuration

Edit the paths in `scripts/x-learning-process.py`:

```python
UNREAD_DIR = Path.home() / "Documents" / "未读"  # Your inbox folder
VAULT_DIR = Path.home() / "Documents" / "FLUX学习笔记"  # Your vault
```

Create your vault structure:

```
YourVault/
├── agent进化/      # AI, automation
├── 内容创作类/     # Content creation
└── 投资交易类/     # Trading
```

## Classification Rules

| Category | Keywords |
|----------|----------|
| agent进化 | Agent, AI, automation, OpenClaw, MCP |
| 投资交易类 | 期权, 交易, 投资, K线, 量化 |
| 内容创作类 | 内容, 小红书, 文案, 视频, 营销 |

## Integration

Works great with:
- [x-bookmarks-watch](https://github.com/your-username/x-bookmarks-watch) - Monitors X bookmarks
- OpenClaw cron jobs - Automate processing

## License

MIT
