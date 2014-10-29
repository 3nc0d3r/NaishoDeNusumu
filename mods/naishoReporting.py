#!/usr/bin/python
import sys
from ui.ui import *
class naishoreporting:


	def __init__(self, message, reporting):
		self.message = message
		self.reporting = reporting
        #--------------------------------------------|
        #               Base64                       |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
        def naishoexporthtml(self):
		filename = raw_input("Name of File for export(eq. Internal_systems):")
		file = open(filename, 'w')
		file.write("""
<!DOCTYPE html>
<html>
<head>
<style>
table,th,td
{
border:1px solid black;
border-collapse:collapse;
}
th,td
{
padding:5px;
}
</style>
</head>
<body>
<center>
<pre>
,   .     o     |         ,--.      ,   .                         
|\  |,---..,---.|---.,---.|   |,---.|\  |.   .,---..   .,-.-..   .
| \ |,---||`---.|   ||   ||   ||---'| \ ||   |`---.|   || | ||   |
`  `'`---^``---'`   '`---'`--' `---'`  `'`---'`---'`---'` ' '`---'
</pre>
Stealing Secretly <br>
[Copyright (C) 2014, Adam Crompton (@3nc0d3r)]<p>



<table style="width:400px">
<tr bgcolor="#C6C6BE">
  <th>Source IP Address</th>
  <th>Destination IP Address</th>		
  <th>Protocol</th>
  <th>Port</th>
  <th>Outcome</th>
</tr>
""")
		
		count =0
		while count < len(self.reporting):
			count2= 0
			file.write("<tr>")
			while count2 < len(self.reporting[count]):
				if count2 == 4 and self.reporting[count][count2]=="Success":
					file.write("<td bgcolor='#33CC33'>"+ self.reporting[count][count2]+"</td>")
				elif count2 == 4 and self.reporting[count][count2]=="Failed":
					file.write("<td bgcolor='#FF3300'>"+ self.reporting[count][count2]+"</td>")
				else:
					file.write("<td>"+ self.reporting[count][count2]+"</td>")
					print count2, self.reporting[count][count2]
				count2 = count2 +1
			file.write("</tr>")
			count = count + 1

		file.write("""</table>
Special Thanks to Mick Douglas and John Strand.
</center>
</body>
</html>
""")
		file.close()
		raw_input("Press Enter to continue...")
