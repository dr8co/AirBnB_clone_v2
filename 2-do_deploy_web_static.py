#!/usr/bin/python3
"""
A Fabric script that distributes an archive to the web servers,
based on the file 1-pack_web_static.py
"""

from fabric.api import put, run, env
from os.path import isfile

env.hosts = ['18.234.80.163', '100.26.164.167']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if isfile(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, name))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run('rm -rf {}{}/web_static'.format(path, name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, name))
        return True
    except BaseException:
        return False
