from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    db = 'users_schema'

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': user_id}
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_user(cls, user_id):
        query = "DELETE FROM users WHERE id=%(id)s;"
        data = {'id': user_id}
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
