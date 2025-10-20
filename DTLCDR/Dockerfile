FROM python:3.8-bullseye

WORKDIR /app

COPY . /app

RUN pip install torch_geometric cudatoolkit dgl dgllife torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html

CMD ["matlab", "-batch", "momlin_docker_entry"]
