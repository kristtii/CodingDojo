from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

app.secret_key = "surveySafe"


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/add/user', methods=['POST'])
def addUser():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/')


@app.route('/show/users')
def showUsers():
    print(User.get_all())
    return render_template('read.html', users=User.get_all())


if __name__ == "__main__":
    app.run(debug=True)
