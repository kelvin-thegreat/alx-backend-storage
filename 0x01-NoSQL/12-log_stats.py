#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    """Count total logs"""
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    """Count methods using aggregation"""
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    method_counts = list(nginx_collection.aggregate(pipeline))
    
    print('Methods:')
    for method_doc in method_counts:
        method = method_doc["_id"]
        count = method_doc["count"]
        print(f'\tmethod {method}: {count}')

    """ Count status checks """
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')

