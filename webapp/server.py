#!/usr/bin/env python3
from subprocess import PIPE, Popen
from flask  import Flask
from flask  import request,render_template, redirect, url_for, session
from models import db, User, Command, Device
from forms  import LoginForm
import paramiko
#import re
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'development'
db.init_app(app)
#db = SQLAlchemy(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form) 
    if request.method == 'POST':
        adminuser = User.query.filter_by(username='admin').first()
        #username = request.form['username']
        #password = request.form['password']
        username = form.username.data
        password = form.password.data
        failmsg = "Username or Password is not correct"
        print(form.validate(), request.form['username'], request.form['password'])
        if form.validate() == False:
            return render_template('index.html', form = form)
        else:  
            if username == adminuser.username and password == adminuser.password:
                session['username'] = form.username.data
                return redirect(url_for('main'))
            else:
                #return "username pasword is incorrect"
                return render_template('index.html', form = form, failmsg=failmsg)
    elif request.method == 'GET':
        return render_template('index.html', form = form)
        

@app.route('/')
def index():
	return redirect(url_for("login"))

@app.route('/login2', methods=['POST', 'GET'])
def login2():
    if request.method == 'GET':
       return redirect('/')
    if request.method == 'POST':
        adminuser = User.query.filter_by(username='admin').first()
        username = request.form['username']
        password = request.form['password']
        #if username == 'admin' and password == 'admin123':
        if username == adminuser.username and password == adminuser.password:
             return redirect(url_for('main'))
        else:
            #`return render_template('authfail.html')
            return render_template('index.html', failmsg="Username or Password is incorrect")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/main')
def main():
    if 'username' not in session:
        return redirect(url_for('login'))

    def chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i+n]

    desc=[]
    name=[]
    command = []
    global commands
    desc, name, command, commands = [], [], [], []
    commands_query = Command.query.all()
    for i in commands_query: 
        command.append(i.command)
    for i in commands_query: 
        name.append(i.name)
    for i in commands_query: 
        desc.append(i.desc)
    w =[j for i in zip(command,name,desc) for j in i]
    for i in list(chunks(w, 3)): 
        commands.append(i)

    global devices
    name,desc,ip,devices = [],[],[],[]
    dev_query = Device.query.all()
    for i in dev_query: 
        ip.append(i.ip)
    for i in dev_query: 
        name.append(i.name)
    for i in dev_query: 
        desc.append(i.desc)
    x =[j for i in zip(ip,name,desc) for j in i]
    for i in list(chunks(x, 3)): 
        devices.append(i)
    
    return render_template('main.html', commands = commands, devices=devices)

@app.route('/editdevice', methods=['GET', 'POST'])
def editdevice():
    if 'username' not in session:
        return redirect(url_for('login'))

    data = request.get_data()
    data = str(data)
    print(data)
    if request.method == 'POST':
        data = data.strip('b').strip("'").split("=")[1]
        data = data.split('&')
        #data = data.split('&')[0]
        global ipaddr
        ipaddr, button = data[0], data[1]
        print(ipaddr, button)
        """
        devip = Device.query.filter_by(ip=ipaddr).first()
        db.session.delete(devip)
        db.session.commit()
        """
        if button == "delete":
            devip = Device.query.filter_by(ip=ipaddr).first()
            db.session.delete(devip)
            db.session.commit()
            return render_template('editdevice.html', success_msg="Deviced deleted successfully")
        elif button == "edit":
            device = Device.query.filter_by(ip=ipaddr).first()
            #db.session.delete(devip)
            #db.session.commit()
            print('EDIT', device.ip)
            return render_template('updatedevice.html', header="Update New Device", 
                                    submitvalue="Update Device", ip=device.ip, name = device.name, desc = device.desc)
            #return render_template('addnewdevice.html')
        #return render_template('editdevice.html', success_msg="Deviced deleted successfully")
    #data = data.strip('b').strip("'").split('=')[1]
    #print(data)
    return render_template('editdevice.html', devices=devices)

@app.route('/updatedevice', methods=['GET', 'POST'])
def updatedevice():
    if 'username' not in session:
        return redirect(url_for('login'))
    data = request.get_data()
    data = str(data)
    data = data.strip('b').split('&')
    x,y = [],[]
    if request.method == 'POST':
        for i in data:
            #print(i.split('=')[1].rstrip("'").replace("+", " "))
            x.append(i.split('=')[1].rstrip("'").replace("+", " "))
        ip, name, desc = x[0],x[1], x[2]
        print(ip, name, desc, "UPDATEEEEEEEEEEE")
        curdata = Device.query.filter_by(ip=ipaddr).first()
        curdata.ip = ip
        curdata.name = name
        curdata.desc = desc
        db.session.commit()
    return redirect(url_for('main'))

@app.route('/editcommand', methods=['GET', 'POST'])
def editcommand():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template('editcommand.html', commands=commands)

@app.route('/addnewdevice', methods=['GET', 'POST'])
def addnewdevice():
    if 'username' not in session:
        return redirect(url_for('login'))

    data = request.get_data()
    data = str(data)
    data = data.strip('b').split('&')
    x,y = [],[]
    if request.method == 'POST':
        for i in data:
            #print(i.split('=')[1].rstrip("'").replace("+", " "))
            x.append(i.split('=')[1].rstrip("'").replace("+", " "))
        ip, name, desc = x[0],x[1], x[2]
        print(ip, name, desc)
        newdevice = Device(ip, name, desc)
        try:
            db.session.add(newdevice)
            db.session.commit()
            return render_template('addnewdevice.html', success_msg="Device added successfully")
        except:
            return render_template('addnewdevice.html', fail_msg="Error occured. Can not add device")
    return render_template('addnewdevice.html', header="Add New Device", submitvalue="Add Device")

@app.route('/addnewcommand', methods=['GET', 'POST'])
def addnewcommand():
    if 'username' not in session:
        return redirect(url_for('login'))

    data = request.get_data()
    data = str(data)
    data = data.strip('b').split('&')
    x,y = [],[]
    if request.method == 'POST':
        for i in data:
            #print(i.split('=')[1].rstrip("'").replace("+", " "))
            x.append(i.split('=')[1].rstrip("'").replace("+", " "))
        command, name, desc = x[0],x[1], x[2]
        print(command, name, desc)
        newcommand = Command(command, name, desc)
        print(newcommand, command,name,desc, "demello")
        try:
            db.session.add(newcommand)
            db.session.commit()
            return render_template('addnewcommand.html', success_msg="Command added successfully")
        except:
            return render_template('addnewcommand.html', fail_msg="Error occured.Can not add new command")
    return render_template('addnewcommand.html')



@app.route('/ciscoconnect', methods=['GET', 'POST'])
def ciscoconnect1():
    if 'username' not in session:
        return redirect(url_for('login'))

    data = request.get_data()
    print(data)
    data = str(data)
    index = data.index("customcommand")
    if len(data[index:]) < 16:
         data = data[0:-len(data[index:])-1]
    print(data, type(data))
    #ip_addresses = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
    data = data.strip('b').split('&')
    devices_and_commands = []
    for i in data:
         devices_and_commands.append(i.split('=')[1])
    result = devices_and_commands
    print(result)
    devices= devices_and_commands[:len(devices_and_commands)-1]
    print(devices)
    devices = str(devices)
    #devices = devices.strip(']').lstrip('[').strip("'")
    print(devices)
    print('###################################################################')
    command= devices_and_commands[len(devices_and_commands)-1]
    command = command.rstrip("'").replace('+', ' ')
    print(devices_and_commands, "", "Command: ", command, "Devices: ", devices)
    #p = subprocess.Popen(['/Cisco/netapp/connector.py', devices, command], stdout=subprocess.PIPE )
    command = command.replace("%7C","|").replace("%2F", "/")
    print(devices, "------")
    print(command, "------")
    p = Popen(['/Cisco/netapp/connector.py', devices, command], stdout=PIPE )
    out, err = p.communicate()
    out = str(out)
    out = out.lstrip('b').strip()
    print(out)
    data = []
    for i in out.split('\\n'):
        i = i.replace(' ', "&nbsp;")
        data.append(i)

    print('----------------------------------')
    for i in out.split('\\n'):
        print(i)
 
    return render_template("cisco_output.html", output=data)

	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


