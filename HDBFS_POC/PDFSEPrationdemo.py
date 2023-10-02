
# import boto3
# from PyPDF4 import PdfFileReader, PdfFileWriter 
# import io 

# region_name="us-east-1"
# aws_access_key="AKIAS75ADNXVKGS4WMKB"
# secret_access_key="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"   
# bucket_name = "demoproject0409"
# input_object_key = "project0409/5. BGV.pdf"
# output_bucket = "demoproject0409"
# service_name="s3"

# def separation_pdf(bucket_name,input_object_key,service_name,region_name,aws_access_key,secret_access_key,output_bucket):
    
#     s3_client = boto3.client(service_name,region_name,aws_access_key_id=aws_access_key,aws_secret_access_key=secret_access_key)
#     s3_resource = boto3.resource(service_name,region_name,aws_access_key_id=aws_access_key,aws_secret_access_key=secret_access_key)

#     obj = s3_resource.Object(bucket_name, input_object_key).get()
#     pdf_content = obj['Body'].read()
#     pdf_file = io.BytesIO(pdf_content)
#     pdf_reader = PdfFileReader(pdf_file)

#     for page_number in range(pdf_reader.getNumPages()):
#         pdf_writer = PdfFileWriter()
#         pdf_writer.addPage(pdf_reader.getPage(page_number))
#         folder_name = f"page_{page_number + 1}"
#         output_object_key = f"projectfile/separated/{folder_name}/output.pdf"
#         output_pdf_bytes = io.BytesIO()
#         pdf_writer.write(output_pdf_bytes)

#         s3_client.put_object(Body=output_pdf_bytes.getvalue(), Bucket=output_bucket, Key=output_object_key)    
            
#     return f"Pages separated successfully and stored in S3 bucket: {output_bucket}"
            
# obj=separation_pdf(bucket_name,input_object_key,service_name,region_name,aws_access_key,secret_access_key,output_bucket)
# print(obj)


import boto3
from PyPDF4 import PdfFileReader, PdfFileWriter
import io

region_name = "us-east-1"
aws_access_key = "AKIAS75ADNXVKGS4WMKB"
secret_access_key = "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"
bucket_name = "demoproject0409"
input_object_key = "project0409/5. BGV.pdf"
output_bucket = "demoproject0409"
service_name = "s3"

def separation_pdf(bucket_name, input_object_key, service_name, region_name, aws_access_key, secret_access_key, output_bucket):
    s3_client = boto3.client(service_name, region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=secret_access_key)
    s3_resource = boto3.resource(service_name, region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=secret_access_key)

    obj = s3_resource.Object(bucket_name, input_object_key).get()
    pdf_content = obj['Body'].read()
    pdf_file = io.BytesIO(pdf_content)
    pdf_reader = PdfFileReader(pdf_file)

    for page_number in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page_number))

        output_pdf_bytes = io.BytesIO()
        pdf_writer.write(output_pdf_bytes)

        folder_name = f"page_{page_number + 1}"
        output_object_key = f"projectfile/separated/{folder_name}/output.pdf"

        s3_client.put_object(Body=output_pdf_bytes.getvalue(), Bucket=output_bucket, Key=output_object_key)

    return f"Pages separated successfully and stored in S3 bucket: {output_bucket}"

obj = separation_pdf(bucket_name, input_object_key, service_name, region_name, aws_access_key, secret_access_key, output_bucket)
print(obj)
