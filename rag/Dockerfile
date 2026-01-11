FROM python:3.11-slim

# 1️⃣ 基础环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 2️⃣ 系统依赖（Chroma / 一些 embedding 需要）
RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  && rm -rf /var/lib/apt/lists/*

# 3️⃣ 安装 Python 依赖（先 requirements，提高缓存命中率）
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 4️⃣ 拷贝项目代码
COPY . .

# 5️⃣ 默认执行
CMD ["python", "new_demo.py"]
