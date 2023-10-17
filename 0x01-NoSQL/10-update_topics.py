#!/usr/bin/env python3
""" Python function that changes all topics of a school document based on the name """

def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on its name.

    :param mongo_collection: PyMongo collection object
    :param name: School name to update
    :param topics: List of topics to update
    """
    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return result

