import boto3
from botocore.config import Config

s3 = boto3.client(
    "s3",
    region_name="us-east-1",
    endpoint_url="https://objstorage.leapcell.io",
    aws_access_key_id="59eecfdc5fa5477db4a74f41bb290835",
    aws_secret_access_key="aa6ff7605d20b6525f524481c0804d2956342c609020f234f3ca0853b96abc1b"
)

# List files
response = s3.list_objects_v2(Bucket="testbucket1-akvq-hi4s-72kql5vi")
for obj in response.get("Contents", []):
    print(obj["Key"])

# Upload a file
s3.put_object(
    Bucket="testbucket1-akvq-hi4s-72kql5vi",
    Key="example.txt",
    Body="Hello, this is a sample file content."
)

# Download a file
response = s3.get_object(
    Bucket="testbucket1-akvq-hi4s-72kql5vi",
    Key="example.txt"
)
content = response["Body"].read().decode("utf-8")
print("Downloaded content:", content)

# Delete files
s3.delete_objects(
    Bucket="testbucket1-akvq-hi4s-72kql5vi",
    Delete={
        "Objects": [
            {"Key": "example.txt"},
            {"Key": "another_file.txt"}
        ]
    }
)