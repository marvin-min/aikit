"""
配置管理模块
"""
import os
import dotenv
from pathlib import Path
from typing import Optional

dotenv.load_dotenv()


class Config:
    """全局配置管理"""

    # API 配置
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")
    DASHSCOPE_MODEL_NAME = os.getenv("DASHSCOPE_MODEL_NAME", "qwen-plus")

    # 硅基流动配置
    SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")
    SILICONFLOW_BASE_URL = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1")
    SILICONFLOW_MODEL_NAME = os.getenv("SILICONFLOW_MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
    SILICONFLOW_EMBEDDING_MODEL = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "BAAI/bge-m3")
    
    # RAG 配置
    DEFAULT_CHUNK_SIZE = 1000
    DEFAULT_CHUNK_OVERLAP = 100
    DEFAULT_RETRIEVAL_K = 5
    
    # 日志配置
    LANGCHAIN_VERBOSE = os.getenv("LANGCHAIN_VERBOSE", "false").lower() == "true"
    
    # 用户代理
    USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36")
    
    @classmethod
    def validate(cls) -> bool:
        """验证必要配置是否存在"""
        required = ["DASHSCOPE_API_KEY", "DASHSCOPE_BASE_URL", "DASHSCOPE_MODEL_NAME"]
        missing = [key for key in required if not getattr(cls, key)]

        if missing:
            print(f"❌ 缺少环境变量: {', '.join(missing)}")
            print("请在 .env 文件中设置这些变量")
            return False

        return True

    @classmethod
    def use_siliconflow(cls, provider: str = None) -> bool:
        """检查是否使用硅基流动

        Args:
            provider: 指定使用的服务商 ('dashscope' 或 'siliconflow')
                      如果为 None，则优先使用千问，fallback到硅基流动
        """
        if provider == "siliconflow":
            return bool(cls.SILICONFLOW_API_KEY)
        elif provider == "dashscope":
            return False
        else:
            # 优先使用千问，如果千问没有配置，fallback 到硅基流动
            return not bool(cls.DASHSCOPE_API_KEY) and bool(cls.SILICONFLOW_API_KEY)