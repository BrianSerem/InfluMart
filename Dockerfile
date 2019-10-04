FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN  docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres

RUN pip install -r requirements.txt

