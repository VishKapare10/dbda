
FROM ubuntu:20.04
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update
WORKDIR /opt
COPY . /opt
COPY -r ./inte_pycode ./opt
