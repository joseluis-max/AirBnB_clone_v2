#!/usr/bin/python3
""" Generate .tgz
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Genarate .tgz from web_static with fabric
    """
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%S%M")
    local("mkdir -p versions")
    status = local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
    if status.failed:
        return None
    else:
        return ("versions/web_static_{}.tgz".format(date))
