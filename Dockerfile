FROM ubuntu
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update
RUN python3 date.py
