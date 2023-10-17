#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a MongoDB collection based on keyword arguments.

    :param mongo_collection: PyMongo collection object
    :param kwargs: Keyword arguments representing the document fields
    :return: The new document's _id
    """
    inserted_document = mongo_collection.insert(kwargs)
    return inserted_document

