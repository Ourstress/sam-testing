#!/bin/bash

sam build --use-container
sam package --output-template \
    packaged.yaml --s3-bucket hello888
sam  deploy --template-file packaged.yaml \
    --region us-east-1 --capabilities \
    CAPABILITY_IAM --stack-name hello888