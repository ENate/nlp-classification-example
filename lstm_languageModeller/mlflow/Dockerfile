FROM ubuntu:22.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget build-essential time && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 

RUN conda --version

RUN conda init bash

RUN conda create -n myenv -c conda-forge -c bioconda python==3.10 pip

SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
EXPOSE 5000