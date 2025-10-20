FROM python:3.9-bullseye

WORKDIR /app

COPY . /app

RUN pip install torch torchvision timm ultralytics

CMD ["matlab", "-batch", "momlin_docker_entry"]
