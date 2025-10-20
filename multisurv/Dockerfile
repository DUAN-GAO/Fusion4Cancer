FROM python:3.9-bullseye

WORKDIR /app

COPY . /app

RUN pip install tensorboard-data-server==0.7.2 texttable==1.7.0 threadpoolctl==3.6.0 tifffile==2025.5.10 tomli==2.3.0 torch==2.8.0 torchtuples==0.2.2 torchvision==0.23.0 tqdm==4.67.1 triton==3.4.0 typeguard==4.4.4 typing_extensions==4.15.0 tzdata==2025.2 urllib3==2.5.0 wadler_lindig==0.1.7 Werkzeug==3.1.3 wheel==0.45.1 wrapt==1.17.3 wsipre==0.1.2 zstandard==0.25.0
 
CMD ["matlab", "-batch", "momlin_docker_entry"]
