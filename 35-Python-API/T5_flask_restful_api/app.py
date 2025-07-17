from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Resource
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user.to_dict(), 200
        return {"message": "User not found"}, 404

    def put(self, user_id):
        data = request.json
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        db.session.commit()
        return user.to_dict(), 200

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200

    def post(self):
        data = request.json
        user = User(name=data["name"], email=data["email"])
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 201

api.add_resource(UserListResource, "/users")
api.add_resource(UserResource, "/users/<int:user_id>")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
