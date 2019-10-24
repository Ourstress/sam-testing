# Container image that runs your code
FROM python:alpine

# install python
RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev\
    && pip install cython awscli aws-sam-cli\
    && apk del .build-deps 

# install awscli and zip
RUN apk add zip

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["sh", "/entrypoint.sh"]