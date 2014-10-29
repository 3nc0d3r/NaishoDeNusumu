#!/usr/bin/python
import sys
from ui.ui import *

class denusumuexport:

	def __init__(self, message):
		self.message = message
		self.split = 0
		self.hostname = ""
		self.httpsplitrequest = message


	def denusumuexport2(self):
        #--------------------------------------------|
        #               Export to a file             |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		encrypted_file = raw_input("Type path of saving text file: ")
		f = open(encrypted_file, 'w')
		f.write(self.message)
		print "\n \033[32m[+]\033[0m File has been written out to " + encrypted_file + "."
		f.close()
		raw_input("Press Enter to continue...")

