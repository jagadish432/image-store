import os
import hashlib


def get_hash(message):
    return hashlib.md5(message.encode('utf-8')).hexdigest()


def makeURL(url):
    return "http://127.0.0.1:5000/retrieve/" + url
