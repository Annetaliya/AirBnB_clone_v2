#!/usr/bin/python3
'''that creates and distributes archive to your
    web servers, using function deploy
'''
from fabric.api import run, env, put
import os.path
from datetime import datetime
from fabric.api import local

env.hosts = ['52.87.232.99', '34.204.81.158']
env.path_key = '~/.ssh/school'
env.user_name = 'ubuntu'


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


def do_deploy(archive_path):
    '''Upload the archive to the /tmp/ directory of the web server'''
    if not os.path.isfile(archive_path):
        return False
    file_com = archive_path.split('/')[-1]
    file_ext = file_com.split('.')[0]
    try:
        path_est = "/data/web_static/releases/{}/".format(file_ext)
        create_lnk = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}'.format(path_est))

        run('sudo tar -xvzf /tmp/{} -C {}'.format(file_com, path_est))
        run('sudo rm /tmp/{}'.format(file_com))
        run('sudo mv {}/web_static/* {}'.format(path_est, path_est))
        run('sudo rm -rf {}/web_static'.format(path_est))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf {} {}'.format(path_est, create_lnk))
        return True
    except Exception as err:
        return False


def deploy():
    '''transfer of archive file to web server'''
    f_path = do_pack()
    if f_path is None:
        return False
    return do_deploy(f_path)
