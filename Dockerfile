FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip freeze > requirements.txt

ADD . .

CMD ["python",  "./main.py"]