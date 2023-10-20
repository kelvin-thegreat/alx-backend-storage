#!/usr/bin/env python3
'''A module for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


def cache_data(method: Callable) -> Callable:
    '''Decorator to cache fetched data.
    '''
    @wraps(method)
    def wrapper(url: str) -> str:
        '''Wrapper function for caching data and tracking requests.
        '''
        redis_client = redis.Redis()
        redis_client.incr(f'count:{url}')
        cached_result = redis_client.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
        redis_client.set(f'count:{url}', 0)
        redis_client.setex(f'result:{url}', 10, result)
        return result
    return wrapper

@cache_data
def get_page(url: str) -> str:
    '''Return the content of a URL after caching the response and tracking the request.
    '''
    return requests.get(url).text
