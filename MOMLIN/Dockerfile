# 基于官方MATLAB镜像
FROM mathworks/matlab:r2024a

# 设置工作目录
WORKDIR /app

# 复制整个项目文件
COPY . /app

# 容器启动时自动运行的入口脚本
CMD ["matlab", "-batch", "momlin_docker_entry"]
