#!/usr/bin/python3
""" Fabric script to distribute archive """


from fabric.api import run, env, put
from os.path import exists
env.hosts = ['54.211.187.147', '23.23.62.187']


def do_deploy(archive_path):
    """deploy web static"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        path_name = "/data/web_static/releases/" + name
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(folder_name))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, folder_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(folder_name, folder_name))
        run("rm -rf {}/web_static".format(folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(folder_name))
        return True
    except:
        return False
