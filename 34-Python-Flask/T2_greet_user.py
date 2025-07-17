from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! Add your name to the URL, like /hello/John"

@app.route("/hello/<name>")
def greet(name):
    # Capitalize the name just for fun
    return f"Hello, {name.capitalize()}!"

if __name__ == "__main__":
    app.run(debug=True)