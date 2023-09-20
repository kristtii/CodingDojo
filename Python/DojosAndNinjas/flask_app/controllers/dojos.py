from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def redirectHome():
    return redirect("/dojos")


@app.route("/dojos")
def dojos():
    return render_template('dojos.html', dojos=Dojo.get_all_dojos())


@app.route("/dojos/<int:dojo_id>")
def listNinjas(dojo_id):
    ninjas = Ninja.get_all_ninjas_by_dojo_id(dojo_id)
    return render_template('listNinjas.html', ninjas=ninjas)


@app.route("/add/dojo", methods=["POST"])
def addDojo():
    dojoData = request.form
    Dojo.create_dojo(dojoData)
    return redirect("/dojos")
