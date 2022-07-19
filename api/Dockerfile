# base image
FROM python:3.9

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /api

# add application and install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile
COPY . ./

# entrypoint
RUN chmod a+x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
