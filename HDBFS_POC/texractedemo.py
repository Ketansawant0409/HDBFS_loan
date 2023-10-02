# import boto3

# s3_client = boto3.client('s3', region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")
    
# bucket_name = "newproject0409"
# folder_prefix = "separated/"
    
# response = s3_client.list_objects_v2(Bucket=bucket_name,Prefix=folder_prefix, Delimiter='/')
# folder_names = [prefix['Prefix'] for prefix in response.get('CommonPrefixes', [])]
# sorted_folders = sorted(folder_names, key=lambda folder: s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder)['Contents'][0]['LastModified'], reverse=True)
    
# if sorted_folders:
#         folder_name = sorted_folders[0]
#         print("Most recently created folder:", folder_name)
# else:
#         print("No folders found in the specified bucket.")     
  
# folder_response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
        
# for obj in folder_response.get('Contents', []):
#             object_key = obj['Key']
#             file_name = object_key.split('/')[-1]
#             print(file_name)
            
#             string=""
#             input_object_key = f"{folder_name}{file_name}"
#             print(input_object_key)
                            

#             textract_client = boto3.client('textract',region_name="us-east-1",
#                                                         aws_access_key_id="AKIAQXKGVPUEW3JFL4JY",
#                                                         aws_secret_access_key="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")

#             response = textract_client.detect_document_text( Document={'S3Object': {'Bucket': bucket_name,'Name': input_object_key}})   
                                
#             extracted_text = ""
#             for item in response['Blocks']:
#                                         if item['BlockType'] == 'LINE':
#                                             extracted_text += item['Text'] + "\n"
#             print(extracted_text)                                
            
#             count=0
#             string=extracted_text.split()   
#             for i in range(len(string)):
#                 if(count==3):
#                     break
#                 else:
#                     if(string[i]=="NAME"):
#                         Employee_name = string[i+1]+" "+string[i+2]+" "+string[i+3]+" "+string[i+4]
#                         count=count+1  
                                        
#                     elif(string[i]=="EMPLOYEE" and string[i+1]=="CODE"):
#                         Employee_code= string[i+2]
#                         count=count+1
                        
#                     elif(string[i]=="JOINING" and string[i+1]=="DATE"):
#                         joining_date=string[i+2] 
#                         count=count+1
                         
#                     else:
#                         continue
# print(Employee_name,Employee_code,joining_date)                    

                                
# dynamodb_client = boto3.client('dynamodb',region_name="us-east-1",
#                                     aws_access_key_id="AKIAQXKGVPUEW3JFL4JY",
#                                     aws_secret_access_key="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")

# table_name = 'newtable'
# item = {
#             'Employee_name': {'S': Employee_name},  
#             'Employee_code': {'S':Employee_code }
            
#         }
# try:
#             response = dynamodb_client.put_item(TableName=table_name, Item=item)
#             print("Item inserted successfully!")
# except Exception as e:
#             print(f"Error inserting item: {e}")



import boto3

bucket_name = "newproject0409"
input_object_key= "separated/filename.2/filename.2_1.pdf"

textract_client = boto3.client('textract',region_name="us-east-1",
                                                        aws_access_key_id="AKIAQXKGVPUEW3JFL4JY",
                                                        aws_secret_access_key="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")

response = textract_client.detect_document_text( Document={'S3Object': {'Bucket': bucket_name,'Name': input_object_key}})   
                                
extracted_text = ""
for item in response['Blocks']:
                                        if item['BlockType'] == 'LINE':
                                            extracted_text += item['Text'] + "\n"
print(extracted_text)   















  
# writer = PyPDF4.PdfFileWriter()
# page_width = 612 
# page_height = 792 
# page = writer.addBlankPage(width=page_width, height=page_height)
# page.mergePage(PyPDF4.pdf.PageObject.createTextObject(string))
# with open('C:/Users/ketan/OneDrive/Desktop/HDBFS_POC/output.pdf', 'wb') as output_pdf:
#         string.write(output_pdf)
# s3_object_key="project0409/outputfolder/output.pdf"
# s3_client = boto3.client('s3')
# s3_client.upload_file('C:/Users/ketan/OneDrive/Desktop/HDBFS_POC/output.pdf', bucket_name, s3_object_key)
# print("done")

    







