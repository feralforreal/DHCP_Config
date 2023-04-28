#!/usr/bin/env python
from netmiko import ConnectHandler

Router2 = {
'device_type': 'cisco_ios',
'ip': '198.51.100.10',
'username': 'ngdb1',
'password': 'ngdb@1234',
'secret' : 'ngdb@1234'
}
Router3 = {
'device_type': 'cisco_ios',
'ip': '198.51.100.20',
'username': 'ngdb2',
'password': 'ngdb@1234',
'secret' : 'ngdb@1234'
}
Router4 = {
'device_type': 'cisco_ios',
'ip': '198.51.100.30',
'username': 'ngdb3',
'password': 'ngdb@1234',
'secret' : 'ngdb@1234'
}

#passing the config_commands

cmd = [
    'no ip routing',
    'int Fa1/0',
    'ip address dhcp',
    'no shut',
    'exit'
    ]

#listing the router ssh details to variable all
all = [Router2, Router3, Router4]
print ("Author : Srivaishnavi G")
print ("Date : 2/5/2023")
print ("****************DHCP Configuration Script using Netmiko*******")
for devices in all:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(cmd)
    print (output)


