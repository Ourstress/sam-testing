# Container image that runs your code
FROM python:alpine

# install python
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install cython \
    && apk del .build-deps 

# install awscli and zip
RUN pip3 install awscli 
RUN pip3 install regex
RUN pip3 install aws-sam-cli
RUN apk add zip

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["sh", "/entrypoint.sh"]