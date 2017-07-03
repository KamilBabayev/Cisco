#!/usr/bin/env python3
import paramiko

ssh_conn = paramiko.SSHClient()
ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_conn.connect('10.50.5.57', 
				username='cisco', 
				password='cisco',
				look_for_keys=False, 
				allow_agent=False)

stdin, stdout, stderr = ssh_conn.exec_command('show version')
for i in stdout.readlines():
    print(i.rstrip())
		
