FROM python:3.8-bullseye

WORKDIR /app

COPY . /app

RUN pip install "joblib>=1.2.0" "lifelines>=0.27.4" "numpy>=1.21.5" "pandas==1.5.3" "pyyaml>=6.0" "torch>=2.0.1" "scikit-learn>=1.2.0" "scikit-survival>=0.21.0" "statsmodels>=0.13.5" "tensorboard>=2.8.0" "tqdm>=4.63.0"

CMD ["matlab", "-batch", "momlin_docker_entry"]
