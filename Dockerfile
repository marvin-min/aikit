# 使用 Python 3.10 官方镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 复制项目代码
COPY . .

# 安装项目（开发模式）
RUN pip install -e .

# 设置环境变量（示例，实际使用时通过 .env 文件配置）
ENV DASHSCOPE_API_KEY=your_dashscope_api_key_here \
    DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1 \
    DASHSCOPE_MODEL_NAME=qwen-plus \
    SILICONFLOW_BASE_URL=https://api.siliconflow.cn/v1 \
    SILICONFLOW_MODEL_NAME=Qwen/Qwen2.5-72B-Instruct \
    SILICONFLOW_EMBEDDING_MODEL=BAAI/bge-m3

# 默认命令
CMD ["aikit", "--help"]
