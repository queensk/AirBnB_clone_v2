#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean:
"""
import os
from fabric.api import env, lcd, cd, run

env.hosts = ["204.236.240.97", "54.237.108.98"]


def do_clean(number=0):
    """
    Delete archive files
    Args:
        number: number of archive files to keep
    keeps the most recent file if number is 0
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for arch_num in range(number)]
    with lcd("versions"):
        [locals("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
