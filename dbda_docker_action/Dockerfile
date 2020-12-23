FROM ubuntu:20.04
RUN apt-get update -y \
    && apt-get -y install python3-pip
WORKDIR /opt
COPY . /opt
RUN ls -l /opt
RUN ["/bin/bash", "-c", "cd /opt && ls && python3 log_create.py && ls -l"]
