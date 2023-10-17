#!/usr/bin/env python3
""" Python function that returns the list of school having a specific topic """

def schools_by_topic(mongo_collection, topic):
    """
    Get a list of schools that have a specific topic.

    :param mongo_collection: PyMongo collection object
    :param topic: Topic to search for (string)
    :return: List of schools
    """
    schools_with_topic = mongo_collection.find({"topics": topic})
    return list(schools_with_topic)
