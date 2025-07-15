# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional: for rdkit, scientific libraries)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU version
RUN pip install torch==1.11.0+cpu torchvision==0.12.0+cpu torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cpu

# Install DGL CPU version
RUN pip install dgl==0.6.1 -f https://data.dgl.ai/wheels/repo.html

# Install RDKit
RUN pip install rdkit-pypi

# Install Python libraries
RUN pip install \
    dgllife \
    matplotlib \
    seaborn \
    lifelines \
    prettytable \
    pubchempy \
    fitlog

# Default command (optional)
CMD ["python"]
