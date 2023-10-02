import boto3
import zipfile
import io


s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")  # Specify the appropriate region


bucket_name = 'newproject0409'
zip_file_key = 'zipfolder.zip'
destination_prefix = "unzipfolder/"

try:
    # Download the zip file from S3
    zip_file_obj = s3.get_object(Bucket=bucket_name, Key=zip_file_key)
    zip_content = zip_file_obj['Body'].read()

    # Unzip the file
    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_ref:
        for file_info in zip_ref.infolist():
            file_name = file_info.filename
            if not file_name.endswith('/'):  # Skip directories
                file_content = zip_ref.read(file_info)
                s3_key = destination_prefix + file_name
                s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)
                print(f"Uploaded: {s3_key}")

    print("Unzipped and uploaded successfully!")

except Exception as e:
    print("Error:", e)

   
