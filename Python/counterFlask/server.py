from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "counter123"

@app.route('/')
def homepage():
    if 'counter' in session:
        return render_template('counter.html', counter=session['counter'])
    session['counter'] = 0
    return render_template('counter.html', counter=session['counter'])

@app.route('/add/count')
def addCount():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('counter', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
