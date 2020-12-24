FROM ubuntu:20.04
WORKDIR /opt
COPY . /opt
RUN ls -l /opt
