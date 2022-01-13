#!/usr/bin/python3
# distributes an archive to your web servers, using the function do_deploy
""" Deploy a static content
"""
from fabric.api import put, run, env
env.host['34.75.115.12', "54.92.203.11"]


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
            path = archive_path.split("/")[1]
            name_file = path.split(".")[0]
            run("mkdir -p /data/web_static/releases/{}/".format(path))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                .format(archive_path, path))
            # Delete the archive from the web server
            run("rm /tmp/{}".format(archive_path))
            run("mv /data/web_static/releases/{}/web_static/*\
                 /data/web_static/releases/{}/"
                .format(path, path))
            # Delete the symbolic link /data/web_static/current
            # from the web server
            run("rm -rf /data/web_static/releases/{}/web_static"
                .format(path))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                .format(path))

            return True
        else:
            return False
    else:
        return False
