#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import redis
import requests

r = redis.Redis()


def get_page(url: str) -> str:
    """ Track how many times a particular URL was accessed in the key
        "count:{url}" and cache thei expiration time of 10 seconds """
    count_key = f"count:{url}"
    cached_key = f"cached:{url}"

    # Increment the count
    r.incr(count_key)
    count = r.get(count_key)

    # Cache the result with an expiration time of 10 seconds
    if r.exists(cached_key):
        return r.get(cached_key).decode("utf-8")

    resp = requests.get(url)
    r.setex(cached_key, 10, resp.text)

    return resp.text


if __name__ == "__main__":
    # Call get_page with the URLs to cache them
    get_page('http://google.com')
    get_page('http://slowwly.robertomurray.co.uk')
