"""
Read file from disc
"""


import json


def write(data, path):
    """"""
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
