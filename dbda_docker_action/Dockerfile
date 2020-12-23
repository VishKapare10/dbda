FROM ubuntu:20.04
RUN apt-get update -y \
    && apt-get -y install python3-pip
WORKDIR /opt
COPY . /opt
RUN ls -l /opt
RUN ls -l /opt/inte_pycode
CMD ["/bin/bash", "-c", "cd /opt && ls && python3 inte_pycode/log_create.py && ls -l"]
