import json
import boto3

def lambda_handler():
    try:
        s3_client = boto3.client('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")

        bucket_name = "newproject0409"
        folder_prefix = "separated/"

        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix, Delimiter='/')
        folder_names = [prefix['Prefix'] for prefix in response.get('CommonPrefixes', [])]
        sorted_folders = sorted(folder_names, key=lambda folder: s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder)['Contents'][0]['LastModified'], reverse=True)

        if sorted_folders:
            folder_name = sorted_folders[0]
            print("Most recently created folder:", folder_name) 
            
        else:
            print("No folders found in the specified bucket.")

        folder_response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

        for obj in folder_response.get('Contents', []):
            object_key = obj['Key']
            file_name = object_key.split('/')[-1]
            print(file_name)

            string = ""
            input_object_key = f"{folder_name}{file_name}"
            print(input_object_key)

            textract_client = boto3.client('textract', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")

            response = textract_client.detect_document_text(Document={'S3Object': {'Bucket': bucket_name, 'Name': input_object_key}})

            extracted_text = ""
            for item in response['Blocks']:
                if item['BlockType'] == 'LINE':
                    extracted_text += item['Text'] + "\n"

            count = 0
            string = extracted_text.split()
            for i in range(len(string)):
                if count == 2:
                    break
                else:
                    if string[i] == "NAME":
                        Employee_name = string[i + 1] + " " + string[i + 2] + " " + string[i + 4]
                        count = count + 1

                    elif string[i] == "EMPLOYEE" and string[i + 1] == "CODE":
                        Employee_code = string[i + 2]
                        count = count + 1

                    else:
                        continue

        status = "Sucesssfully all stages completed"

    except Exception as e:
        status = "error: " + str(e)  # Capture the exception message
        print(e)

    dynamodb_client = boto3.client('dynamodb', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")

    table_name = 'newtable'

    item = {
        'Employee_name': {'S': Employee_name},
        'Employee_code': {'S': Employee_code},
        'unique_code': {'S': unique_code},
        'Status': {'S': status}
    }

    try:
        dynamodb_client.put_item(
            TableName=table_name,
            Item=item
        )
        print("Item inserted successfully!")
    except Exception as e:
        print(f"Error inserting item: {e}")
lambda_handler()