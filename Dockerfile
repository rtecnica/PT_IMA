FROM python:3.9-alpine

COPY / /app
WORKDIR /app

RUN pip3 install -r /app/requirements.txt

CMD python /app/main.py