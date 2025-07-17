from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# We'll use a simple dictionary to store submitted data for this session (not persistent!)
submitted_data = {}

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        submitted_data["name"] = name
        submitted_data["email"] = email
        return redirect(url_for("submitted"))
    return render_template("form.html")

@app.route("/submitted")
def submitted():
    # If user tries to access /submitted without submitting, redirect to form
    if "name" not in submitted_data or "email" not in submitted_data:
        return redirect(url_for("form"))
    return render_template("submitted.html", data=submitted_data)

if __name__ == "__main__":
    app.run(debug=True)
