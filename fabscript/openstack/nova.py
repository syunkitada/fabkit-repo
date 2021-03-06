# coding: utf-8

from fabkit import task, parallel
from fablib.openstack import Nova

nova = Nova()


@task
@parallel
def setup():
    nova.setup()

    return {'status': 1}


@task
def enable_services():
    nova.enable_nova_services()


@task
def sync_flavors():
    nova.sync_flavors()


@task
def restart():
    nova.restart_services()
