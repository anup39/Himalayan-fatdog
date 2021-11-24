FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update &&\
    apt-get install -y  libpangocairo-1.0 binutils libproj-dev gdal-bin gettext build-essential libffi-dev python-dev libpq-dev libc-dev curl gcc 


COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# ENTRYPOINT /code/entrypoint.sh