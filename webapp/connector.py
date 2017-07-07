#!/usr/bin/env python3
import paramiko
import sys
device = sys.argv[1]

def cisco_conn(device):
	ssh_conn = paramiko.SSHClient()
	ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_conn.connect(device, 
					username='cisco', 
					password='cisco',
					look_for_keys=False, 
					allow_agent=False)
	stdin, stdout, stderr = ssh_conn.exec_command('show arp')
	for i in stdout.readlines():
		print(i.rstrip())

		
cisco_conn(device)
