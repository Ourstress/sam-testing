#!/bin/bash

sam build
sam package --output-template \
    packaged.yaml --s3-bucket aishu-samtest
sam  deploy --template-file packaged.yaml \
    --region ap-southeast-1 --capabilities \
    CAPABILITY_IAM --stack-name samTesting