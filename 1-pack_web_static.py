#!/usr/bin/python3
""" Generate .tgz
"""
from fabric.api import local
from datetime import date, datetime


def do_pack():
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%S%M")
    # local(f"sudo mkdir version && sudo tar\
    # -cvaz -f ./version/web_static_{date}.tgz ./web_static")
    local(f"tar -cvzf versions/web_static_{date}.tgz web_static")
    return (f"versions/web_static_{date}.tgz")


if __name__ == '__main__':
    do_pack()
