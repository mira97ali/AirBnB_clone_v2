#!/usr/bin/python3
"""Compress before sending"""
import time

import fabric


def do_pack():
    """Pack web static"""
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        fabric.api.local("mkdir -p versions")
        fabric.api.local(
            "tar -cvzf versions/web_static_{}.tgz web_static/".format(timestr)
        )
        return ("versions/web_static_{}.tgz".format(timestr))
    except Exception as _:
        return None
