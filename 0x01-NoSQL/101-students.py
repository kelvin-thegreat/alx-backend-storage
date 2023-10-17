#!/usr/bin/env python3
""" MongoDB Operations using pymongo """


def top_students(mongo_collection):
    """
    Get all students sorted by average score.

    :param mongo_collection: PyMongo collection object
    :return: List of students with average score
    """
    students = list(mongo_collection.find())
    for student in students:
        scores = student["scores"]
        total_score = 0
        count = 0
        for score in scores:
            total_score += score["score"]
            count += 1
        average_score = total_score / count if count > 0 else 0
        student["averageScore"] = average_score

    sorted_students = sorted(students, 
            key=lambda student: student["averageScore"], 
            reverse=True)
    return sorted_students

