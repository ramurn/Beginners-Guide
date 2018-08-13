
sgfsFile="/github/pythonBeginner/Config/sgfsname"
def fslay(l,m):
	print ("fs_name                 ",l)
	print ("fs_server                       \"\"")
	print ("fs_directory            ",m)
	print ("fs_type                  ext4\nfs_mount_opt                    \"\"\nfs_umount_opt                   \"\"\nfs_fsck_opt                     \"\"\nfs_fsck_opt                     \"\"")

with open (sgfsFile,'r') as fd2:
	for line in fd2:
		line=line.strip()
		out=line.split()
		l=out[0]
		m=out[1]
		fslay(l,m)
