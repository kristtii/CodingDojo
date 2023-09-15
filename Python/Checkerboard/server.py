from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('assignedRows.html', x=8, y=8)

@app.route('/<int:number>')
def assignedRows(number):
    return render_template('assignedRows.html', x=number, y=8)

@app.route('/<int:number>/<int:number2>')
def xAndY(number, number2):
    return render_template('assignedRows.html', x=number, y=number2)
    

if __name__ == '__main__':
    app.run(debug=True)
