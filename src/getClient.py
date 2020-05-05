import json
from src.functions import run_command

def getClientSecret(event, context):
    # run_command('/opt/aws --version')
    poolId = event['pathParameters']['poolId']
    clientId = event['pathParameters']['clientId']
    getClientSecretCommand = '/opt/aws cognito-idp describe-user-pool-client --client-id ' + clientId + ' --user-pool-id ' + poolId
    command_result = run_command(getClientSecretCommand)
    if command_result == False:
        i_message = "Fail big time."
    else:
        i_message = "Your function executed successfully!"
        data = json.loads(command_result)
        clientObject = {}
        clientObject['ClientName'] = data['UserPoolClient']['ClientName']
        clientObject['ClientId'] = data['UserPoolClient']['ClientId']
        clientObject['ClientSecret'] = data['UserPoolClient']['ClientSecret']
    
    body = {
        "message": i_message,
        "info": clientObject
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
