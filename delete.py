"""
Utility for deleting files from DB by Id
python delete.py -id <id>
"""


import argparse
import os

from dotenv import load_dotenv

from dal.client import client
from dal.operations import delete


def parse_args():
    """Add comand line arguments"""
    ag = argparse.ArgumentParser(description="Delete metadata file from DB")
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
    if kwargs.get("id"):
        try:
            obj_id = kwargs.get("id")
            cl = client(uri)
            id = delete(cl, obj_id)
        except Exception as e:
            print(e)
            exit(1)
        print(f'Colletcion was cleared: {id.deleted_count}')


if __name__ == "__main__":
    kwargs = parse_args()
    main(**kwargs)
