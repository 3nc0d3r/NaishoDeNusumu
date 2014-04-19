#!/usr/bin/python
import sys
from ui.ui import *
class naishoencoding:


	def __init__(self, message):
		self.message = message

        #--------------------------------------------|
        #               Base64                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def naishobase64(self):
		
		import base64
		try:
			self.message = base64.b64encode(self.message)
		except:
			print "[-] Base64 encoding error"
			raw_input("Base64 error: Data was not encoded")

        #--------------------------------------------|
        #               HEX                          |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def naishohex(self):
	
		import binascii
		try:
			self.message = binascii.hexlify(self.message)
		except:
			print "[-] Hex encoding error"
			raw_input("HEX error: Data was not encoded")
			 
        #--------------------------------------------|
        #               Ceaser Cipher                |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def naishoceaser(self):
		k = int(raw_input("How Many Space do you want to move over: "))
		encoding = ''
		for each in self.message:
			c = (ord(each)+k) % 126
			encoding += chr(c)
		self.message = encoding

        #--------------------------------------------|
        #               ROT_13                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def naishorot13(self):
		import codecs
		try:
			self.message = self.message.encode('rot_13')
		except:
			raw_input("[-] ROT-13 cannot encode, try to encode with something else before using ROT-13")
        #--------------------------------------------|
        #               Base32                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def naishobase32(self):
		
		try:
			import base64
			self.message = base64.b32encode(self.message)
		except:
			raw_input ("[-] Base32 encoding error. Data was not encoded")

        #--------------------------------------------|
        #               Base16                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def naishobase16(self):

                try:
                        import base64
                        self.message = base64.b16encode(self.message)
                except:
                        print ("[-] Base16 encoding error. Data was not encoded")
	#--------------------------------------------|
        #               Show Data                    |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def naishoshowdata(self):
		banner1()
		print self.message + "\n\n"
		raw_input("Press Enter to continue...")
