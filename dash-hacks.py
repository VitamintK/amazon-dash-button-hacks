from scapy.all import *

LABELS = {'f0:4f:7c:1c:f4:9d': "IZZE", '74:c2:46:ac:56:c6': "GERBER"}

def arp_display(fn):
  def arp_display_aux(pkt):
	  if pkt[ARP].op == 1: #who-has (request)
	    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
	      hwsrc = pkt[ARP].hwsrc
	      if hwsrc in LABELS:
	      	print(LABELS[hwsrc])
	      	fn(LABELS[hwsrc])
	      else:
	        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
  return arp_display_aux

def listen(fn):
	print sniff(prn=arp_display(fn), filter="arp", store=0, count=0)