# coding: utf-8

import datetime
from fabkit import task
from fablib.openstack import Test

test = Test()


@task
def test_basic():
    test.basic()
    return
    # date = datetime.datetime.today()
    # vm_name = date.strftime('test-%Y%m%d-%H%M')

    # result = nova.cmd("image-list 2>/dev/null | grep '| ' | grep -v '| ID' | awk '{print $4}'")
    # image_list = result.split('\r\n')

    # result = nova.cmd("net-list 2>/dev/null | grep 'test_net' | grep -v '| ID' | awk '{print $2}'")
    # net_list = result.split('\r\n')

    # result = nova.cmd("flavor-list 2>/dev/null | sort -k 6 -n | grep 'RAM_64M-DISC_2G-VCPUS_1' | grep -v '| ID' | awk '{print $4}'")  # noqa
    # flavor_list = result.split('\r\n')

    # boot_cmd = 'boot --image {0} --flavor {1} --nic net-id={2} {3}'.format(
    #     image_list[0], flavor_list[0], net_list[0], vm_name)
    # nova.cmd(boot_cmd)
