import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb',region_name="us-east-1", aws_access_key_id="AKIAQXKGVPUEW3JFL4JY", aws_secret_access_key="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")

# Specify the table name
table_name = 'newtable'

# Perform a scan operation to retrieve all items in the table
response = dynamodb.scan(TableName=table_name)

# Get the count of items returned
item_count = response['Count']

print(f"Total number of items in '{table_name}': {item_count}")
