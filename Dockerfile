FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./Pipfile ./Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

COPY ./app /code/app

ENV PYTHONPATH=/code/app

EXPOSE 8000
