"""
简化测试硅基流动 API
"""
import os
from dotenv import load_dotenv

load_dotenv()

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
    exit(1)

# 测试 LLM
print("\n2. 测试 LLM...")
try:
    llm = get_client()
    response = llm.invoke("你好，用3句话介绍硅基流动")
    print(f"✅ LLM 响应:")
    print(f"   {response.content}")
except Exception as e:
    print(f"❌ LLM 测试失败: {e}")
    import traceback
    traceback.print_exc()

# 测试 Embedding
print("\n3. 测试 Embedding...")
try:
    embeddings = get_embeddings()
    result = embeddings.embed_query("硅基流动提供大模型API服务")
    print(f"✅ Embedding 维度: {len(result)}")
except Exception as e:
    print(f"❌ Embedding 测试失败: {e}")

# 模拟 RAG 总结
print("\n4. 测试模拟 RAG 总结...")
try:
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain.docstore.document import Document

    llm = get_client()

    # 模拟检索到的文档
    docs = [
        Document(page_content="硅基流动是一家AI模型API服务平台，提供多种开源大模型。"),
        Document(page_content="平台支持Qwen、DeepSeek、GLM等主流模型，按Token计费。"),
        Document(page_content="硅基流动提供免费额度，价格透明，API完全兼容OpenAI格式。"),
    ]

    # 创建总结链
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的文档总结助手。请根据以下上下文内容进行总结。\n\n上下文：\n{context}"),
        ("user", "任务：{input}\n\n注意：请分条目列出核心要点,保持客观准确。"),
    ])

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    result = combine_docs_chain.invoke({
        "context": docs,
        "input": "硅基流动的主要特点是什么？"
    })

    print(f"✅ RAG 总结成功:")
    print(f"   {result}")
except Exception as e:
    print(f"❌ RAG 总结失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("✅ 测试完成")
print("=" * 50)
