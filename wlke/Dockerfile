FROM python:3.8.3
LABEL maintainer="haudraufhaun"

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y apt-utils 

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

COPY . /code/

RUN apt-get update &&  apt-get install -y netcat
 
ENTRYPOINT ["/code/entrypoint.sh"]
