# Use full Python base image
FROM python:3.6-bullseye

WORKDIR /app

# install libgl1
RUN apt-get update && apt-get install -y --no-install-recommends libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU version
RUN pip install torch==1.10+cpu -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install Numpy==1.19.2  

RUN pip install scikit-learn==0.24.2

RUN pip install scipy==1.5.4

RUN pip install fitlog

RUN pip install requests

RUN pip install pandas

RUN pip install tqdm
# Default command
CMD ["python"]
