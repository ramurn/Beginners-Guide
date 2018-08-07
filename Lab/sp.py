#!/usr/bin/env python 
 
#from subprocess import Popen, PIPE
#process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
#stdout, stderr = process.communicate()
#print stdout

import subprocess
subprocess.call(["cat","test.py"])

s = subprocess.check_output(["echo", "Hello World!"])
print("s = " + s)
