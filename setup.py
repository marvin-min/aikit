"""
AI Kit 安装配置
"""
from setuptools import setup, find_packages

setup(
    name="aikit",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="人工智能工具集合",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aikit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv>=1.0.0",
        "click>=8.0.0",
        "pydantic>=2.5.0",
        "h11>=0.14.0",
        "httpcore>=0.17.0",
        "httpx>=0.25.0",
        "openai>=1.30.0",
        "langchain-openai>=0.2.0",
        "langchain-community>=0.2.0",
        "langchain-core>=0.2.0",
        "langchain-text-splitters>=0.2.0",
        "chromadb>=0.4.0",
        "beautifulsoup4>=4.12.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "aikit=aikit.cli.main:cli",
        ],
    },
)