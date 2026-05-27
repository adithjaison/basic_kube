FROM python:3.11.5 AS base

ENV PATH="/scripts:${PATH}"

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ./docker/basic_kube/requirements.txt /requirements.txt
COPY ./docker/basic_kube/scripts /scripts
RUN chmod +x /scripts/*
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /basic_kube

COPY . /basic_kube/

FROM base AS dev

CMD ["/scripts/start_runserver.sh"]

FROM dev AS prod
RUN apt-get update && apt-get install -y --no-install-recommends \
        daphne \
    && rm -rf /var/lib/apt/lists/*

#CMD ["/scripts/start_prod_server.sh"]
