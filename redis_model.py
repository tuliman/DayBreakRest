import redis
from datetime import timedelta
import json

r = redis.Redis()


def current():
    keys = r.keys('*')
    current_key = 0
    for key in keys:
        current_key += 1

    return current_key


def get_new_key():
    key = current()
    new_key = key + 1
    return new_key


def add_value(data_file):
    r.hmset(get_new_key(), data_file)


def get_values(key):
    stats = r.hgetall(key)
    return stats


def get_all_keys():
    all_keys = r.keys('*')

    return all_keys


def get_all_value():
    all_value = []
    new_id = 0
    for key in get_all_keys():
        new_id += 1
        all_value.append( get_values(key))
    return all_value

