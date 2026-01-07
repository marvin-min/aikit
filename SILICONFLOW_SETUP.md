# 硅基流动 API 集成配置指南

## 1. 获取 API Key

1. 访问硅基流动官网：https://cloud.siliconflow.cn/
2. 注册或登录账号
3. 进入 API 密钥管理页面：https://cloud.siliconflow.cn/account/ak
4. 点击"新建 API 密钥"
5. 复制生成的 API Key

## 2. 配置 .env 文件

编辑 `.env` 文件，添加以下配置：

```bash
# 硅基流动 API 配置
SILICONFLOW_API_KEY=sk-your-api-key-here
SILICONFLOW_BASE_URL=https://api.siliconflow.cn/v1
SILICONFLOW_MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
SILICONFLOW_EMBEDDING_MODEL=BAAI/bge-m3
```

## 3. 测试 API

运行测试脚本：

```bash
python test_siliconflow.py
```

## 4. 使用 aikit 总结网页

配置完成后，aikit 会自动使用硅基流动的 API：

```bash
# 总结网页
aikit summarize https://docs.siliconflow.cn/cn/userguide/quickstart

# 保存到文件
aikit summarize https://example.com -o summary.txt

# 自定义查询
aikit summarize https://example.com --query "这个网站的主要功能是什么？"
```

## 支持的模型

### 语言模型（可选）

- `Qwen/Qwen2.5-72B-Instruct`（默认）
- `deepseek-ai/DeepSeek-V3`
- `deepseek-ai/DeepSeek-R1`
- `Qwen/Qwen3-32B`
- 更多模型：https://cloud.siliconflow.cn/models

### Embedding 模型（可选）

- `BAAI/bge-m3`（默认，支持 8192 tokens）
- `BAAI/bge-large-zh-v1.5`
- `Qwen/Qwen3-Embedding-8B`

## 切换回通义千问

如果需要切换回通义千问，只需注释掉或删除 `.env` 文件中的 `SILICONFLOW_API_KEY` 即可。

## 注意事项

- 硅基流动提供部分免费模型，也有付费模型
- 按实际使用 Token 计费
- 查看价格：https://siliconflow.cn/pricing
- 查看速率限制：https://docs.siliconflow.cn/cn/userguide/rate-limits/rate-limit-and-upgradation
