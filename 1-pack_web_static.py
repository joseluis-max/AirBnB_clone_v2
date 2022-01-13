#!/usr/bin/python3
""" Generate .tgz
"""
from fabric.api import local
from datetime import date, datetime


def do_pack():
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%S%M")
    status = local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
    if status.failed:
        return None
    else:
        return ("versions/web_static_{}.tgz".format(date))
