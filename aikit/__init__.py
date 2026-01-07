"""
AI Kit - 人工智能工具集合

一个可扩展的AI工具库，包含常用的AI和机器学习工具。
"""

__version__ = "0.1.0"
__author__ = "Your Name"

from .core.config import Config
from .core.models import get_client, get_embeddings

__all__ = ["Config", "get_client", "get_embeddings"]