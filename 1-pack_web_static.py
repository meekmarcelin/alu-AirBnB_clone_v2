#!/usr/bin/python3
""" do pack and generates an archive """


from fabric.api import local
from datetime import datetime


def do_pack():
    """ generate tgz """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
