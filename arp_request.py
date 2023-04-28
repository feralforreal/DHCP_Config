from scapy.all import *

r1 = "198.51.100.1"
tarmac = "ff:ff:ff:ff:ff:ff"
smac = "f6:24:32:c9:56:b9"
sip = "198.51.100.2"

arpreq = ARP(op=1, pdst=r1, hwdst=tarmac, psrc=sip, hwsrc=smac)
print(arpreq.show())
print("Author : Srivaishnavi")
print("*****ARP Request Packet Creation*******")
send(arpreq)