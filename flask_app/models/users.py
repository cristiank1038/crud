from flask_app.config.mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        #data = {"id": "1", "first_name":"Elena", "last_name":"De Troya", "email": "elena@cd.com", "created_at":"0000-00-00", "updated_at":"0000-00-00"}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, formulario):
        #formulario = {first_name: "Elena", last_name:"De Troya", email:"elena@cd.com"}
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        #query = "INSERT INTO users (first_name, last_name, email) VALUES ('Elena', 'De Troya', 'elena@cd.com')"
        result = connectToMySQL('crud').query_db(query, formulario)
        return result

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('crud').query_db(query)
        #results = [
        #   {"id": "1", "first_name":"Elena", "last_name":"De Troya", "email":"elena@cd.com", "created_at":"0000-00-00", "updated_at":"0000-00-00"},
        #   {"id": "1", "first_name":"Juana", "last_name":"De Arco", "email":"juana@cd.com", "created_at":"0000-00-00", "updated_at":"0000-00-00"},
        #]
        #hacemos una lista vacia
        users = []
        for u in results:       #recorremos 1-1 lo que tenemos en results
            #u = {"id": "1", "first_name":"Elena", "last_name":"De Troya", "email":"elena@cd.com", "created_at":"0000-00-00", "updated_at":"0000-00-00"}
            instancia_usuario = cls(u) #User(u)
            users.append(instancia_usuario)
        return users

    @classmethod
    def borrar(cls, data):
        #data = {"id": "1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('crud').query_db(query, data)
        return result

    @classmethod
    def editar(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('crud').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('crud').query_db(query, data)
        print(result)
        return cls (result[0])
