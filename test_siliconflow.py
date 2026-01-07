"""
测试硅基流动 API
"""
import os
from dotenv import load_dotenv

load_dotenv()

from aikit.tools.web_summarizer.summarizer import WebSummarizer
from aikit.core.models import get_client, get_embeddings
from aikit.core.config import Config

print("=" * 50)
print("硅基流动 API 测试")
print("=" * 50)

# 检查配置
print("\n1. 检查配置...")
if Config.use_siliconflow():
    print(f"✅ 使用硅基流动")
    print(f"   Base URL: {Config.SILICONFLOW_BASE_URL}")
    print(f"   LLM 模型: {Config.SILICONFLOW_MODEL_NAME}")
    print(f"   Embedding 模型: {Config.SILICONFLOW_EMBEDDING_MODEL}")
else:
    print(f"❌ 未配置硅基流动 API Key")
    print(f"   请在 .env 文件中设置 SILICONFLOW_API_KEY")
    exit(1)

# 测试 LLM
print("\n2. 测试 LLM...")
try:
    llm = get_client()
    print(f"   客户端: {llm}")
    response = llm.invoke("你好，用一句话介绍硅基流动")
    print(f"✅ LLM 响应: {response.content[:100]}...")
except Exception as e:
    print(f"❌ LLM 测试失败: {e}")
    exit(1)

# 测试 Embedding
print("\n3. 测试 Embedding...")
try:
    embeddings = get_embeddings()
    print(f"   客户端: {embeddings}")
    result = embeddings.embed_query("测试文本")
    print(f"✅ Embedding 维度: {len(result)}")
    print(f"   向量示例: {result[:5]}...")
except Exception as e:
    print(f"❌ Embedding 测试失败: {e}")
    exit(1)

# 测试网页总结
print("\n4. 测试网页总结...")
try:
    summarizer = WebSummarizer(chunk_size=1000, retrieval_k=3)
    summary = summarizer.summarize(
        "https://example.com",
        "这个网站的主要内容是什么？"
    )
    print(f"✅ 总结成功:")
    print(f"   {summary}")
except Exception as e:
    print(f"❌ 网页总结失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("测试完成")
print("=" * 50)
