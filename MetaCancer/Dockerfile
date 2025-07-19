# Use full Python base image
FROM python:3.6-bullseye

WORKDIR /app

# install libgl1
RUN apt-get update && apt-get install -y --no-install-recommends libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Install from requirements.txt
RUN pip install -r ./code/requirements.txt

# Default command
CMD ["python"]
