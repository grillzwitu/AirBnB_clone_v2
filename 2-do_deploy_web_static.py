#!/usr/bin/python3
"""
Generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
import os.path 
from fabric.api import put, run, env


env.hosts = ['35.231.195.110', '35.243.157.198']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not isfile(archive_path):
        return False
    filename = basename(archive_path)
    try:
        no_ext = filename.split(".")[0]
        put(archive_path, "/tmp/")
        extract_path = "/data/web_static/releases/{}".format(no_ext)
        run("mkdir -p {}".format(extract_path))
        run("tar xzf /tmp/{} -C {}".format(filename, extract_path))
        run("rm /tmp/{}".format(filename))
        run("mv {0}/web_static/* {0}/".format(extract_path))
        run("rm -rf {0}/web_static/".format(extract_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(extract_path))
        return True
    except:
        return False
