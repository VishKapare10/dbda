FROM python:alpine3.7
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN python3 ./date.py
CMD python3 ./date.py > ./abc.txt
