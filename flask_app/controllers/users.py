from flask_app import app 
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route("/")
def all_users():
    users = User.get_all_users()
    return render_template("read.html",users=users)

@app.route("/new")
def add_new():
    return render_template("create.html")

@app.route("/create", methods=["POST"])
def create_users():
    User.create_user(request.form)
    return redirect("/")

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("update.html",user=user)

@app.route("/show/<int:id>")
def show_user(id):
    data = {
        "id":id,
    }
    user = User.get_user(data)
    return render_template("show.html",user=user)

@app.route("/update/<int:id>",methods=["POST"])
def user_list(id):
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "id":id
    }
    User.edit_user(data)
    return redirect(f"/show/{id}")

@app.route("/delete/<int:id>")
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect ("/")