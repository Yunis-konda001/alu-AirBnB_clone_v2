#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    The archive is stored in the versions directory and is named based on
    the current timestamp.

    Returns:
        str: The path to the created archive on success.
        None: If the archive creation fails.
    """

    try:
        time_str = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(time_str)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except:
        return None