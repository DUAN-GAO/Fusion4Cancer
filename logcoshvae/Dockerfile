FROM python:3.9-bullseye

WORKDIR /app

COPY . /app

RUN pip install numpy pandas scikit-learn matplotlib keras tensorflow joblib

CMD ["matlab", "-batch", "momlin_docker_entry"]
