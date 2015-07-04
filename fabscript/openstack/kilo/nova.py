# coding: utf-8

from fabkit import task
from fablib.openstack.kilo import Nova

nova = Nova()


@task
def setup():
    nova.setup()

    return {'status': 1}


@task
def restart():
    nova.restart_services()


@task
def enable_services():
    nova.enable_nova_services()


@task
def sync_flavors():
    nova.sync_flavors()
