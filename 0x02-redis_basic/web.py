#!/usr/bin/env python3

"""
This module provides a cache decorator that caches
the result of a function for a certain amount of time
and tracks how many times the function has been called.
"""

import requests
import time
from functools import wraps


def cache(expiration_time: int) -> callable:
    """
    A decorator that caches the result of a function for
    a certain amount of time
    and tracks how many times the function has been called.

    :param expiration_time: The expiration time of the cache in seconds.
    :return: The decorated function.
    """
    def decorator(func: callable) -> callable:
        cache_dict = {}
        count_dict = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]
            if url in cache_dict and time.time() -
            cache_dict[url]["time"] < expiration_time:
                print("Retrieving from cache")
                cache_dict[url]["count"] += 1
                count_dict[f"count:{url}"] += 1
                return cache_dict[url]["content"]
            else:
                print("Retrieving from URL")
                content = requests.get(url).content
                cache_dict[url] = {"content": content, "time": time.time()}
                count_dict[f"count:{url}"] = 1
                return content

        wrapper.cache_dict = cache_dict
        wrapper.count_dict = count_dict
        return wrapper

    return decorator


@cache(10)
def get_page(url: str) -> bytes:
    """
    Retrieves the content of a URL and caches it for a certain amount of time.

    :param url: The URL to retrieve the content from.
    :return: The content of the URL.
    """
    return requests.get(url).content
