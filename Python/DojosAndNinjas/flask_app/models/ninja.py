from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.age = data.get('age')
        self.dojo_id = data.get('dojo_id')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    db = 'dojos_and_ninjas_schema'

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_all_ninjas_by_dojo_id(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"
        results = connectToMySQL(cls.db).query_db(query, {"dojo_id": dojo_id})
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
