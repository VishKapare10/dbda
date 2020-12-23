
FROM ubuntu:20.04
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update -y \
    && apt-get -y install python3-pip \
    && pip3 install ansible 
WORKDIR /opt
COPY ./inte_pycode /opt
RUN ls -l
CMD ansible-playbook ansible_code/demo_play.yml
CMD python3 ./log_create.py
