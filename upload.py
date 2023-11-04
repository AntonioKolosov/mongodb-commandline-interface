"""
Utility for uploading files to DB by Path
python  upload.py --input <path/file>
"""


import argparse
import os

from dotenv import load_dotenv

from dal.client import client
from dal.operations import upload
from fs_utility.reader import read


def parse_args():
    """Add comand line arguments"""
    ag = argparse.ArgumentParser(description="Upload metadata file to DB")
    ag.add_argument("-i",
                    "--input",
                    required=True,
                    help="Full path to the metadata file")
    args = ag.parse_args()
    kwargs = dict((k, v) for k, v in vars(args).items() if k != "message_type")
    return kwargs


def main(**kwargs):
    """"""
    load_dotenv()
    uri = os.getenv("URI")

    metadata = None
    if kwargs.get("input"):
        metadata = read(kwargs.get("input"))
    if metadata:
        try:
            cl = client(uri)
            id = upload(cl, metadata)
        except Exception as e:
            print(e)
            exit(1)
        print(f"Document uploaded with id: {id.inserted_id}")


if __name__ == "__main__":
    kwargs = parse_args()
    main(**kwargs)
