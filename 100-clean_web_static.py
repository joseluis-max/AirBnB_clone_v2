#!/usr/bin/python3
""" Clean files oldest
"""
from fabric.api import run, local, env
env.hosts = ['34.75.115.12', '54.92.203.11']


def do_clean(number=0):
    """ Clean files oldest
    """
    if number == 0 or number == 1:
        number = 2
    else:
        number = int(number) + 1

    local("""ls -t versions | tail +{} |
           sed 's/^/versions\//' | xargs -d '\n' rm -rf"""
          .format(number))
    run("""ls -t /data/web_static/releases | tail +{} |
         sed 's/^/data/web_static/releases\//' | xargs -d '\n' rm -rf"""
        .format(number))
