
import paramiko

ssh=paramiko.SSHClient()
ssh.connect(lab1,port=22,timeout=2)
cmd="ls -ltr"
stdin, stdout, stderr = ssh.exec_command(cmd)
for line in stdout.readlines():
	print(line)
ssh.close()
