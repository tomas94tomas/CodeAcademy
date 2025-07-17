from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def index():
    users = User.query.all()
    return render_template("users.html", users=users)

@app.route("/user/<int:user_id>")
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user_detail.html", user=user)

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")
    if name and email:
        db.session.add(User(name=name, email=email))
        db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
    