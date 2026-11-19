FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends openjdk-17-jdk-headless \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 \
    PYSPARK_PYTHON=/usr/local/bin/python \
    PYSPARK_DRIVER_PYTHON=/usr/local/bin/python \
    SPARK_LOCAL_IP=127.0.0.1

RUN python -m pip install --no-cache-dir pyspark==4.0.1

USER vscode
