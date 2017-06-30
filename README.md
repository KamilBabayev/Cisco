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

- Installation of paramiko on Ubuntu16: </br>
*I use Ubuntu inside of Docker container on above Centos7 host*

```
docker pull ubuntu
docker run --name web -itd -p 8000:80 ubuntu
docker exec -it web bash

apt-get update
apt-get install python3 -y
apt-get install python3-pip -y
apt-get install python3-openssl -y
apt-get install  git vim   -y
pip3  install --upgrade pip
pip3 install paramiko
python3 -c 'import paramiko'

apt-get install  iputils-ping net-tools -y
```
- I will install netmiko and Flask also, I will use Flask for web app, netmiko for connections.
```
pip3 install netmiko
pip3 install flask
```

*webapp directory will contain dynamic and static web application codes.</br>
netapp directory will contain python codes for cisco devices interaction.</br> Web application will use this scripts 
when connection is needed.*

Our environment is ready, now we can start coding! :+1:

