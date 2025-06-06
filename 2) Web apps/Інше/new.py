# import boto3, pymysql
#
# rds = boto3.client('rds', region_name = 'eu-north-1')
# # response = rds.create_db_instance(
# #     DBInstanceIdentifier='mydbinst',
# #     MasterUsername='masterusername',
# #     MasterUserPassword='masteruserpassword',
# #     DBInstanceClass='db.t3.micro',
# #     Engine='mysql',
# #     AllocatedStorage=20,
# #     DBName = 'mydatabase'
# # )
# # print(response)
# waiter = rds.get_waiter('db_instance_available')
# waiter.wait(DBInstanceIdentifier='mydbinst')
#
# desc = rds.describe_db_instances(DBInstanceIdentifier='mydbinst')
# # print(desc)
#
# endpoint = desc['DBInstances'][0]['Endpoint']['Address']
# port = desc['DBInstances'][0]['Endpoint']['Port']
# print(f"Instance: mydbinst\nEndpoint: {endpoint}\nPort: {port}")
#
# connection = pymysql.connect(
#     host=endpoint,
#     port=port,
#     user='masterusername',
#     password='masteruserpassword',
#     database='mydatabase'
# )
#
# cursor = connection.cursor()
# cursor.execute("SELECT DATABASE();")
# db_name = cursor.fetchone()
# print(db_name)
