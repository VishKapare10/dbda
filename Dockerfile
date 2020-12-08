FROM ubuntu
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update -y \
    && apt-get -y install python3-pip \
    && pip3 install ansible
RUN python3 date.py
RUN echo inside container!
