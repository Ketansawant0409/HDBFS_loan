import boto3
import io
import uuid
from PyPDF4 import PdfFileReader, PdfFileWriter

def lambda_handler(event,context):
    try:
        aws_access_key_id = "AKIAQXKGVPUEW3JFL4JY"
        aws_secret_access_key = "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"
        region_name = "us-east-1"
        bucket_name = 'newproject0409'
        folder_prefix = "project0409/"
        output_bucket = 'newproject0409'

        dynamodb_client = boto3.client('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        s3_client = boto3.client('s3', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        s3_resource = boto3.resource('s3', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        table_name = 'newtable'
        unique_code = str(uuid.uuid4())  # Generate a unique UUID
        
        item = {
            'unique_code': {'S': unique_code},
            "Employee_name": {'S': "NA"},
            "Employee_code": {'S': "NA"},
            "Status": {'S': "in_Process"}
        }
        dynamodb_client.put_item(TableName=table_name, Item=item)


        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix, Delimiter='/')
        objects = response.get('Contents', [])

        if objects:
            sorted_objects = sorted(objects, key=lambda obj: obj['LastModified'], reverse=True)
            file_name = sorted_objects[0]['Key']
            splitted = file_name.split("/")
            split=splitted[-1].split(".")
            file=split[0]
            


            input_object_key = file_name
            obj = s3_resource.Object(bucket_name, input_object_key).get()
            pdf_content = obj['Body'].read()
            pdf_file = io.BytesIO(pdf_content)
            pdf_reader = PdfFileReader(pdf_file)

            for page_number in range(pdf_reader.getNumPages()):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(page_number))
                output_object_key = f"separated/{file}/{file}_{page_number + 1}.pdf"
                output_pdf_bytes = io.BytesIO()
                pdf_writer.write(output_pdf_bytes)

                s3_client.put_object(Body=output_pdf_bytes.getvalue(), Bucket=output_bucket, Key=output_object_key)

            status = "Stage 1 done, Stage 2 in process"
        
        else:
            status = "No objects found in the specified bucket."

    except Exception as e:
        status = "error: " + str(e)
        print(e)

    dynamodb_client = boto3.client('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

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
        print(unique_code)
    except Exception as e:
        print(f"Error inserting item into DynamoDB: {e}")

    return f"Pages separated successfully and stored in S3 bucket: {output_bucket}. Status: {status}. and unique_id {unique_code}"


























 

















