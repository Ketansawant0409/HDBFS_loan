import boto3
import io
from PyPDF4 import PdfFileReader, PdfFileWriter

def lambda_handler(event, context):
    try:
        bucket_name = 'newproject0409'
        folder_prefix = "project0409/"
        output_bucket = 'newproject0409'
        
        
        s3_client = boto3.client('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
        s3_resource = boto3.resource('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")

        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix, Delimiter='/')
        objects = response['Contents']

        if objects:
            sorted_objects = sorted(objects, key=lambda obj: obj['LastModified'], reverse=True)
            file_name = sorted_objects[0]['Key']
            file = file_name[12::]
            print(file)
            splitted=file.split(".")
            unique_code=splitted[-1]
            print(unique_code)

            input_object_key = file_name
            print(input_object_key)
            obj = s3_resource.Object(bucket_name, input_object_key).get()
            pdf_content = obj['Body'].read()
            pdf_file = io.BytesIO(pdf_content)
            pdf_reader = PdfFileReader(pdf_file)

            for page_number in range(pdf_reader.getNumPages()):
                print(page_number)
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(page_number))
                output_object_key = f"separated/{file}/{file}_{page_number + 1}.pdf"
                print(output_object_key)
                output_pdf_bytes = io.BytesIO()
                pdf_writer.write(output_pdf_bytes)

                s3_client.put_object(Body=output_pdf_bytes.getvalue(), Bucket=output_bucket, Key=output_object_key)

            status = "Stage 1 done, Stage 2 in process"
        
        else:
            status = "No objects found in the specified bucket."

    except Exception as e:
        bucket_name = 'newproject0409'
        folder_prefix = "project0409/"
        output_bucket = 'newproject0409'
        
        
        s3_client = boto3.client('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
        s3_resource = boto3.resource('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")

        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix, Delimiter='/')
        objects = response['Contents']

        if objects:
            sorted_objects = sorted(objects, key=lambda obj: obj['LastModified'], reverse=True)
            file_name = sorted_objects[0]['Key']
            file = file_name[12:-1]
            splitted=file.split(".")
            unique_code=splitted[-1]
            print(unique_code)
        status = "error: " + str(e)  
        print(e)
    
    dynamodb_client = boto3.client('dynamodb', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
    
    table_name = 'newtable'
    item = {
        'unique_code': {'S': unique_code},
        'Status': {'S': status}
    }

    try:
        dynamodb_client.put_item(
            TableName=table_name,
            Item=item
        )
        print("Item inserted successfully into DynamoDB!")
    except Exception as e:
        print(f"Error inserting item into DynamoDB: {e}")

    return f"Pages separated successfully and stored in S3 bucket: {output_bucket}. Status: {status}"