# Use official Python base image
FROM python:3.6-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for RDKit and other scientific packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU version
RUN pip install torch==1.8.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Install PyTorch Geometric and related libraries (CPU version)
RUN pip install \
    torch-scatter==2.0.6 -f https://data.pyg.org/whl/torch-1.8.0+cpu.html \
    torch-sparse==0.6.10 -f https://data.pyg.org/whl/torch-1.8.0+cpu.html \
    torch-cluster==1.5.9 -f https://data.pyg.org/whl/torch-1.8.0+cpu.html \
    torch-geometric==2.0.3

# Install RDKit (using rdkit-pypi)
RUN pip install rdkit-pypi==2020.9.1.0

# Install DeepChem and PubChemPy
RUN pip install deepchem==2.5.0 pubchempy==1.0.4

# Default command
CMD ["python"]
