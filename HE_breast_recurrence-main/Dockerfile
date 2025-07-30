# Use full Python base image
FROM python:3.6-bullseye

WORKDIR /app

# install libgl1
RUN apt-get update && apt-get install -y --no-install-recommends libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU version
RUN pip install torch==1.8.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Install PyTorch Geometric and related libraries (CPU version)
RUN pip install \
    torch-scatter==2.0.6 -f https://data.pyg.org/whl/torch-1.8.0+cpu.html \
    torch-sparse==0.6.10 -f https://data.pyg.org/whl/torch-1.8.0+cpu.html \
    torch-cluster==1.5.9 -f https://data.pyg.org/whl/torch-1.8.0+cpu.html \
    torch-geometric==2.0.3

# Install RDKit (using rdkit-pypi)
RUN pip install rdkit-pypi==2021.9.4  #changed version from 2020.9., using latest version

# Install DeepChem and PubChemPy
RUN pip install deepchem==2.5.0 pubchempy==1.0.4

RUN pip install tensorflow thop
# Default command
CMD ["python"]
