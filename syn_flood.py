from scapy.all import *

sip = "198.51.100.2"
dip = "198.51.100.1"
sport = 12345
tarport = 80

syn = IP(src=sip, dst=dip) / TCP(sport=sport, dport = tarport, flags="S")
print(syn.show())
print ("Author: Srivaishnavi")
print("***SYN Packet Creation using Scapy******")
send(syn, count=10, verbose=0)