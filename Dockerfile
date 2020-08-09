FROM continuumio/miniconda3:4.8.2

RUN apt-get update && \
        apt-get install -y  --no-install-recommends \
        && rm -rf /var/lib/apt/lists/*

COPY environment.yml environment.yml
RUN conda env update --name base --file environment.yml \
    && conda clean --all --yes

ENTRYPOINT [ "python3" ]
