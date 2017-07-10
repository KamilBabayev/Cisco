#!/usr/bin/env python3
import paramiko
from sys import argv
host = argv[1]
command = argv[2]


ssh_conn = paramiko.SSHClient()
ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_conn.connect(host, 
				username='cisco', 
				password='cisco',
				look_for_keys=False, 
				allow_agent=False)

stdin, stdout, stderr = ssh_conn.exec_command(command)
for i in stdout.readlines():
    print(i.rstrip())

	
