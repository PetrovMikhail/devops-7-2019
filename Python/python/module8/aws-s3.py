from typing import List

import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_to_copy = "bucket-id-main"
buckets_from_copy = ["bucket-id123123", "bucket-id1231355", "bucket-id546"]


def copy_files(dest_bucket: str, src_buckets: List) -> None:
    response = client.list_buckets()
    if dest_bucket not in [bucket['Name'] for bucket in response['Buckets']]:
        create_bucket(client, dest_bucket)

    for bucket in src_buckets:
        for key in client.list_objects(Bucket=bucket)['Contents']:
            files = key['Key']
            copy_source = {'Bucket': bucket, 'Key': files}
            s3.meta.client.copy(copy_source, dest_bucket, files)
            print(files)


def create_bucket(client: boto3.client, bucket_name: str):
    client.create_bucket(Bucket=bucket_name)
    print("New bucket {} was created".format(bucket_name))


if __name__ == "__main__":
    copy_files(dest_bucket=bucket_to_copy, src_buckets=buckets_from_copy)
