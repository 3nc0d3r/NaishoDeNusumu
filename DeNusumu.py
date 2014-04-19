#!/usr/bin/python	
from mods.denusumuDecryption import *
from mods.denusumuDecoding import *
from ui.ui import *
import os


if __name__ == "__main__":
	banner1()
	if os.geteuid() == 0:
			message = sys.argv[1]
        #--------------------------------------------|
        #               Encoding                     |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
			decode = denusumudecoding(message)
			cho = 0
			while cho != "":
				banner1()
				cho = raw_input("\033[038mWhat type of decoding will you use?\033[0m\n\n[1] HEX\n[2] Base64\n[3] Base32\n[4] Base16\n[5] Ceaser Cipher\n[6] ROT-13\n[0] Show Data\n\nNaisho:Decoding> ")
				if cho == str(1):
					decode.denusumuhex()
				elif cho == str(2):
					decode.denusumubase64()
				elif cho == str(3):
					decode.denusumubase32()
				elif cho == str(4):
					decode.denusumubase16()
				elif cho == str(5):
					decode.denusumuceaser()
				elif cho == str(6):
					decode.denusumurot13()
				elif cho == str(0):
					decode.denusumushowdata()
				else:
					pass

        #--------------------------------------------|
        #               Encryption                   |
        #--------------------------------------------|------------------------------------------------------------------------------------------------
			banner1()
			cho = raw_input("\033[038m\nWhat type of decryption will you use?\033[0m\n\n\033[038m[1] RSA (Excellent - Data will not be recovered)\n[2] BlowFish (Great - keep you key close)\n[3] AES (Great - keep your key close)\n[4] Stenography (Password)\n[5] Stenography (No Password) \033[0m\n\nNaisho:Decryption> ")
			decrypt = denusumudecryption(decode.message)
			if cho == str(1):
				decrypt.denusumursa()
			elif cho == str(2):
				decrypt.denusumublowfish()
			elif cho == str(3):
				decrypt.denusumuaes()
			elif cho == str(4):
				pass	
			elif chos == str(5):
				decrypt.denusumustepic()
			else:
				pass
			print decrypt.message
	else:
		print "Usage: Denusumu.py [text] \n"
