"""
Utility for showing list of IDs added to DB
"""


import os

from dotenv import load_dotenv

from dal.client import client
from dal.operations import items


def main():
    load_dotenv()
    uri = os.getenv("URI")

    try:
        cl = client(uri)
    except Exception as e:
        print(e)
        exit(1)

    metadata = items(cl)
    for doc in metadata:
        print(f"{doc['service_alias']}: {doc['_id']}")


if __name__ == "__main__":
    main()
