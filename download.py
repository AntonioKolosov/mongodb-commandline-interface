"""
Utility ffor downloading files from DB by ID and Path
python download.py -o <path/file> -id <id>
"""


import argparse
import os

from dotenv import load_dotenv

from dal.client import client
from dal.operations import download
from fs_utility.writer import write


def parse_args():
    """Add comand line arguments"""
    ag = argparse.ArgumentParser(description="Upload metadata file to DB")
    ag.add_argument("-o",
                    "--output",
                    required=True,
                    help="Full path to the metadata file")
    ag.add_argument("-id",
                    required=True,
                    help="File id")
    args = ag.parse_args()
    kwargs = dict((k, v) for k, v in vars(args).items() if k != "message_type")
    return kwargs


def main(**kwargs):
    """"""
    load_dotenv()
    uri = os.getenv("URI")

    if kwargs.get("output") and kwargs.get("id"):
        try:
            obj_id = kwargs.get("id")
            cl = client(uri)
            metadata = download(cl, obj_id)
        except Exception as e:
            print(e)
            exit(1)
        del metadata['_id']
        ffn = kwargs.get("output")
        write(metadata, ffn)
        print(f"File with {ffn} succsesfully wrote")


if __name__ == "__main__":
    kwargs = parse_args()
    main(**kwargs)
