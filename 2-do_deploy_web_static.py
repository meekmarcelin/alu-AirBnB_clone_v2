#!/usr/bin/python3
""" Fabric script to distribute an archive """
from fabric.api import *
from os.path import exists
env.hosts = ['3.89.247.193', '54.211.187.147']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        folder_name = filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, folder_name))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(folder_name, folder_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(folder_name))
        print("New version deployed!")
        return True
    except:
        return False

