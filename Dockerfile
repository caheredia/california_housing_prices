# add miniconda image 
FROM continuumio/miniconda3:4.8.2

# our current verison of fico xpress - 8.8.0 - needs libncurses5...for more details see:
# https://bitbucket.org/wlearn/python-base/pull-requests/25
RUN apt-get update && \
        apt-get install -y  --no-install-recommends \
        && rm -rf /var/lib/apt/lists/*

COPY environment.yml environment.yml
RUN conda env update --name base --file environment.yml \
    && conda clean --all --yes

ENTRYPOINT [ "python3" ]
