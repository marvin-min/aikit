"""
日志管理工具
"""
import logging
import sys
from typing import Optional


def setup_logger(name: str = "aikit", level: str = "INFO") -> logging.Logger:
    """设置日志记录器"""
    
    logger = logging.getLogger(name)
    
    if logger.handlers:
        return logger
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, level.upper()))
    
    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """获取日志记录器"""
    return logging.getLogger(name or "aikit")