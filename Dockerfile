FROM python:3.9

ENV DockerHome=/home/app/webapp

RUN mkdir -p $DockerHome

WORKDIR $DockerHome

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/DelphinePythonique/projet13 .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000