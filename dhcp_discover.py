from scapy.all import *

def dhcp():
    smac = "f6:24:32:c9:56:b9"
    tarmac = "ff:ff:ff:ff:ff:ff"
    sip = "0.0.0.0"
    dip = "255.255.255.255"
    
    dhcp_discover = Ether(src=smac, dst=tarmac)/IP(src=sip, dst=dip)/UDP(sport=68, dport=67)/BOOTP(chaddr=smac)/DHCP(options=[("msg", "discover"), "end"])
    return dhcp

print("Author : Srivaishnavi G")
print("******DHCP Discover creation using Scapy******")
sendp(dhcp(), iface="tap0")