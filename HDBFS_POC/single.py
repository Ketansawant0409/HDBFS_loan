import boto3
import io
from PyPDF4 import PdfFileReader, PdfFileWriter
import requests

def lambda_handler():
    bucket_name = 'newproject0409'
    folder_prefix="project0409/"
    output_bucket = 'newproject0409'
    s3_client = boto3.client('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
    s3_resource = boto3.resource('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
    
    dynamodb = boto3.client('dynamodb',region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
    table_name = 'newtable'
    response = dynamodb.scan(TableName=table_name)
    item_count = response['Count']
    print(f"Total number of items in '{table_name}': {item_count}")

    response = s3_client.list_objects_v2(Bucket=bucket_name,Prefix=folder_prefix, Delimiter='/')
    objects = response['Contents']

    if objects: 
        sorted_objects = sorted(objects, key=lambda obj: obj['LastModified'], reverse=True)
        file_name = sorted_objects[0]['Key']
        file=file_name[12:-4]
        print(file_name)
          

    response_data = {
        "message": "Work completed successfully",
        "additional_info": "Any additional information you want to include"
    }
    
    # POST the response data back to the PUT API
    api_url =f"https://opai2yay0b.execute-api.us-east-1.amazonaws.com/demo/newproject0409/{file_name}"
    print(api_url)
    #response = requests.post(api_url, json=response_data)
    
    # # Return a response
    # return {
    #     "statusCode": response.status_code,
    #     "body": json.dumps(response.json())
    # }      
                   
        # input_object_key = file_name
        # print(input_object_key)
        # obj = s3_resource.Object(bucket_name, input_object_key).get()
        # pdf_content = obj['Body'].read()
        # pdf_file = io.BytesIO(pdf_content)
        # pdf_reader = PdfFileReader(pdf_file)
        
                        
#         for page_number in range(pdf_reader.getNumPages()):
#                 print(page_number)
#                 pdf_writer = PdfFileWriter()
#                 pdf_writer.addPage(pdf_reader.getPage(page_number))
#                 output_object_key = f"separated/{file}/{file}_{page_number + 1}.pdf"
#                 print(output_object_key)
#                 print(output_object_key)
#                 output_pdf_bytes = io.BytesIO()
#                 pdf_writer.write(output_pdf_bytes)
                            
#                 s3_client.put_object(Body=output_pdf_bytes.getvalue(), Bucket=output_bucket, Key=output_object_key)
                    
#     return f"Pages separated successfully and stored in S3 bucket: {output_bucket}"
    
lambda_handler()    