from flask import Flask

app = Flask(__name__)


@app.route('/')
def sayHello():
    return ('Hello World!')


@app.route('/dojo')
def sayDojo():
    return ('Hello Dojo!')


@app.route('/say/<name>')
def sayName(name):
    return (f'Hello {name.capitalize()}')


if __name__ == '__main__':
    app.run(debug=True)
