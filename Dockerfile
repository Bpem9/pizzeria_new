FROM python:3.10.11-slim

RUN mkdir -p ./app/src && \
    apt-get update && \
    apt-get install -y libpq-dev gcc g++ gettext python-dev python3-dev libffi-dev musl-dev make libevent-dev \
        git libmagickwand-dev fontconfig lcdf-typetools openjdk-11-jre woff2

RUN pip install poetry==1.4.1 &&  \
    poetry config virtualenvs.create false

WORKDIR /app/src/
COPY ./src/poetry.lock ./src/pyproject.toml /app/src/

RUN cd /app/src && \
    poetry install --without dev

COPY ./src /app/src
ENV PYTHONUNBUFFERED=1

#CMD gunicorn config.wsgi --config ./config/gunicorn.py
CMD python manage.py runserver 0.0.0.0:8000

