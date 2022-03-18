# base image
FROM python:3.9

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /api

# add application and install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
COPY . ./

# entrypoint
RUN chmod a+x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
