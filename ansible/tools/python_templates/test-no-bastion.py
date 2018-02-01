#!/usr/bin/python

import ravello_quick_template as ravello

controller = ravello.Vm(name="Controller", tag="controller", boot_disk_size_GB=40, 
                     ip="10.0.1.10", mac="2c:c2:60:14:42:52",
                     num_cpus=2, mem_size=2)
controller.add_service(name='ssh', external=True, port_range=22, protocol='SSH')
controller.add_hard_drive(name='vol', size=100)

template = ravello.Template(controller)
print template.to_yaml()
