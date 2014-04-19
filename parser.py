#!/usr/bin/env python
import sys


def check(number):
    if number%2==0:
        print "Even Number"
    else:
        print "Odd Number"

if len(sys.argv) != 2:
	print "Usage: ./parser.py <filename>\n  eg: ./parser.py pcapHEX.txt"
	sys.exit(1)



file = open(sys.argv[1],'r')
reassemble = ""

count = 0 
for line in file:
	if count%2 ==0:
		#a = file.readline()
		a = line.split(' ')
		reassemble = (reassemble + a[8] + a[9]).split('\n')[0]
		print 'a: ' + str(count)
	else:
		# a = file.readline()
		a = line.split(' ')
		reassemble = (reassemble + a[2] + a[3] +a[4] +a[5] + a[6] +a[7]).split('/n')[0]
		print 'b: ' + str(count)
	count = count +1

print reassemble
#print file.readline()
#print file.readline()
file.close
