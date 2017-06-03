#!/usr/bin/python
# -*- coding:utf-8 -*-

# 在celery_worker.py目录下运行   celery -A celery_worker.celery  worker --loglevel=info
# 运行定时任务 celery beat -A celery_worker.celery
from app import create_app,celery
from celery import platforms

platforms.C_FORCE_ROOT = True
app = create_app('default')
app.app_context().push()
# celery.conf.update(app.config)
