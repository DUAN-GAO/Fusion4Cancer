# 基础镜像：Ubuntu 18.04
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

# 更换系统源为阿里云
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 && \
    apt-get clean && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends \
        python3 python3-pip python3-dev \
        build-essential ca-certificates curl && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 链接Python3为默认
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# 升级pip并使用国内源
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 安装基础工具
RUN pip install --no-cache-dir setuptools==58.0.4 wheel==0.37.1 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 安装PyTorch 1.6.0+cpu（阿里云源）
RUN pip install --no-cache-dir --default-timeout=1000 \
    torch==1.6.0 torchvision==0.7.0 \
    -f https://mirrors.aliyun.com/pytorch-wheels/cpu/torch_stable.html \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 安装TensorFlow
RUN pip install --no-cache-dir tensorflow==2.3.1 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/


# 安装其他依赖
RUN pip install --no-cache-dir \
    pandas==0.25.2 \
    scikit-learn==0.21.3 \
    seaborn==0.10.0 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/

WORKDIR /app
CMD ["bash"]