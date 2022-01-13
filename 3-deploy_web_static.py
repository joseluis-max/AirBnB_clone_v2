#!/usr/bin/python3
""" Make pack and desploy in a function call deploy
"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """ Call do_pack and call do_deploy for deploy web static
    """
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
