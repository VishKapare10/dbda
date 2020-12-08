FROM ubuntu:18.04
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update -y \
    && apt-get -y install python3-pip \
    && pip3 install ansible \
    && mkdir -p /opt/dbda  \
    && COPY /date.py /opt/dbda \
    && cd /opt/dbda
RUN pwd
RUN python3 --version
RUN python3 date.py
RUN echo inside container!
