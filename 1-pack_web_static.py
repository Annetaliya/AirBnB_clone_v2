#!/usr/bin/python3
''' a Fabric script that generates a .tgz archive
    from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack
'''
from datetime import datetime
from fabric.api import local


def do_pack():
    '''function that generates a tgz archive'''
    now = datetime.now()
    time_stamp = now.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static".format
              (time_stamp))
        return ("versions/web_static_{}".format(time_stamp))
    except Exception as err:
        return None
