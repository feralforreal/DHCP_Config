from scapy.all import *

ipaddress = IP(dst='198.51.100.1')
icmp_packet = ICMP()
ping = ipaddress/icmp_packet
print(ping.show())
print(****ICMP_ECHO USING SCAPY***********)
send(ping)
