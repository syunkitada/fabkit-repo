# coding: utf-8

from fabkit import task
from fablib.openstack.juno import Keystone

keystone = Keystone()


@task
def setup():
    keystone.setup()
    keystone.dump_openstackrc()

    return {'status': 1}
