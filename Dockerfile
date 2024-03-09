FROM python:3.10.10-slim-bullseye AS base

FROM base AS builder

COPY requirements.txt /requirements.txt
RUN mkdir /install
RUN pip install --prefix=/install --no-warn-script-location -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
RUN apt-get clean && apt-get update && apt-get install -y build-essential git

RUN mkdir /app
COPY . /app

EXPOSE 5000
ENTRYPOINT ["bash", "/app/docker-entrypoint.sh"]
