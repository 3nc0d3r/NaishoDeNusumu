#!/usr/bin/python
import sys
from ui.ui import *
class naishoencryption:
	def __init__(self, message):
		self.message = message
	
	def naishorsa(self):
        #--------------------------------------------|
        #               RSA                          |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			from Crypto.PublicKey import RSA
			from Crypto.Cipher import PKCS1_OAEP
			varkey = open('pubkey.pem',"r").read()
			rsakey = RSA.importKey(varkey)
			rsakey = PKCS1_OAEP.new(rsakey)
			encrypted = rsakey.encrypt(self.message)
			del RSA, PKCS1_OAEP
			self.message = encrypted
		except:
			print "\033[31m[-]\033[0mPublic key not found!!!"
                        print "[-] Encryption was not implemented"
			raw_input("Press Enter to continue...")
	def naishoaes(self):
        #--------------------------------------------|
        #               AES                          |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			import getpass
			from Crypto.Cipher import AES
			import base64
			
			BLOCK_SIZE = 32
			PADDING = '{'
			
   			
			pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
		
			EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
			
			banner1()
			rand = raw_input("[1] Create Random key\n[2] Create custom key\n\nNaisho:Encryption:AES> ")
			if rand == str(1):
				import random, string
                                randme = random.SystemRandom()
                                length = 32
                                alpha = string.letters[0:52] + string.digits
                                secret = str().join(randme.choice(alpha) for _ in range(length))
                                print "[+] Random key generated: " + secret + ""
				raw_input("Press Enter to continue...")
			elif rand == str(2):
				secret =  getpass.getpass("Type your Passphrase\n*Note:Secret Passphrase (needs to be 16, 24, or 32 characters long):\n\nNaisho:Encryption:AES> ")
				while ((len(secret) != 16) and (len(secret) != 24) and (len(secret) != 32)):
					secret =  getpass.getpass("\033[31m### Passphrase is not 16, 24, or 32 characters long ### \n\n*Secret Passphrase (needs to be 16, 24, or 32 characters long): \033[0m\n\nNaisho:Encryption:AES> ")
				
			cipher = AES.new(secret)
			
			
			encrypted = EncodeAES(cipher, self.message)
			self.message = encrypted
		except:
			print "Key proided is not the proper size!!"
                        print "[-] Encryption was not implemented"
			raw_input("Press Enter to continue...")
	def naishoblowfish(self):
	#--------------------------------------------|
        #               Blowfish                     |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			from Crypto.Cipher import Blowfish
			import getpass
			banner1()
			#message = open(sys.argv[2]).read()
			rand = raw_input("[1] Create Random key\n[2] Create custom key\n\nNaisho:Encryption:Blowfish> ")
			if rand == str(1):
				import random, string
				randme = random.SystemRandom()
				length = 56
				alpha = string.letters[0:52] + string.digits
				key = str().join(randme.choice(alpha) for _ in range(length))
				print "[+] Random Key Generated: " + key
				raw_input("Press Enter to continue...")
			elif rand == str(2):
				secret =  getpass.getpass("\033[31mSecret Passphrase (needs to be 56 characters long): \033[0m\n\nNaisho:Encryption:Blowfish> ")
                        	while (len(secret) != 56):
                                	secret =  getpass.getpass("\033[31m### Passphrase is not 56 characters long ### \n\n Secret Passphrase (needs to be 56 characters long): \033[0m\n\nNaisho:Encryption:Blowfish> ")
    			
    			c1  = Blowfish.new(key, Blowfish.MODE_ECB)

			input_length = len(self.message)
			packingLength = 8 - input_length % 8
			appendage = chr(packingLength) * packingLength
			packedString = self.message + appendage
			
			encrypted = c1.encrypt(packedString)
			self.message = encrypted
			del Blowfish
    		except:
			print "Key proided is not the proper size!!"
			print "[-] Encryption was not implemented"
			raw_input("Press Enter to continue...")
