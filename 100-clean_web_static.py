#!/usr/bin/python3
"""
deletes out-of-date archives
"""
import os
from fabric.api import *

env.hosts = ["35.231.195.110", "35.243.157.198"]


def do_clean(number=0):
    """
    deletes data from the archives
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    my_archives = sorted(os.listdir("versions"))
    [my_archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in my_archives]

    with cd("/data/web_static/releases"):
        my_archives = run("ls -tr").split()
        my_archives = [a for a in my_archives if "web_static_" in a]
        [my_archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in my_archives]
