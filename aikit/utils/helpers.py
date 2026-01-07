"""
辅助函数
"""


def truncate_text(text: str, max_length: int = 60, suffix: str = "...") -> str:
    """截断文本"""
    if len(text) <= max_length:
        return text
    return text[:max_length].replace('\n', ' ') + suffix


def safe_get(dictionary: dict, key: str, default=None):
    """安全获取字典值"""
    return dictionary.get(key, default)


def format_list(items: list, indent: int = 2) -> str:
    """格式化列表"""
    return '\n'.join(f"{' ' * indent}• {item}" for item in items)