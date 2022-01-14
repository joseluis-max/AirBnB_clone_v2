#!/usr/bin/python3
""" Clean files oldest
"""
from fabric.api import run, local, env, cd
env.hosts = ['34.75.115.12', '54.92.203.11']


def do_clean(number=0):
    """
    """
    if number == 0 or number == 1:
        number = 2
    else:
        number = int(number) + 1
    # Trying with cd operations.
    local("cd versions && ls -t . | tail +{} | xargs -d '\n' rm -rf"
          .format(number))

    with cd('/data/web_static/releases'):
        run("ls -t . | tail +{} | xargs -d '\n' rm -rf"
            .format(number))
