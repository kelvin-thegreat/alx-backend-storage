#!/usr/bin/env python3
""" MongoDB Operations using pymongo """

#!/usr/bin/env python3
"""
MongoDB Operations with Python using pymongo
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    :param mongo_collection: PyMongo collection object
    :return: List of students with average score
    """
    top = list(mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]))

    return top
