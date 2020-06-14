from flask import Flask
import sys
sys.path.append('d:\\Storee\\Database')
import crud_role
import crud_user


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'Hello, World!'    

@app.route('/role')
def add_role():
    crud_role.create_role("admin", "IT admin of the company Storee System")
    return 'role added'

@app.route('/user')
def add_user():
    crud_user.create_user("Aria Malik Havidiansyah", "aria_malik@hotmail.com", "ariamalikh", "test", 1)
    return 'user added'

@app.route('/test')
def add_user():
    crud_user.create_user("Aria Malik Havidiansyah", "aria_malik@hotmail.com", "ariamalikh", "test", 1)
    return 'user added'

if __name__ == "__main__":
    app.run()