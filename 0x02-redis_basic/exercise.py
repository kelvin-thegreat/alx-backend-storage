#!/usr/bin/env python3

'''
This module provides functionality for using Redis, a NoSQL data storage system.
'''

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union

def track_calls(method: Callable) -> Callable:
    '''
    Decorator: Tracks the number of calls made to a method within a Cache class.
    '''
    @wraps(method)
    def call_tracker(self, *args, **kwargs) -> Any:
        '''
        Invokes the given method while incrementing its call count.
        '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return call_tracker

def track_call_history(method: Callable) -> Callable:
    '''
    Decorator: Tracks the call history of a method within a Cache class.
    '''
    @wraps(method)
    def history_tracker(self, *args, **kwargs) -> Any:
        '''
        Invokes the method, records its inputs and outputs, and returns the output.
        '''
        input_key = '{}:inputs'.format(method.__qualname__)
        output_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return output
    return history_tracker

def display_call_history(fn: Callable) -> None:
    '''
    Displays the call history of a method within a Cache class.
    '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    method_name = fn.__qualname__
    input_key = '{}:inputs'.format(method_name)
    output_key = '{}:outputs'.format(method_name)
    call_count = 0
    if redis_store.exists(method_name) != 0:
        call_count = int(redis_store.get(method_name))
    print('{} was called {} times:'.format(method_name, call_count))
    input_data = redis_store.lrange(input_key, 0, -1)
    output_data = redis_store.lrange(output_key, 0, -1)
    for input_args, output in zip(input_data, output_data):
        args = eval(input_args)  # Convert the string back to arguments
        print('{}(*{}) -> {}'.format(
            method_name,
            args,
            output,
        ))

class Cache:
    '''
    Represents an object for storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        '''
        Initializes a Cache instance with a connection to Redis and clears its database.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @track_call_history
    @track_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Stores data in a Redis data storage and returns a unique key.
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def retrieve(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''
        Retrieves data from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def retrieve_str(self, key: str) -> str:
        '''
        Retrieves a string value from a Redis data storage.
        '''
        return self.retrieve(key, lambda x: x.decode('utf-8'))

    def retrieve_int(self, key: str) -> int:
        '''
        Retrieves an integer value from a Redis data storage.
        '''
        return self.retrieve(key, lambda x: int(x))

