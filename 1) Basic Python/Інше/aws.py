import boto3
# s3 = boto3.client('s3')
# response = s3.list_buckets()
# print(response)
# for b in response['Buckets']:
#     print(b['Name'])

# s3 = boto3.resource('s3')
#
# with open('info.txt', 'rb') as data:
#     s3.Bucket('bucket-1-us').put_object(Key='info.txt', Body=data)

# s3 = boto3.client('s3', region_name='us-east-1')
# s3.create_bucket(Bucket='bucket-1-us')
# print('Done.')
# s3 = boto3.client('s3')
# response = s3.list_objects(Bucket='bucket-1-us')
# for odj in response.get('Contents', []):
#     print(odj['Key'])

