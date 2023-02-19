FROM python:3.9

ADD . . 

RUN pip freeze > requirements.txt

CMD ["python",  "./main.py"]