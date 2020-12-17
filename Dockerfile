
FROM ubuntu:20.04
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update \
    && apt-get install -y git \
    && apt-get -y install python3-pip \
    && git clone https://f999ccd543c206a3b744f129528dd77e254ec5bb@github.com/VishKapare10/dbda.git \
    && echo inside container!
WORKDIR /opt
COPY . /opt
RUN curl https://github.com/VishKapare10/dbda/releases/tag/refs%2Fheads%2Fmaster/my-artifact.zip
CMD find . -name "*.py" | xargs -n 1 python3
