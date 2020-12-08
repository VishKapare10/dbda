FROM ubuntu
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt update \
    && apt-get install -y git \
    && apt-get -y install python3-pip \
    && pip3 install ansible \
    && mkdir -p /opt/dbda  \
    && cd /opt/dbda \
    && git clone https://f999ccd543c206a3b744f129528dd77e254ec5bb@github.com/VishKapare10/dbda.git \
    && python3 dbda/date.py \
    && python3 dbda/r_no.py \
    && python3 dbda/bank_acc.py \
    && ansible-playbook dbda/debug_msg.yml \
    && echo inside container!
