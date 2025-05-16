from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt

app = Flask(__name__)
app.secret_key = ""

users = {}  # username: hashed_password


@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html", user=user)


@app.route("/register", methods=["GET", "POST"])
def registros():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Hashear la contraseña
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Guardar el usuario con su contraseña hasheada
        users[username] = hashed_pw

        session["user"] = username
        print(users)
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=2009)
