# Use full Python base image
FROM python:3.9-bullseye

WORKDIR /app

# install libgl1
RUN apt-get update && apt-get install -y --no-install-recommends libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU version
RUN pip install -r requirement.txt
# Default command
CMD ["python"]
