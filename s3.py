import boto3

def hello_s3():
	"""
	Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service 
	(Amazon S3) resource and list the buckets in your account.
	This example uses the default settings specified in your shared credentials 
	and config files.
	"""
	s3 = boto3.resource(
		service_name='s3',
		region_name = 'us-west-2',
		aws_access_key_id='AKIAYVVB3KESN3MY2KXZ',
		aws_secret_access_key='2weTgc01012/rgTywqqtPWtfiHpHuzkghS/dVADi'
	)
	my_bucket = s3.Bucket('elasticbeanstalk-us-west-1-596266144036')

	for my_bucket_object in my_bucket.objects.all(): 
		print(my_bucket_object.key)

if __name__ == '__main__':
	hello_s3()
