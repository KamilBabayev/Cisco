#!/bin/bash
# Date: August 10 2017
# Desc: This script is for auto install of Cisco automation tool



echo ''

for i in {1..60} ; do  printf '%s' '.' ; sleep .01 ; done
echo ''
echo ''
echo ''


echo '-----------------------------------------------------------------------'
echo ''
echo "Cisco Automation Tool installation"
echo "First assign credentials for web interface and remote cisco connections"
echo ''
echo '-----------------------------------------------------------------------'

echo ''
read -p "Enter web mgmt username: " mgmtuser


while true;
do
        read -p "`echo -e '\nEnter web mgmt password:  '`" -s  mgmtpass1
        echo ''
        read -p "Repeat web mgmt password: " -s mgmtpass2
        echo ''
        if [[ "$mgmtpass1" == "$mgmtpass2" ]];
        then
                echo "Password set correctly !!! "
                break
        else
                echo "Password does not match !!!"
        continue
        fi
done

echo ''
echo "Enter credentials that will be used to connect to CISCO devices"
read -p "Enter username : " ciscouser

while true;
do
    read -p "Enter password: " -s  ciscopass1
    echo ''
    read -p "Repeat password: " -s ciscopass2
    echo ''
    if [[ "$ciscopass1" == "$ciscopass2" ]];
    then
        echo "Password set correctly !!! "
        break
    else
        echo "Password does not match !!!"
        continue
    fi
done

echo ''
echo "Be patient, installation begins..."
sleep 2


echo " ------  Update package index"
apt-get update -y

echo " ------  Installing pip3"
apt-get install python3-pip -y

echo " ------  Installing python3-openssl"
apt-get install python3-openssl -y

echo " ------  Installing git "
apt-get install  git   -y

echo " ------  Cloning git project repo"
mkdir /var/www
cd / ; git clone https://github.com/KamilBabayev/Cisco.git /var/www/html

mkdir /db ;  mv /var/www/html/webapp/users.db /db  ; chown -R www-data:www-data /db/

echo " -----    Creating soft app.py  link"
ln -s /var/www/html/webapp/server.py  /var/www/html/webapp/app.py

echo " ------  Upgrading pip3"
pip3 install --upgrade pip

echo " ------  Installing paramiko"
pip3 install paramiko

echo " ------  Installing netmiko"
pip3 install netmiko

echo " ------  Installing flask"
pip3 install flask

echo " ------  Installing flask alchemy orm etxension"
pip3 install flask_sqlalchemy

echo " ------  Installing flask Form extension"
pip3 install flask_wtf

echo " ------  Installing Nginx Uwsgi"
apt-get install nginx -y
sleep 3
apt-get install uwsgi -y

echo " ------  Installing nginx uwsgi"
apt-get install uwsgi-plugin-python3

rm -rf /etc/nginx/sites-available/default ;rm -rf  /etc/nginx/sites-enabled/default

wget https://raw.githubusercontent.com/KamilBabayev/Cisco/master/nginx_cisco.conf -O  /etc/nginx/sites-available/default

ln -s /etc/nginx/sites-available/default  /etc/nginx/sites-enabled/

wget https://raw.githubusercontent.com/KamilBabayev/Cisco/master/cisco.ini -O /etc/uwsgi/apps-available/cisco.ini

ln -s /etc/uwsgi/apps-available/cisco.ini /etc/uwsgi/apps-enabled/cisco.ini

/etc/init.d/nginx   restart ; /etc/init.d/uwsgi  restart

echo " ------ Installing Sqllite3"
apt-get install sqlite3 -y
sqlite3 /db/users.db "insert into user values(1, '$mgmtuser', '$mgmtpass2');"
sqlite3 /db/users.db "insert into conn_user values(1, '$ciscouser', '$ciscopass2');"

echo ''
echo "*** Installation completed successfully ***"


echo ''
b=$(/sbin/ifconfig | grep -i "inet addr:" | grep -v 127.0.0.1 | awk {'print $2'} | cut -d ':' -f2)
echo ''
echo "You can connnect now:  http://"$b":80/"
echo ''

