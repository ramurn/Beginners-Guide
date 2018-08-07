import sys, os

########## Variable Declaration ###########
serList="/github/pythonbeginner/Config/awslab.txt"

def argChk():
        if __name__ == "__main__":
                try:
                        arg1 = sys.argv[1]
                except IndexError:
                        print ('ScriptError: Usage: ssh.py arg1 [arg2..]    # Arguments should be SSH remote commands')
                        sys.exit(1)

argChk()
with open(serList,'r') as f:
	for line in f:
		ser=line.split()[0]
		cmd=";".join(sys.argv[1:])
		sshusr="ec2-user"
		sshopt="-q -o ConnectTimeOut=8 -o BatchMode=yes -i /home/ec2-user/mylinux.pem"
		sshcmd="ssh "+sshopt+" "+sshusr+"@"+ser+" -t \""+cmd+"\""
		os.system(sshcmd)
