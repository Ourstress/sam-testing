#!/bin/sh -l

export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION
export AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN
export APINAME="$LAMBDA_FUNC_NAME-API"
export OVERLAY_S3URL="s3://${BUCKET_NAME}/${LAMBDA_FUNC_NAME}/lambda-deploy.tgz"


rm -f lambda-deploy.zip
cd sam-app; 
cd sam-checker; zip -r ../lambda-deploy.zip *
cd ..

if sh deploy.sh
    then 
        exit 0
    else
        exit 1
fi
    
exit 0 