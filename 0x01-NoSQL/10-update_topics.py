#!/usr/bin/env python3
"""
This script changes a School Topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    This line updates many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
