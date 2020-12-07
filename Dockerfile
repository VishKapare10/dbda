FROM ubuntu
MAINTAINER vishwambhar.kapare@paroscale.com
RUN apt-get update
CMD ["ls", "-l"]
