FROM python:3.8-bullseye

WORKDIR /app

COPY . /app

RUN pip install sklearn

CMD ["matlab", "-batch", "momlin_docker_entry"]
