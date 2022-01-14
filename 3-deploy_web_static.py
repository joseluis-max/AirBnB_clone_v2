#!/usr/bin/python3
""" Make pack and desploy in a function call deploy
"""
from datetime import datetime
from fabric.api import run, local, env, put
env.hosts = ['34.75.115.12', '54.92.203.11']


def do_deploy(archive_path):
    """Deploy a static content in the web server
    """
    if archive_path:
        # Upload the archive to the /tmp/ directory of the web server
        status = put(archive_path, "/tmp")
        if status.succeeded:
            # Uncompress the archive to the folder
            # / data/web_static/releases/<archive filename without extension
            #  > on the web server
            path = archive_path.split("/")
            name_file = path[1].split(".")[0]
            run("mkdir -p /data/web_static/releases/{}/".format(name_file))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                .format(path[1], name_file))
            # Delete the archive from the web server
            run("rm /tmp/{}".format(path[1]))
            run("mv /data/web_static/releases/{}/web_static/*\
                 /data/web_static/releases/{}/"
                .format(name_file, name_file))
            # Delete the symbolic link /data/web_static/current
            # from the web server
            run("rm -rf /data/web_static/releases/{}/web_static"
                .format(name_file))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                .format(name_file))
            print("New version deployed!")
            return True
        else:
            return False
    else:
        return False


def do_pack():
    """ Genarate .tgz from web_static with fabric
    """

    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    status = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(date))
    if status.failed:
        return None
    else:
        return "versions/web_static_{}.tgz".format(date)


def deploy():
    """ Call do_pack and call do_deploy for deploy web static
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    else:
        return do_deploy(archive_path)
