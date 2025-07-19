FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install --no-cache-dir setuptools==58.0.4 wheel==0.37.1 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install --no-cache-dir --default-timeout=1000 \
    torch==1.6.0 torchvision==0.7.0 \
    -f https://mirrors.aliyun.com/pytorch-wheels/cpu/torch_stable.html \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install --no-cache-dir tensorflow==2.3.1 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/


RUN pip install --no-cache-dir \
    pandas==0.25.2 \
    scikit-learn==0.21.3 \
    seaborn==0.10.0 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/

WORKDIR /app
CMD ["bash"]