FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 as uvicorn-fastapi-texlive-stage

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN pip install -U pip && pip install -U -r /requirements.txt