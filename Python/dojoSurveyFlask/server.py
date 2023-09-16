from flask import Flask, redirect, render_template, session, request

app = Flask(__name__)

app.secret_key = "surveySafe"


@app.route('/')
def formPage():
    return render_template('formPage.html')


@app.route('/show/user', methods=['POST'])
def showUser():
    session['data'] = request.form
    return redirect('/user')


@app.route('/user')
def user():
    return render_template('user.html', data=session['data'])


@app.route('/leave')
def leave():
    session.clear
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
