"""
Utilities operations
"""


from bson import ObjectId
from dal.client import get_collection


def items(cl):
    """"""
    collection = get_collection(cl)
    return collection.find()


def delete(cl, obj_id):
    """"""
    collection = get_collection(cl)
    return collection.delete_one({"_id": ObjectId(obj_id)})


def upload(cl, metadata):
    """"""
    collection = get_collection(cl)
    return collection.insert_one(metadata)


def download(cl, obj_id):
    """"""
    collection = get_collection(cl)
    items = collection.find({"_id": ObjectId(obj_id)})
    return items[0]
