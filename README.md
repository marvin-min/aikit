# AI Kit 🛠️

一个可扩展的人工智能工具集合，包含常用的AI和机器学习工具。

## 🚀 快速开始

### 安装

```bash
# 克隆项目
git clone <your-repo-url>
cd aikit

# 安装依赖
pip install -r requirements.txt

# 开发模式安装
pip install -e .
```

### 配置

1. 复制环境变量配置文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的 API 密钥：
```bash
DASHSCOPE_API_KEY=your_dashscope_api_key_here
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DASHSCOPE_MODEL_NAME=qwen-plus
```

## 📦 工具集合

### 网页内容总结

使用 RAG 技术总结网页内容：

```bash
# 基本用法
aikit summarize https://example.com

# 自定义查询
aikit summarize https://example.com --query "这个网站的主要产品是什么？"

# 保存到文件
aikit summarize https://example.com -o summary.txt

# 调整参数
aikit summarize https://example.com --chunk-size 1500 --retrieval-k 8
```

### 命令行选项

- `--query, -q`: 自定义查询问题
- `--chunk-size`: 文档切分大小 (默认: 1000)
- `--chunk-overlap`: 文档切分重叠 (默认: 100)
- `--retrieval-k`: 检索文档数量 (默认: 5)
- `--output, -o`: 输出到文件
- `--verbose, -v`: 启用详细日志

## 🏗️ 项目结构

```
aikit/
├── aikit/                     # 主要包
│   ├── cli/                   # CLI 入口
│   ├── core/                  # 核心共享组件
│   ├── tools/                 # 具体工具实现
│   └── utils/                 # 通用工具
├── tests/                     # 测试
├── examples/                  # 使用示例
├── docs/                      # 文档
└── requirements.txt           # 依赖
```

## 🔧 开发

### 添加新工具

1. 在 `aikit/tools/` 下创建新工具目录
2. 实现工具逻辑
3. 在 `aikit/cli/commands/` 下添加命令文件
4. 在 `aikit/cli/main.py` 中注册命令

### 测试

```bash
# 运行测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=aikit
```

## 📝 示例

### Python API 使用

```python
from aikit.tools.web_summarizer import WebSummarizer

# 创建总结器
summarizer = WebSummarizer(chunk_size=1500)

# 总结网页
summary = summarizer.summarize(
    "https://example.com",
    "总结这篇文章的核心观点"
)
print(summary)
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License