from scapy.all import *
import requests
import time

FORM_URL = "http://api.cloudstitch.com/vitamintk/magic-form/datasources/sheet"
def posterino(button):
	data = {"Timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "Button": button}
	x=requests.post(FORM_URL, data)
	#print x.text


def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'f0:4f:7c:1c:f4:9d': # Huggies
        print "PUSHED IZZE"
        posterino("IZZE")
      elif pkt[ARP].hwsrc == '74:c2:46:ac:56:c6':
      	print "PUSHED GERBER"
        posterino("GERBER")
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0)