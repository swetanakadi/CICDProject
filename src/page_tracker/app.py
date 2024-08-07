from flask import Flask
from redis import Redis, RedisError
from functools import lru_cache

app = Flask(__name__)


@app.get("/")
def index():
    try:
        page_views = redis().incr("page_views")
    except RedisError as e:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500
    else:
        return f"This page has been seen {page_views} times"


@lru_cache()
def redis():
    return Redis()
