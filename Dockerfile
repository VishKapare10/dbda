FROM ubuntu:20.04
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update \
    && apt-get install -y git \
    && apt-get -y install python3-pip \
    && mkdir -p /opt/dbda  \
    && cd /opt/dbda \
    && git clone https://f999ccd543c206a3b744f129528dd77e254ec5bb@github.com/VishKapare10/dbda.git \
    && python3 dbda/code/date.py \
    && python3 dbda/code/r_no.py \
    && python3 dbda/code/bank_acc.py \
    && echo inside container!
CMD cd /opt/dbda \
    && python3 dbda/code/date.py
