#!/usr/bin/python
import sys
class naishoforensics:

	def __init__(self, filename):
		self.filename = filename

	def naishomodifyfiledate(self):
        #--------------------------------------------|
        #               Modify File Date             |
        #--------------------------------------------|------------------------------------------------------------------------------------------------

		import datetime
		import os.path

		os.utime(self.filenamefilename, (1038848567, 1038848567))
		print "Forensic Trace of File: " + self.filename
		print "Access: %s" % time.ctime(os.path.getatime(self.filename))
		print "Last Modified: %s" % time.ctime(os.path.getmtime(self.filename))
		print "Created: %s" % time.ctime(os.path.getctime(self.filename))
		os.utime(self.filename, (1038848567, 1038848567))
