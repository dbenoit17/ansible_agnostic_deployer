#!/usr/bin/python

import ravello_quick_template as ravello

workstation = ravello.Vm(name="0workstation", tag="workstation", boot_disk_size_GB=40, 
                     ip="192.168.0.5", mac="2c:c2:60:48:bd:62",
                     num_cpus=2, mem_size=6)
workstation.add_service(name='ssh', external=True, port_range=22, protocol='SSH')
workstation.add_service(name='dns-t', external=True, port_range=53, protocol='TCP')
workstation.add_service(name='dns-u', external=True, port_range=53, protocol='UDP')
workstation.add_service(name='oseapi', external=True, port_range="80,8443,8080-8085", protocol='TCP')
workstation.add_hard_drive(name='vol', size=100)

master = ravello.Vm(name="1master", tag="master", boot_disk_size_GB=80, 
                     ip="192.168.0.10", mac="2c:c2:60:7e:d6:b3",
                     num_cpus=4, mem_size=16)
master.add_hard_drive(name='docker_pool', size=10)

node1 = ravello.Vm(name="2node1", tag="node01", boot_disk_size_GB=60, 
                     ip="192.168.0.11", mac="2c:c2:60:43:e9:16",
                     num_cpus=4, mem_size=12)
node1.add_hard_drive(name='docker', size=10)

node2 = ravello.Vm(name="3node2", tag="node02", boot_disk_size_GB=60, 
                     ip="192.168.0.12", mac="2c:c2:60:67:ea:14",
                     num_cpus=4, mem_size=12)
node2.add_hard_drive(name='docker', size=10)

node3 = ravello.Vm(name="4node3", tag="node03", boot_disk_size_GB=60, 
                     ip="192.168.0.13", mac="2c:c2:60:7b:f7:e4",
                     num_cpus=4, mem_size=12)
node3.add_hard_drive(name='docker', size=10)

cloudforms = ravello.Vm(name="5cloudforms", tag="cfme", boot_disk_size_GB=60, 
                     ip="192.168.0.50", mac="2c:c2:60:0c:e9:65", 
                     boot_image='disk-image-cfme-vsphere-5.8.1.5-1.x86_64.qcow',
                     num_cpus=4, mem_size=12)
cloudforms.add_hard_drive(name='vol', size=20)
cloudforms.add_service(name='http', external=True, port_range=80, protocol='TCP')
cloudforms.add_service(name='https', external=True, port_range=443, protocol='TCP')

template = ravello.Template(workstation, master, node1, node2, node3, cloudforms)
print template.to_yaml()
