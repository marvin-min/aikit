"""
工具基类
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseTool(ABC):
    """所有工具的基类"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """执行工具"""
        pass
    
    def validate_inputs(self, *args, **kwargs) -> bool:
        """验证输入参数"""
        return True