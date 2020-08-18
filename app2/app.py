import os 
from flask import request , Flask , url_for , redirect , render_template
from config import login_manager,app,db 
from models.user import User 

@app.route('/')
def hello():
	return 'Hello from session'

@app.route('/users/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    user = User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()

@app.route('/login',methods =['GET'])
def login():
	return 'Login ae men'

if __name__ == '__main__':
	app.run(debug=True)