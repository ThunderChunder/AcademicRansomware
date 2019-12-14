#!/usr/bin/env python
#import os, shlex, subprocess
#import glob

#RANSOM_KEY = "keys/ransom.key"

#def decryptFiles():
#	for item in glob.glob("*.txt.gpg"):
#		file = item
#		output = os.path.splitext(file)[0]
#		args = shlex.split("gpg --output "+output+" -d --batch --passphrase-file "+RANSOM_KEY+" "+file)
#		subprocess.call(args)

#decryptFiles()

#print(os.path.splitext('ransom.key')[0])