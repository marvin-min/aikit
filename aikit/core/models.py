"""
LLM 客户端管理
"""
import os
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings

from .config import Config


def get_client(api_key=None, base_url=None, model_name=None, provider=None):
    """获取 LLM 客户端"""
    if Config.use_siliconflow(provider):
        return ChatOpenAI(
            api_key=api_key or Config.SILICONFLOW_API_KEY,
            base_url=base_url or Config.SILICONFLOW_BASE_URL,
            model=model_name or Config.SILICONFLOW_MODEL_NAME
        )

    return ChatOpenAI(
        api_key=api_key or Config.DASHSCOPE_API_KEY,
        base_url=base_url or Config.DASHSCOPE_BASE_URL,
        model=model_name or Config.DASHSCOPE_MODEL_NAME
    )


def get_embeddings(provider=None):
    """获取向量化模型"""
    if Config.use_siliconflow(provider):
        return OpenAIEmbeddings(
            model=Config.SILICONFLOW_EMBEDDING_MODEL,
            api_key=Config.SILICONFLOW_API_KEY,
            base_url=Config.SILICONFLOW_BASE_URL
        )

    return DashScopeEmbeddings(
        model="text-embedding-v3",
        dashscope_api_key=Config.DASHSCOPE_API_KEY
    )