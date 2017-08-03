#!/bin/bash

echo "Installing pip3"
apt-get install python3-pip -y

echo "Installing python3-openssl"
apt-get install python3-openssl -y

echo "Installing git "
apt-get install  git   -y

echo "Upgrading pip3"
pip3 install --upgrade pip

echo "Installing paramiko"
pip3 install paramiko

echo "Installing netmiko"
pip3 install netmiko

echo "Installing flask"
pip3 install flask

echo "Cloning git project repo"
git clone https://github.com/KamilBabayev/Cisco.git

echo "Installing flask alchemy orm etxension"
pip3 install flask_sqlalchemy

echo "Installing flask Form extension"
pip3 install flask_wtf

