from flask import render_template, request, redirect
from flask_app import app

#Importando el Modelo de User               
from flask_app.models.users import User



@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html", users=users)


@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/create', methods=['POST'])         #este es para el new.html es decir obtengo esos datos de ese formulario
def create():
    #request.form = {first_name: "Elena", last_name:"De Troya", email:"elena@cd.com"}
    User.guardar(request.form)
    return redirect('/')                        # conesto se va a mi pagina principal

@app.route('/delete/<int:id>')
def delete(id): #/delete/1
    #id = 1
    data = {
        "id": id
    }

    User.borrar(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edite(id):
    data = {
        "id":id
    }
    return render_template('edit.html', user=User.get_one(data))

@app.route('/update', methods=['POST'])
def update():
    

    users = User.editar(request.form)
    return redirect('/')


# elena@codingdojo.com