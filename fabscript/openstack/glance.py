# coding: utf-8

from fabkit import task, parallel
from fablib.openstack import Glance

glance = Glance()


@task
@parallel
def setup():
    glance.setup()

    return {'status': 1}


@task
def register_images():
    glance.register_images()


@task
def restart():
    glance.restart_services()
