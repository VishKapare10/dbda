FROM ubuntu
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update
RUN python3 date.py
RUN echo inside container!
