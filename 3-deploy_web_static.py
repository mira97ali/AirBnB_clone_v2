#!/usr/bin/python3
"""Deploy archive!"""

pack_web_static = __import__("1-pack_web_static")
do_deploy_web_static = __import__("2-do_deploy_web_static")


def deploy():
    """Deploy archive"""
    try:
        return do_deploy_web_static.do_deploy(
            pack_web_static.do_pack()
        )
    except Exception as _:
        return False
