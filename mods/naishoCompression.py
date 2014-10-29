#!/usr/bin/python
import sys
from ui.ui import *
class naishocompression:


	def __init__(self, message):
		self.message = message

	#--------------------------------------------|
	#               BZ2 compress                 |
	#--------------------------------------------|------------------------------------------------------------------------------------------------
	def naishobz2com(self):
		try:
			import bz2
			self.message = bz2.compress(self.message)
		except:
			raw_input ("[-] Bz2 commpressing error. Data was not encoded")
        #--------------------------------------------|
        #               zlib compress                 |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def naishozlibcom(self):
                try:
                        import zlib
                        self.message = zlib.compress(self.message, 6)
                except:
                        raw_input ("[-] zlib commpressing error. Data was not encoded")

	#--------------------------------------------|
        #               Show Data                    |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
	def naishoshowdata(self):
		banner1()
		print self.message + "\n\n"
		raw_input("Press Enter to continue...")
