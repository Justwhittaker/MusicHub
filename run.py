import os
import datetime
import favicon
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from tabulate import tabulate
from flask_paginate import Pagination, get_page_parameter
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    per_page = 3
    page = request.args.get(get_page_parameter(), type=int, default=1)
    recipes = mongo.db.recipes.find().sort("timestamp", -1)
    pagination = Pagination(page=page, total=recipes.count(),
                            per_page=per_page,
                            search=False, record_name='recipes',
                            css_framework='bootstrap4', alignment='center')
    recipe_page = recipes.skip((page - 1) * per_page).limit(per_page)
    return render_template("index.html",
                           recipes=recipe_page, pagination=pagination)


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("index.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route('/about')
def about():
    # about section with how to index and FAQ
    return render_template("about.html")


@app.route('/privacy')
def privacy():
    # about section with how to index and FAQ
    return render_template("privacy_policy.html")


@app.route('/listings')
def listings():
    recipes = mongo.db.recipes.find().sort("RecipeName", 1)
    return render_template("listings.html", recipes=recipes)
    return render_template("listings.html")


app.config["IMAGES"] = "/workspace/PRO3-RecipeCloud/static/img/uploads"
app.config["ALLOWED_IMAGE"] = ["PNG", "JPG", "JPEG"]


@app.route("/input", methods=["GET", "POST"])
def input():
    # POST recipe to recipes DB
    if request.method == "POST":
        upload = {
            "timestamp": datetime.datetime.now(),
            "RecipeName": request.form.get("RecipeName"),
            "PrepTime": request.form.get("PrepTime"),
            "CookingTime": request.form.get("CookingTime"),
            "DifficultyLevel": request.form.get("DifficultyLevel"),
            "Serves": request.form.get("Serves"),
            "Ingredient": request.form.getlist("Ingredient"),
            "Add_ingredient": request.form.getlist("Ingredient"),
            "Qty": request.form.get("Qty"),
            "Instruction": request.form.getlist("Instruction"),
            "upload_pic": request.form.get("upload_pic"),
            "created_by": session["user"],
        }
        mongo.db.recipes.insert_one(upload)
        flash("Recipe Successfully added!" )
    return render_template("input.html")


@app.route("/edit_recipes/<recipes_id>", methods=["GET", "PUT"])
def edit_recipes(recipes_id):
    # Update recipe to recipes DB
    if request.method == "PUT":
        upload = {'$set': {
                  "timestamp": datetime.datetime.now(),
                  "RecipeName": request.form.get("RecipeName"),
                  "PrepTime": request.form.get("PrepTime"),
                  "CookingTime": request.form.get("CookingTime"),
                  "DifficultyLevel": request.form.get("DifficultyLevel"),
                  "Serves": request.form.get("Serves"),
                  "Ingredient": request.form.getlist("Ingredient"),
                  "Add_ingredient": request.form.getlist("Ingredient"),
                  "Qty": request.form.get("Qty"),
                  "Instruction": request.form.getlist("Instruction"),
                  "created_by": session["user"],
                  }}
        mongo.db.tasks.update_one({"_id": ObjectId(recipes_id)}, upload)
        flash("Task Successfully Updated")
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    return render_template("edit_recipes.html", recipes=recipes)


@app.route("/delete_recipes/<recipes_id>", methods=["GET"])
def delete_recipes(recipes_id):
    # Delete recipe to recipes DB
    mongo.db.recipes.delete_one({"_id": ObjectId(recipes_id)})
    recipes = mongo.db.recipes.find().sort("RecipeName", 1)
    flash("Recipe Successfully deleted!")
    return render_template("listings.html", recipes=recipes)


def allow_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE"]:
        return True
    else:
        return False

   # if request.method == "POST":

    # if request.files:
    # image = request.files["image"]

    # if image.filename == "":
    #   print("Image needs a filename")
    #  return redirect(request.url)

    # if not allow_image(image.filename):
    #  print("That file extension is not allowed")
    #  return redirect(request.url)
#
    # else:
    # filename = secure_filename(image.filename)

    #  image.save(os.path.join(app.config["IMAGES"], filename))

    # print("Saved Image")

    # return redirect(request.url)

   # return render_template("input.html")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
