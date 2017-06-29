## Here I will add all Cisco related network scripts

I am going to develop netmiko and paramiko based tools and integrate it with Flask based web appplication. So I want to manage cisco equipment via web interface.

Installation of paramiko to Centos7 is not very smooth. So I write as note for time-saving in future.

* Installation of paramiko on Centos7:
```
yum install epel-release -y
yum install python-pip   -y
yum install python-devel -y
yum install libffi-devel  -y
yum install -y openssl-devel
yum install gcc -y

pip install --upgrade  pip
pip install paramiko
```

@octocat :+1: This PR looks great - it's ready to merge! :shipit:
