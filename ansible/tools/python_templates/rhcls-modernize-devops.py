#!/usr/bin/python

import ravello_quick_template as ravello

bastion = ravello.Vm(name="0workstation", tag="workstation", boot_disk_size_GB=40, 
                     ip="10.0.0.5", mac="2c:c2:60:14:42:50",
                     num_cpus=2, mem_size=6)
bastion.add_service(name='ssh', external=True, port_range=22, protocol='SSH')
bastion.add_service(name='dns-t', external=True, port_range=53, protocol='TCP')
bastion.add_service(name='dns-u', external=True, port_range=53, protocol='UDP')
bastion.add_service(name='oseapi', external=True, port_range='8443,8080', protocol='TCP')
bastion.add_hard_drive(name='vol', size=100)


controller = ravello.Vm(name="1controller", tag="controller", boot_disk_size_GB=100, 
                     ip="10.0.0.10", mac="2c:c2:60:14:42:51",
                     num_cpus=12, mem_size=48)
controller.add_hard_drive(name='images', size="{{ bastion_image_disk_size }}", 
                       image='ScalableInfra - Disk Images')
bastion.add_hard_drive(name='ocp_cinder', size=100)
controller.add_network_device(name="eth1", ip="192.168.100.110", mac="2c:c2:60:14:42:b8")
controller.add_service(name='dash', external=True, port_range=80, 
                       protocol='TCP', ip='10.0.0.10')


cloudforms = ravello.Vm(name="3cfme", tag="cfme", boot_disk_size_GB=40, 
                     ip="10.0.0.8", mac="2c:c2:60:14:42:53",
                     num_cpus=4, mem_size=12)
cloudforms.add_hard_drive(name='vol', size=20)

template = ravello.Template(bastion, controller, cloudforms)
print template.to_yaml()
