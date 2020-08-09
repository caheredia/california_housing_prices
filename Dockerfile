FROM python:3.8.3-slim-buster
COPY ["pyproject.toml", "poetry.lock" , "./"]
RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get -y install gcc \
&& apt-get clean \ 
&& pip install --upgrade pip \
&& pip install poetry==1.0.3 && poetry config virtualenvs.create false \
&& poetry install --no-dev --no-interaction --no-ansi 
ENTRYPOINT [ "python3" ]
