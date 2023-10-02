# import boto3
# import requests
# import random
# import json


# def lambda_handler(event, context):
#     try:
#         random_number = random.randint(1, 100)

#         api_url = "YOUR_PUT_API_ENDPOINT_URL"

#         payload = {
#             "random_number": random_number
#         }

#         response = requests.put(api_url, json=payload)

      
#         if response.status_code == 200:
#             return {
#                 "statusCode": 200,
#                 "body": json.dumps(f"Successfully uploaded random number {random_number}")
#             }
#         else:
#             return {
#                 "statusCode": response.status_code,
#                 "body": json.dumps(f"Failed to upload random number. Status code: {response.status_code}")
#             }
#     except Exception as e:
#         return {
#             "statusCode": 500,
#             "body": json.dumps(f"An error occurred: {str(e)}")
#         }


# except Exception as e:
#         print("Error:", e)
        
# try:
        
#         response = dynamodb.scan(
#             TableName=table_name,
            
#         )
        
#         for item in response.get('Items', []):
#             field1 = item.get('Employee_code', {}).get('S', 'N/A')
            
#         return (f"{field1} succesfully updated")
            
    
# except Exception as e:
#         print("Error:", e)


import os

folder_path = "C:\\Users\\Acc User\\Desktop\\ACC\\ACC\\project0409\\fold2"

# Check if the given path is a directory
if os.path.isdir(folder_path):
    # List all files in the directory
    files = os.listdir(folder_path)
    
    # Filter out subdirectories (if needed)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    # Print the list of files
    for file in files:
        print(file)
else:
    print("Invalid folder path")
