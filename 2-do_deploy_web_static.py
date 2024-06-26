#!/usr/bin/python3
"""Deploy archive!"""
import os

import fabric.api


fabric.api.env.hosts = ["100.26.254.240", "52.23.222.226"]


def do_deploy(archive_path):
    """Deploy archive"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])
        fabric.api.put(archive_path, "/tmp/")
        fabric.api.run("sudo mkdir -p {}".format(new_folder))
        fabric.api.run(
            "sudo tar -xzf /tmp/{} -C {}".format(new_comp, new_folder)
        )
        fabric.api.run("sudo rm /tmp/{}".format(new_comp))
        fabric.api.run(
            "sudo mv {}/web_static/* {}/".format(new_folder, new_folder)
        )
        fabric.api.run("sudo rm -rf {}/web_static".format(new_folder))
        fabric.api.run("sudo rm -rf /data/web_static/current")
        fabric.api.run(
            "sudo ln -s {} /data/web_static/current".format(new_folder)
        )
        return True
    except Exception as _:
        return False
