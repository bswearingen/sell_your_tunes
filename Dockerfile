# Pull base image
FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .