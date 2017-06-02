from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
	###my custom loging page
        return render_template('youin.html')

@app.route('/login', methods=['POST'])

def do_admin_login():
    if request.form['password'] == 'zzzzz' and request.form['username'] == 'zzzzz':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
   
if __name__ == '__main__':
   app.secret_key = os.urandom(12)
   app.run(debug=True,host='0.0.0.0', port=80)

   
   
##Login
##load things from SQL lite
##Create Check
## 
##create dynamic image loads