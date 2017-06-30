#!/usr/bin/env python3
from flask import Flask
from flask import request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            return render_template('main.html')
        else:
            return render_template('authfail.html')
	
		
	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
