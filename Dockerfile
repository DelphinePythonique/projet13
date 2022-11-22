FROM python:3.9

ENV DockerHome=/home/app/webapp

RUN mkdir -p $DockerHome

WORKDIR $DockerHome

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

# Create dir and user
RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system --group app

# Setup app directory and variables
ENV HOME=/home/app
ENV APP_HOME=$HOME/web
RUN mkdir $APP_HOME && mkdir -p $HOME/logs
WORKDIR $APP_HOME

# Copy project and allow our user to run it
COPY ./project13 $APP_HOME
RUN chown -R app:app $HOME
USER app

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000