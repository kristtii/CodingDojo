from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=Dojo.get_all_dojos())


@app.route("/add/ninja", methods=["POST"])
def addNinja():
    ninjaData = request.form
    Ninja.create_ninja(ninjaData)
    return redirect("/dojos")
