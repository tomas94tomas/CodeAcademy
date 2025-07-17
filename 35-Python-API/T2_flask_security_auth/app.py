import uuid
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///security_demo.db'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'salty'

db = SQLAlchemy(app)

# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
@login_required
def home():
    return "You are logged in!"

if __name__ == '__main__':
    # --- APP INIT CODE (Run once at startup) ---
    with app.app_context():
        db.create_all()
        if not user_datastore.find_user(email="admin@example.com"):
            user_datastore.create_user(
                email='admin@example.com',
                password='password',         # Note: Not hashed, use real hashing in real projects
                fs_uniquifier=str(uuid.uuid4())
            )
            db.session.commit()
        print("Database and default user initialized.")
    app.run()
