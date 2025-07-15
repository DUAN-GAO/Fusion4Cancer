# 使用官方Python 3.6基础镜像
FROM python:3.6-slim

# 设置工作目录
WORKDIR /app

# 解决Debian源DNS解析问题
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf

# 安装系统依赖（仅当scipy或numpy编译需要）
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 安装PyTorch（CPU版本）及其依赖
RUN pip install \
    torch==1.10.0+cpu \
    torchvision==0.11.1+cpu \
    torchaudio==0.10.0+cpu \
    --extra-index-url https://download.pytorch.org/whl/cpu

# 安装其他Python依赖
RUN pip install \
    numpy==1.19.2 \
    scipy==1.5.4 \
    scikit-learn==0.24.2

# 复制你的Python脚本（可选）
# COPY . /app

# 默认执行（可根据需求修改）
CMD ["python"]
