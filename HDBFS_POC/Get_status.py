# import boto3


# dynamodb = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")  # Specify the appropriate region


# table_name = 'newtable'

# try:
    
#     response = dynamodb.scan(
#         TableName=table_name,
        
#     )
    
#     for item in response.get('Items', []):
#         field1 = item.get('place', {}).get('S', 'N/A')
#         field2 = item.get('Date', {}).get('S', 'N/A')
#         print(f"employee name: {field1} {field2} succesfully updated")
        

# except Exception as e:
#     print("Error:", e)
    
    
# import requests


# api_url = 'https://your-api-url.com/endpoint'



# headers = {
#     'Content-Type': 'application/octet-stream',  
   
# }

# response = requests.post(api_url, data=file_data, headers=headers)


# print(f"Response status code: {response.status_code}")
# print("Response body:")
# print(response.text)




import json


def lambda_handler(event, context):
    # Process the uploaded file here
    
    # Assuming processing is complete
    response_message = "Work completed"
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response_message
        })
    }










import json

2

3

print('Loading function")

Code entry type

Edit code inline

5

6

7
import json
def lambda_handler(event, context):

    transactionId=event['queryStringParameters']['transactionId']
  
    print('transactionId="transactionId)

    transactionResponse ={}

    transactionResponse[ 'transactionId'] transactionId 
    transactionResponse['message'] = 'Hello from Lambda land"

    responseObject ={}
    responseObject['statusCode'] - 200
    responseObject['headers'] {}
    responseObject['headers']['Content-Type'] = 'application/json' 
    responseObject['body'] json.dumps (transactionResponse)

    return responseObject

