import socket
import sys
import os

def windows(ip):
	HOST = socket.gethostbyname(socket.gethostname())
	#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	#s.bind((HOST, 0))
	#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
	
	#s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 0)
	#s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 0)	

	print "\n\nThis is the IP and port ===> " + ip + " \n"
	gonow = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	count = 0
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
		s.bind((HOST, 0))
		s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
		s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 0)

		data, addr = s.recvfrom(4096)
		print data
		gonow = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
		#gonow = socket.socket(socket.AF_INET, socket.SOCK_RAW)
		#gonow = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, icmp)		

		#try:
		gonow.connect((ip, 0))
		gonow.sendall(data)
			#gonow.sendto(str(pkt),(ip, 1))
			#gonow.sendall('hellow Wo')
		gonow.close()
		#except:
		count = count +1
		s.close()

def maclinux(dest):
	#try:  
	#s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
	s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.getprotobyname('icmp'))
	#s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 0)
	s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 0)

	my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
	#my_socket.socket()
	while 1:
		#data, addr = s.recvfrom(2028)
		data,addr = s.recvfrom(4096)
		#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		my_socket.connect((dest, 0))
		my_socket.sendall(data)
		#data = s.recv(1024)
		#my_socket.close() 
		#print "Packet from %r: %r" % (addr,data)
		print data


if __name__ == "__main__":
	ip = raw_input("IP address to route the traffic: ")
	if os.name == "nt":
		windows(ip)
	else:
		maclinux(ip)