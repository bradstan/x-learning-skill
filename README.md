# X-Learning Skill for OpenClaw

将 X（Twitter）收藏转化为结构化学习笔记，自动归档到 Obsidian vault。

## 完整工作流

```
X 收藏 → AI 分析生成笔记 → 归档到 vault → 分类 → 完成
   1           2              3          4
```

### Step 1: 抓取 X 收藏
定时抓取你在 X 上收藏的文章，提取原文内容。

### Step 2: AI 分析生成学习笔记
对每篇文章生成结构化笔记，包含：
- **原文总结** — 核心观点一句话概括
- **深度分析** — 对 AI/投资/内容的价值分析  
- **TODO 建议** — 可直接开发 / 需决策 的 action items

### Step 3: 归档到 vault
自动移动到目标 Obsidian vault。

### Step 4: 分类
根据内容关键词归类到对应文件夹。

## 核心功能

### 智能分类
| 关键词 | 目标文件夹 |
|--------|-----------|
| Agent、AI、自动化、MCP、OpenClaw | `agent进化/` |
| 期权、交易、K线、量化 | `投资交易类/` |
| 小红书、内容、营销 | `内容创作类/` |

### 标题提取与清洗
原始：
```
xxx111god-这几天在鼓捣_永续 Agent_，受到...-20260222.md
```
转为：
```
2月22日这几天在鼓捣永续 Agent.md
```

### 定时运行
Cron job `学习内容扫描`：10:00, 14:00, 18:00, 22:00

全自动：抓取 → 分析 → 归档 → 推送汇总

## 安装

```bash
git clone https://github.com/bradstan/x-learning-skill.git ~/.openclaw/workspace/skills/x-learning
```

## 配置

```python
# scripts/x-learning-process.py
UNREAD_DIR = Path.home() / "Documents" / "未读"
VAULT_DIR = Path.home() / "Documents" / "FLUX学习笔记"
```

Vault 结构：
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

# 预览模式
python3 scripts/x-learning-process.py --dry
```

对话触发：
```
User: 处理今天的 X 收藏
Agent: 抓取 2 篇 → 生成学习笔记 → 归档到 agent进化/
```

## 依赖

- Python 3.8+
- 无外部包依赖

## License

MIT
