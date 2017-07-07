#!/usr/bin/env python3
import subprocess
from flask import Flask
from flask import request, render_template, redirect, url_for
import re

app = Flask(__name__)

@app.route('/ciscoconnect', methods=['GET', 'POST'])
def ciscoconnect1():
    data = request.get_data()
    data = str(data)
    ip_addresses = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
    for ip in ip_addresses:
        print(ip)
    return data

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
@app.route('/ciscoconnect')
def ciscoconnect():
	return 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
