# Docker 快速开始

## 前置要求

- Docker Desktop 或 Docker Engine 已安装
- Docker Compose 已安装（Docker Desktop 自带）

## 方式 1：使用 Docker Compose（推荐）

### 1. 配置环境变量

创建 `.env` 文件：

```bash
# 通义千问配置
DASHSCOPE_API_KEY=your_dashscope_api_key_here
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DASHSCOPE_MODEL_NAME=qwen-plus

# 硅基流动配置（可选）
SILICONFLOW_API_KEY=your_siliconflow_api_key_here
SILICONFLOW_BASE_URL=https://api.siliconflow.cn/v1
SILICONFLOW_MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
SILICONFLOW_EMBEDDING_MODEL=BAAI/bge-m3
```

### 2. 构建并启动容器

```bash
# 构建镜像
docker-compose build

# 启动容器（后台运行）
docker-compose up -d

# 或者前台运行（查看日志）
docker-compose up
```

### 3. 运行命令

```bash
# 进入容器
docker-compose exec aikit bash

# 总结网页（默认使用千问）
aikit summarize https://www.active.com/affiliate

# 指定使用硅基流动
aikit summarize https://www.active.com/affiliate --provider siliconflow

# 保存到文件
aikit summarize https://www.active.com/affiliate -o summary.txt
```

### 4. 退出容器

```bash
# 停止容器
docker-compose stop

# 停止并删除容器
docker-compose down
```

## 方式 2：直接使用 Docker

### 1. 构建镜像

```bash
docker build -t aikit:latest .
```

### 2. 运行容器

```bash
docker run --rm \
  -e DASHSCOPE_API_KEY=your_api_key_here \
  -e SILICONFLOW_API_KEY=your_siliconflow_api_key_here \
  aikit:latest \
  aikit summarize https://www.active.com/affiliate
```

## 方式 3：交互式容器

```bash
docker run --rm -it \
  -e DASHSCOPE_API_KEY=your_api_key_here \
  -e SILICONFLOW_API_KEY=your_siliconflow_api_key_here \
  aikit:latest \
  bash

# 然后在容器内运行
aikit summarize https://www.active.com/affiliate
```

## 开发模式（挂载本地代码）

如果需要开发调试，修改 `docker-compose.yml`，取消 volumes 注释：

```yaml
volumes:
  - .:/app
```

然后：

```bash
# 重启容器
docker-compose down
docker-compose up -d

# 修改本地代码后，容器内会自动更新
docker-compose exec aikit aikit summarize https://example.com
```

## 常见问题

### 1. 容器无法访问网络

检查 Docker 的网络设置，确保允许容器访问外网。

### 2. 环境变量不生效

- 确保 `.env` 文件在 `docker-compose.yml` 同级目录
- 检查 `.env` 文件格式是否正确（不要有空格在等号周围）

### 3. 查看容器日志

```bash
docker-compose logs -f aikit
```

### 4. 重新构建镜像

```bash
# 停止并删除旧容器
docker-compose down

# 删除旧镜像
docker rmi aikit:latest

# 重新构建
docker-compose build --no-cache
```

## 性能优化

### 使用国内镜像源（如果在国内）

修改 `Dockerfile`，添加：

```dockerfile
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 清理资源

```bash
# 停止所有容器
docker-compose down

# 删除所有容器、网络、镜像
docker-compose down --rmi all -v
```
