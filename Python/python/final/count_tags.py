import datetime
import os

import boto3
from bs4 import BeautifulSoup

import requests

url = 'https://yandex.ru'
logging = "123"
s3_bucket_id = None


def count_tag(url: str, logging=None, s3_bucket_id=None):
    time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = {}
    all_tags = [tag.name for tag in soup.find_all()]
    for tag in set(all_tags):
        result.update({tag: all_tags.count(tag)})

    if logging:
        dir_name = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(dir_name, "count_tags.log")
        with open(path, 'w') as write_file:
            write_file.write(f"{time} {url} {len(all_tags)} {result}")

    if s3_bucket_id:
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(path, s3_bucket_id, 'count_tags.log')

    print(f"{time} {url} {len(all_tags)} {result}")


if __name__ == "__main__":
    count_tag(url=url, logging=logging, s3_bucket_id=s3_bucket_id)
