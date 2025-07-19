# Use full Python base image (not slim)
FROM python:3.9-bullseye

WORKDIR /app

# install libgl1
RUN apt-get update && apt-get install -y --no-install-recommends libgl1 && \
    rm -rf /var/lib/apt/lists/*


# Install PyTorch CPU version
RUN pip install torch==1.11.0+cpu torchvision==0.12.0+cpu torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cpu

# Install DGL CPU version
RUN pip install dgl==0.9 -f https://data.dgl.ai/wheels/repo.html

# Install RDKit
RUN pip install rdkit-pypi

# Install other Python libraries
RUN pip install \
    dgllife \
    matplotlib \
    seaborn \
    lifelines \
    prettytable \
    pubchempy \
    fitlog \
    subword_nmt \
    tensorboard \
    transformers==4.29.0 \
# Default command
CMD ["python"]
