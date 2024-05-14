import sys
#sys.path.append("../bd")
from flask import Flask, render_template, redirect, url_for, request
from bson import ObjectId
from bd import examenes, categorias, indicaciones
from pymongo import MongoClient 


app = Flask(__name__, template_folder="../templates")
app.config['SECRET_KEY'] = "clave secreta"

@app.route("/categoria/list", methods=["GET"])
def getList():
    elementsList = categorias.find()

    return render_template('/categorias/lista.html.jinja', elementsList=elementsList)

@app.route('/categoria/add', methods=['GET', 'POST'])
def add_element():
    if request.method == "POST":
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        object = {
            'nombre': nombre,
            'descripcion': descripcion
        }
        categorias.insert_one(object)
        return redirect(url_for('getList'))
    return render_template("/categorias/add.html.jinja")

@app.route('/categoria/detail/<id>', methods=['GET'])
def get_element(id):
    oid = ObjectId(id)
    element = categorias.find_one({'_id': oid})
    return render_template('/categorias/detail.html.jinja', element = element)

@app.route('/categoria/update/<id>', methods=['GET', 'POST'])
def update_element(id):
    oid = ObjectId(id)
    element = categorias.find_one({'_id': oid})
    if request.method == "POST":
        new_element = request.form
        categorias.replace_one({'_id': oid}, 
                                         {'nombre': new_element['nombre'],
                                          'descripcion': new_element['descripcion']})    
        return redirect(url_for('getList'))
    return render_template("/categorias/update.html.jinja", element=element)

@app.route('/categoria/delete/<id>', methods=['POST'])
def delete_element(id):
    oid = ObjectId(id)
    categorias.delete_one({'_id': oid})
    return redirect(url_for('getList'))

if __name__ == "__main__":
    app.run(debug=True)