#!/usr/bin/python3
"""File for the deply function"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ["34.74.201.211", "34.138.193.238"]

def do_pack():
    """Is function and store the path of the created archive"""
    try:
        file_name = datetime.now().strftime("%Y%m%d%H%M%S")

        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(file_name)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name

    except:
        return None


def do_deploy(archive_path):
    """Is a Fabric script that distributes an archive to your web servers,
    using the function do_deploy"""

    env.hosts = ["34.74.201.211", "34.138.193.238"]

    if not exists(archive_path):
        return False

    try:
        name_extention = archive_path.split("/")[-1]
        name = name_extention.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(name_extention, path, name))
        run("rm /tmp/{}".format(name_extention))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run('rm -rf {}{}/web_static'.format(path, name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, name))

        return True

    except:
        return False

def deploy():
    """Is a Fabric script (based on the file 2-do_deploy_web_static.py) that
    creates and distributes an archive to your web servers,
    using the function deploy:"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
