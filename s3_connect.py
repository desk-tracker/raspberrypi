import boto3
from dotenv import load_dotenv
import os

load_dotenv()
def s3_connection():
	try:
		# connect s3 client
		s3 = boto3.client(
			service_name="s3",
			region_name="ap-northeast-2",
			aws_access_key_id=os.environ['aws_access_key'],
			aws_secret_access_key=os.environ['aws_secret_access_key']
		)
	except Exception as e:
		print(e)
	else:
		print("s3 bucket connected")
		return s3