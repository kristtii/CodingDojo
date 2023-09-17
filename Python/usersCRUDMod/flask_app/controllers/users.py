from flask_app import app, render_template, request, redirect
from flask_app.models.user import User


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
    return redirect('/show/users')


@app.route('/edit/user/<int:user_id>')
def editUser(user_id):
    user = User.get_user_by_id(user_id)
    return render_template('edit.html', user=user[0])


@app.route('/update/user/<int:user_id>', methods=['POST'])
def updateUser(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/show/users')


@app.route('/delete/user/<int:user_id>')
def deleteUser(user_id):
    User.delete_user(user_id)
    return redirect('/show/users')


@app.route('/show/users')
def showUsers():
    return render_template('read.html', users=User.get_all())
