#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Author: huxuan
Email: i(at)huxuan.org
Description: Initialization for app.
"""
import Queue
import threading
import time

import redis

from flask import Flask
from flask import g
from flask.ext.babel import Babel
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
babel = Babel(app)
Bootstrap(app)

# tasks = Queue.Queue()
# 
# def tasks_worker():
#     """docstring for tasks_worker"""
#     while True:
#         tasks.get().start()
#         time.sleep(1)
# 
# thread = threading.Thread(target=tasks_worker, args=())
# thread.daemon = True
# thread.start()
thread = threading.Thread()

db = redis.StrictRedis()
db.config_set('maxmemory', '100000000')
db.config_set('maxmemory-policy', 'allkeys-lru')

from app import views
