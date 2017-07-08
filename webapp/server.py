#!/usr/bin/env python3
import subprocess, os
from flask import Flask
from flask import request, render_template, redirect, url_for
import re
import paramiko

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
       return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
             return redirect(url_for('main'))
        else:
            return render_template('authfail.html')

@app.route('/main')
def main():
	return render_template('main.html')
@app.route('/addnewdevice')
def addnewdevice():
    return render_template('addnewdevice.html')
@app.route('/addnewcommand')
def addnewcommand():
    return render_template('addnewcommand.html')

@app.route('/ciscoconnect', methods=['GET', 'POST'])
def ciscoconnect1():
    data = request.get_data()
    data = str(data)
    #ip_addresses = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
    data = data.strip('b').split('&')
    devices_and_commands = []
    for i in data:
         devices_and_commands.append(i.split('=')[1])
    result = devices_and_commands
    command= devices_and_commands[len(devices_and_commands)-1]
    print(devices_and_commands, "", "Command: ", command)
    p = subprocess.Popen(['/Cisco/netapp/connector.py', '10.50.5.57'], stdout=subprocess.PIPE )
    out, err = p.communicate()
    out = str(out)
    for i in out.split('\\n'):
        print(i)
    
    return render_template("cisco_output.html", output=out)
	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
