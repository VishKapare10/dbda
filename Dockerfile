
FROM ubuntu:20.04
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update \
    && apt-get install -y git \
    && apt-get -y install python3-pip \
    && pip3 install ansible \
    && mkdir -p /opt/dbda  \
    && cd /opt/dbda \
    && git clone https://f999ccd543c206a3b744f129528dd77e254ec5bb@github.com/VishKapare10/dbda.git \
    && echo inside container!
WORKDIR /opt/dbda/code
CMD find . -name "*.yml" | xargs -n 1 ansible-playbook
