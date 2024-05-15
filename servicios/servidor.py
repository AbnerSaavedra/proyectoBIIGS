import sys
#sys.path.append("../bd")
from flask import Flask, render_template, redirect, url_for, request
from bson import ObjectId
from bd import examenes, categorias, indicaciones
from pymongo import MongoClient 


app = Flask(__name__, template_folder="../templates")
app.config['SECRET_KEY'] = "clave secreta"

# Categorías
@app.route("/categoria/list", methods=["GET"])
def getCategoriaList():
    elementsList = categorias.find()

    return render_template('/categorias/lista.html.jinja', elementsList=elementsList)

@app.route('/categoria/add', methods=['GET', 'POST'])
def addCategoria():
    if request.method == "POST":
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        object = {
            'nombre': nombre,
            'descripcion': descripcion
        }
        categorias.insert_one(object)
        return redirect(url_for('getCategoriaList'))
    return render_template("/categorias/add.html.jinja")

@app.route('/categoria/detail/<id>', methods=['GET'])
def getCategoria(id):
    oid = ObjectId(id)
    element = categorias.find_one({'_id': oid})
    return render_template('/categorias/detail.html.jinja', element = element)

@app.route('/categoria/update/<id>', methods=['GET', 'POST'])
def updateCategoria(id):
    oid = ObjectId(id)
    element = categorias.find_one({'_id': oid})
    if request.method == "POST":
        new_element = request.form
        categorias.replace_one({'_id': oid}, 
                                         {'nombre': new_element['nombre'],
                                          'descripcion': new_element['descripcion']})    
        return redirect(url_for('getCategoriaList'))
    return render_template("/categorias/update.html.jinja", element=element)

@app.route('/categoria/delete/<id>', methods=['POST'])
def deleteCategoria(id):
    oid = ObjectId(id)
    categorias.delete_one({'_id': oid})
    return redirect(url_for('getList'))

#Examenes
@app.route("/examen/list", methods=["GET"])
def getExamenList():
    elementsList = examenes.find()

    return render_template('/examenes/lista.html.jinja', elementsList=elementsList)

@app.route('/examen/add', methods=['GET', 'POST'])
def addExamen():
    if request.method == "POST":
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        tipoMuestra = request.form['tipoMuestra']
        precio = request.form['precio']
        indicaciones = request.form['indicaciones']
        object = {
            'nombre': nombre,
            'categoria': categoria,
            'tipo': tipoMuestra,
            'precio': precio,
            'indicaciones': indicaciones
        }
        examenes.insert_one(object)
        return redirect(url_for('getExamenList'))
    listaCategorias = categorias.find()
    return render_template("/examenes/add.html.jinja", listaCategorias = listaCategorias)

@app.route('/examen/detail/<id>', methods=['GET'])
def getExamen(id):
    oid = ObjectId(id)
    element = examenes.find_one({'_id': oid})
    return render_template('/examenes/detail.html.jinja', element = element)

@app.route('/examen/update/<id>', methods=['GET', 'POST'])
def updateExamen(id):
    oid = ObjectId(id)
    element = examenes.find_one({'_id': oid})
    if request.method == "POST":
        new_element = request.form
    
        examenes.replace_one({'_id': oid}, 
                                         {'nombre': new_element['nombre'],
                                          'categoria': new_element['categoria'],
                                          'precio': new_element['precio'],
                                          'tipo': new_element['tipoMuestra'],
                                          'indicaciones': new_element['indicaciones']})    
        return redirect(url_for('getExamenList'))
    listaCategorias = categorias.find()
    return render_template("/examenes/update.html.jinja", element=element, listaCategorias = listaCategorias, id=id)

@app.route('/examen/delete/<id>', methods=['POST'])
def deleteExamen(id):
    oid = ObjectId(id)
    examenes.delete_one({'_id': oid})
    return redirect(url_for('getExamenList'))

if __name__ == "__main__":
    app.run(debug=True)