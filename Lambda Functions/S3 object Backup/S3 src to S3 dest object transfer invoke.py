import boto3

def lambda_handler(event, context):
    # Define the source and destination S3 bucket names
    source_bucket_name = 'src-demo-bucket'  # Replace with your source bucket name
    destination_bucket_name = 'destntn-demo-bucket'  # Replace with your destination bucket name
    print(event)

    s3_client = boto3.client('s3')
    
    # Iterate through records in the event
    for record in event['Records']:
        
        # Extract the S3 object key from the event
        source_object_key = record['s3']['object']['key']
        print(source_object_key)

        # Copy the object from the source bucket to the destination bucket
        try:
            copy_source = {'Bucket': source_bucket_name, 'Key': source_object_key}
            destination_object_key = source_object_key  # You can modify the destination object key if needed
            s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket_name, Key=destination_object_key)
            print(f'Copied object from {source_bucket_name}/{source_object_key} to {destination_bucket_name}/{destination_object_key}')
        except Exception as e:
            print(f'Error copying object: {str(e)}')
    
    return {
        'statusCode': 200,
        'body': 'Object copy process completed.'
    }
