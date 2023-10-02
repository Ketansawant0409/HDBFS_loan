# 

{
  "Comment": "Data Processing Pipeline",
  "StartAt": "InvokeFirstLambda",
  "States": {
    "InvokeFirstLambda": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "AXIS"
      },
      "Next": "InvokeSecondLambda"
    },
    "InvokeSecondLambda": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "textExatraction"
      },
      "End": true
    }
  }
}



import boto3                                                            #module to interact with AWS service(S3)
import io                                                               #module to convert Byte to int
from PyPDF4 import PdfFileReader, PdfFileWriter                         #module to perform operations on PDF

def lambda_handler(event, context):                                       #aws Lambda function
    bucket_name = ' '                                              #AWS Credentials
    folder_prefix = ' '
    output_bucket = ' '
    access_key_id=" "
    secret_access_key=" "

    s3_client = boto3.client('s3', region_name="us-east-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)    #using s3_client methods
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix, Delimiter='/')                                        #getting content of bucket
    s3_resource = boto3.resource('s3', region_name="us-east-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)  #using S3_resources methods

    for common_prefix in response.get('CommonPrefixes', []):                                    #iterating through folders of s3 bucket
        folder_name = common_prefix['Prefix']
        folder = folder_name[12:17]                                                              #assigning variable a foldername
        print(folder)
        count=0                                                                                  #counter for only one file from folder
        
        folder_response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)      #access each folder
       
        for obj in folder_response.get('Contents', []):                                           #iterating through names of files of folders                    
            object_key = obj['Key']
            file_name = object_key.split('/')[-1]                                                 #assigning variable a filename
            
            if(count==1):                                                                                                                                   
                break
            else:
                print(file_name)
            
                if not file_name:
                    continue
                else:
                    count=count+1
                    input_object_key = f"project0409/{folder}/{file_name}"
                    obj = s3_resource.Object(bucket_name, input_object_key).get()
                    pdf_content = obj['Body'].read()
                    pdf_file = io.BytesIO(pdf_content)
                    pdf_reader = PdfFileReader(pdf_file)
                    
                    for page_number in range(pdf_reader.getNumPages()):
                        pdf_writer = PdfFileWriter()
                        pdf_writer.addPage(pdf_reader.getPage(page_number))
                        output_object_key = f"project0409/{folder}/separated/{file_name}_{page_number + 1}.pdf"
                        output_pdf_bytes = io.BytesIO()
                        pdf_writer.write(output_pdf_bytes)
    
                        s3_client.put_object(Body=output_pdf_bytes.getvalue(), Bucket=output_bucket, Key=output_object_key)
                
    return f"Pages separated successfully and stored in S3 bucket: {output_bucket}"
    
    



{
"Comment": "Transaction Processor State Machine Using SQS",
"StartAt":"ProcessTransaction",
"States":{
  "ProcessTransaction":{
  "Type":"Pass",
  "Next":"BroadcastToSqs"
},
"BroadcastToSqs":{
    "Type":"Task",
    "Resource": "arn:aws:states:::sqs:sendMessage",
    "Parameters":{
        "QueueUrl":"",
        "MessageBody":{
        "MessageBody.$":"$. MessageBody",
    }
},
"End":true
}}}














