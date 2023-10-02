import boto3

def insert_data_to_dynamodb(table_name, document_id, data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(
            Item={
                'DocumentID': document_id,
                'Data': data
            }
        )
        print("Data inserted into DynamoDB successfully.")
        return True
    except Exception as e:
        print(f"Error inserting data into DynamoDB: {e}")
        return False

# Replace 'your-dynamodb-table-name', 'your-document-id', and 'your-data' with your data values.
table_name = 'your-dynamodb-table-name'
document_id = 'your-document-id'
data = 'your-data'

insert_data_to_dynamodb(table_name, document_id, data)
