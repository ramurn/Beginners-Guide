import os

with open('awslab.txt','r') as f:
	for line in f:
		ser=line.split()[0]
		cmd="sudo hostnamectl set-hostname \""+ser+"-vm\""
		sshusr="ec2-user"
		sshopt="-q -o ConnectTimeOut=8 -o BatchMode=yes -i /home/ec2-user/mylinux.pem"
		sshcmd="ssh "+sshopt+" "+sshusr+"@"+ser+" -t \""+cmd+"\""
		os.system(sshcmd)
