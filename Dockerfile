FROM python:alpine3.7
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install psutil 
CMD python ./date.py
