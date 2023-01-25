#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Pack files tgz to archive
    """
    try:
        date = datetime.now().strftime("%Y%M%D%H%M%S")
        if isdir("versions") is False:
            lacal("mkdir versions")
        file_name = "versions/web_static_{}".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except BaseException:
        return None
