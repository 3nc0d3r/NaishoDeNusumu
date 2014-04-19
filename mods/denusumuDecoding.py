import sys
from ui.ui import *
class denusumudecoding:


	def __init__(self, message):
		self.message = message

        #--------------------------------------------|
        #               Base64                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def denusumubase64(self):
		
		import base64
		try:
			#self.message = self.message.decode('base64')
			self.message = base64.b64decode(self.message)
		except:
			print "[-] Base64 encoding error"
			sys.exit(1)

        #--------------------------------------------|
        #               HEX                          |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def denusumuhex(self):
	
		import binascii
		try:
			self.message = binascii.unhexlify(self.message)
		except:
			print "[-] Hex encoding error"
			sys.exit(1)
			 
        #--------------------------------------------|
        #               Ceaser Cipher                |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def denusumuceaser(self):
		k = int(raw_input("How Many Space do you want to move over: "))
		encoding = ''
		for each in self.message:
			c = (ord(each)+k) % 126
			encoding += chr(c)
		self.message = encoding

        #--------------------------------------------|
        #               ROT_13                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def denusumurot13(self):
		import codecs
		try:
			self.message = self.message.decode('rot_13')
		except:
			print "ROT-13 Error"
			pass
        #--------------------------------------------|
        #               Base32                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def denusumubase32(self):
		
		try:
			import base64
			self.message = base64.b32decode(self.message)
		except:
			print "[-] Base32 encding error"

        #--------------------------------------------|
        #               Base16                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def denusumubase16(self):

                try:
                        import base64
                        self.message = base64.b16decode(self.message)
                except:
                        print "[-] Base16 encding error"
	#--------------------------------------------|
        #               Show Data                    |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def denusumushowdata(self):
		banner1()
		print self.message + "\n\n"
		raw_input("Press Enter to continue...")

