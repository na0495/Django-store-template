# base image
FROM python:3.9

#maintainer
LABEL Author="na0495"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#directory to store app source code
RUN mkdir /app

#switch to /app directory so that everything runs from here
WORKDIR /app

#copy the app code to image working directory
COPY ./app ./app

COPY requirements.txt requirements.txt

#let pip install required packages
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 8080
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
