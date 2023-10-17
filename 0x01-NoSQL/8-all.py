#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    :param mongo_collection: PyMongo collection object
    :return: List of documents
    """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
