from flask import Flask, render_template, request, flash


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@app.route("/register/", methods=["GET", "POST"])
def register():

    """
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
    
    if "@" not in email:
        flash("Email is invalid.", category="error")
    elif len(username) < 4:
        flash("Username must be longer than 3 characters", category="error")
    elif len(password) < 8:
        flash("Password must be at least 8 characters long", category="error")
    elif password != confirm_password:
        flash("Passwords do not match", category="error")
    else:
        flash("Successful.", category="success")
        pass
    """

    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)