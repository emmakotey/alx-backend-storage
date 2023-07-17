#!/usr/bin/env python3
"""
This module's utility function list all document
"""
import pymongo


def list_all(mongo_collection):
    """
    This is to list all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
