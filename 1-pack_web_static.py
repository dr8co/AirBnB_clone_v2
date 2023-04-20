#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from os.path import isdir

from fabric.api import local


def do_pack():
    """generates a tgz archive from the contents of the web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except BaseException:
        return None
