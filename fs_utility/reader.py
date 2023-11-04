"""
Read file from disc
"""


import json


def read(metadata):
    """"""
    with open(metadata, 'r') as f:
        metadata = json.load(f)
    return metadata
