#!/usr/bin/python
import sys
from ui.ui import *
class denusumudecryption:
	def __init__(self, message):
		self.message = message
	
	def denusumursa(self):
        #--------------------------------------------|
        #               RSA                          |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			from Crypto.PublicKey import RSA
			from Crypto.Cipher import PKCS1_OAEP
			varkey = open('privkey.pem',"r").read()
			rsakey = RSA.importKey(varkey)
			rsakey = PKCS1_OAEP.new(rsakey)
			decrypted = rsakey.decrypt(self.message)

			del RSA, PKCS1_OAEP
			self.message = decrypted
		except:
			print "\033[31m[-]\033[0mPublic key not found!!!"
                        print "[-] Decryption was not implemented"
			raw_input("Press Enter to continue...")
	def denusumuaes(self):
        #--------------------------------------------|
        #               AES                          |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			import getpass
			from Crypto.Cipher import AES
			import base64
			
			BLOCK_SIZE = 32
			PADDING = '{'
				
   			secret = getpass.getpass("Whats is the secret: ")	
			cipher = AES.new(secret)
			DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
			decrypted = DecodeAES(cipher, self.message)
			self.message = decrypted
			
		except:
			print "Key proided is not the proper size!!"
                        print "[-] Encryption was not implemented"
			raw_input("Press Enter to continue...")
	def denusumublowfish(self):
	#--------------------------------------------|
        #               Blowfish                     |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		try:
			from Crypto.Cipher import Blowfish
			import getpass
			banner1()
    			
			key = raw_input("Whats is the secret: ")
    			c1  = Blowfish.new(key, Blowfish.MODE_ECB)
				
			decrypted = c1.decrypt(self.message)
			self.message = decrypted
			del Blowfish
    		except:
			print "Key proided is not the proper size!!"
			print "[-] Encryption was not implemented"
			raw_input("Press Enter to continue...")
        #--------------------------------------------|
        #               Stepic                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def denusumustepic(self):
		try:
			import stepic
			from PIL import Image
			pictureLoc = raw_input("Type name of file:")
			openPic= Image.open(pictureLoc)
			stepicdecode = stepic.decode(openPic)
			text =  stepicdecode.decode()
			print "\n\033[31mEncrypted Data:\033[0m\n\n" + text
		except:
			print("Decoding Failed!!")
			raw_input("Press Enter to continue...")
			pass
