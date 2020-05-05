# This Service creates lambdas execute AWS CLI commands.
These lambdas uses AWS CLI package layer to execute AWS CLI commands.

## Instructions:

After the function is created (sls deploy), in Designer in AWS functions console, click on Layers, click Add layer and select the layer you've just created. https://github.com/triluong21/awscli-lambda-layer
Then use Postman tests in /test folder to try. 