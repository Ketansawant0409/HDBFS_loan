
import boto3
import io
from PyPDF4 import PdfFileReader, PdfFileWriter

def lambda_handler():
    bucket_name = 'newproject0409'
    folder_prefix = 'project0409/'
    output_bucket = 'newproject0409'
    s3_client = boto3.client('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
    
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix, Delimiter='/')
    s3_resource = boto3.resource('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")

    for common_prefix in response.get('CommonPrefixes', []):
        folder_name = common_prefix['Prefix']
        folder = folder_name[12:17]
        print(folder)
        
        
        folder_response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
        
        for obj in folder_response.get('Contents', []):
            object_key = obj['Key']
            file_name = object_key.split('/')[-1]
            print(file_name)
            
            
            if not file_name:
                continue
            else:
                input_object_key = f"project0409/{folder}/{file_name}"
                obj = s3_resource.Object(bucket_name, input_object_key).get()
                pdf_content = obj['Body'].read()
                pdf_file = io.BytesIO(pdf_content)
                pdf_reader = PdfFileReader(pdf_file)
                
                for page_number in range(pdf_reader.getNumPages()):
                    pdf_writer = PdfFileWriter()
                    pdf_writer.addPage(pdf_reader.getPage(page_number))
                    output_object_key = f"project0409/{folder}/separated9/{file_name}_{page_number + 1}.pdf"
                    output_pdf_bytes = io.BytesIO()
                    pdf_writer.write(output_pdf_bytes)

                    s3_client.put_object(Body=output_pdf_bytes.getvalue(), Bucket=output_bucket, Key=output_object_key)
                
    return f"Pages separated successfully and stored in S3 bucket: {output_bucket}"


lambda_handler()