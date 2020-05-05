import json
from src.functions import run_command

def createAppClient(event, context):
    goodToRun = True
    errorMessage = ""
    request_body = json.loads(event['body'])
    print(request_body)
    poolId = request_body['poolId']
    appClientName = request_body['appClientName']
    scopesArray = request_body['scopes']
    scopesString = ""
    print(scopesArray)
    if len(scopesArray) > 3:
      goodToRun = False
      errorMessage = "Only allow 3 scopes max"
    else:
      count=0
      while(count<3):
        scopesString = scopesArray[count] + ' '
        count +=1
        
    if goodToRun == True:
      createAppClientCommand = '/opt/aws cognito-idp create-user-pool-client --user-pool-id ' + poolId + ' --client-name ' + appClientName + ' --generate-secret --allowed-o-auth-flows client_credentials --allowed-o-auth-scopes ' + scopesString + '--allowed-o-auth-flows-user-pool-client'
      command_result = run_command(createAppClientCommand)
    
      if command_result == False:
        i_message = "Fail big time."
        data = "Command failed. Review lambda log in Cloudwatch for error message."
      else:
        i_message = "Your function executed successfully!"
        data = json.loads(command_result)
    else:  
      i_message = "Fail big time."
      data = "Validation error. " + errorMessage

    body = {
        "message": i_message,
        "info": data
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
