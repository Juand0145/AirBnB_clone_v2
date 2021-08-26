#!/usr/bin/python3
"""File containeing the function do_pack"""

from fabric.api import local
from os.path import isfile
from datetime import datetime


def do_pack():
    """Is a Fabric script that generates a .tgz archive from
    the contents of the web_static folder of your AirBnB Clone
    repo, using the function do_pack."""

    local("mkdir -p versions")

    file_name = datetime.now().strftime("%Y%m%d%M%S")
    file = "versions/web_static_{}.tgz".format(file_name)

    local("tar -cvzf " + file + " web_static")

    if isfile(file):
        return(file)
