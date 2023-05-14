FROM python:3.9
COPY . /app1
WORKDIR /app1
CMD python guis.py
