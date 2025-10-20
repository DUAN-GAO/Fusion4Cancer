FROM python:3.8-bullseye

WORKDIR /app

COPY . /app

RUN pip install pandas==1.1.5 numpy==1.19.5 networkx==2.5.1 scikit-learn==0.24.2 keras==2.2.4 tensorflow==2.1.0

CMD ["matlab", "-batch", "momlin_docker_entry"]
