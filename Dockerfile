FROM python:3.11-slim-buster

WORKDIR /app
COPY . /app


RUN apt update -y && apt install awscli -y

RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install -r requirements.txt

CMD ["python", "application.py"]

