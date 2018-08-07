import os
import time

curDir = os.getcwd()
print (curDir)
try:
	os.mkdir('newDir')
except OSError:
	print ('OS error. Directory already exists')

os.system('ls -ld *Dir*')
time.sleep(2)
os.rename('newDir','newDir2')
os.system('ls -ld *Dir*')
time.sleep(2)
os.rmdir('newDir2')
os.system('ls -ld *Dir*')
