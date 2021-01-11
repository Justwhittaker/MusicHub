import os
import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home page - Search bar and all recipes shorthand discription
@app.route('/')
def index():
    """ recipes on the page to show 3 """
    per_page = 3
    page = request.args.get(get_page_parameter(), type=int, default=1)
    recipes = mongo.db.recipes.find().sort("timestamp", -1)
    """pagination for users to flip through different recipes - assistance provided by Cormac_Tutor at CI"""
    pagination = Pagination(page=page, total=recipes.count(),
                            per_page=per_page,
                            search=False, record_name='recipes',
                            css_framework='bootstrap4', alignment='center')
    """pagination to skip though 3 id per page """
    recipe_page = recipes.skip((page - 1) * per_page).limit(per_page)
    return render_template("index.html",
                           recipes=recipe_page, pagination=pagination)


# Read individual recipe ingredients
@app.route("/get_recipe/<recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    """allow user to retreive the full recipe for usage"""
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("get_recipe.html", recipe=recipe)


# search query
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    print(query)
    recipe = mongo.db.recipes.find({"$text": {"$search": query,
                                              "$caseSensitive": False,
                                              "$diacriticSensitive": False}})
    return render_template("search_recipe.html", recipe=recipe)


# User registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """ check if username already exists in db"""
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        """ Register user info"""
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        """ put the new user into 'session' cookie"""
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


# User Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """check if username exists in db"""
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            """ensure hashed password matches user input"""
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                """redirect to profile if submitted correctly"""
                return redirect(url_for("profile", username=session["user"]))
            else:
                """Else invalid password match try again"""
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            """Else if username doesn't exist"""
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        """ recipes on the page to show 3 """
        per_page = 3
        page = request.args.get(get_page_parameter(), type=int, default=1)
        recipes = mongo.db.recipes.find({"created_by": session["user"]})
        """pagination for users to flip through different recipes"""
        pagination = Pagination(page=page, total=recipes.count(),
                                per_page=per_page,
                                search=False, record_name='recipes',
                                css_framework='bootstrap4', alignment='center')
        recipe_page = recipes.skip((page - 1) * per_page).limit(per_page)
        """redirect to profile if submitted correctly"""
        return render_template("profile.html", username=username,
                               recipes=recipe_page, pagination=pagination)
    return redirect(url_for("login"))


# User Logout
@app.route("/logout")
def logout():
    """Remove user from session cookie"""
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


# About - introduction and quick explaination for CRUD ops
@app.route('/about')
def about():
    """about section with how to index and FAQ"""
    return render_template("about.html")


# Privacy policy - GDPR instructions and data holding
@app.route('/privacy')
def privacy():
    return render_template("privacy_policy.html")


# Admin page for editing and deleting power over all users
@app.route('/listings')
def listings():
    """ recipes on the page to show 3 """
    per_page = 3
    page = request.args.get(get_page_parameter(), type=int, default=1)
    recipe = mongo.db.recipes.find().sort("timestamp", -1)
    """pagination for users to flip through different recipes"""
    pagination = Pagination(page=page, total=recipe.count(),
                            per_page=per_page,
                            search=False, record_name='recipes',
                            css_framework='bootstrap4', alignment='center')
    recipe_page = recipe.skip((page - 1) * per_page).limit(per_page)
    return render_template("listings.html",
                           recipe=recipe_page, pagination=pagination)


# add recipe is the Create id for the DB
@app.route("/add_recipe", methods=["GET", "POST", "PUT"])
def add_recipe():
    """POST recipe to recipes DB"""
    if request.method == "POST":
        """Upload recipe to recipes DB"""
        upload = {
            "timestamp": datetime.datetime.now(),
            "recipe_name": request.form.get("recipe_name"),
            "category": request.form.get("category"),
            "prep_time": int(request.form.get("prep_time")),
            "cooking_time": int(request.form.get("cooking_time")),
            "difficulty_level": request.form.get("difficulty_level"),
            "serves": int(request.form.get("serves")),
            "ingredient": request.form.getlist("ingredient"),
            "instruction": request.form.getlist("instruction"),
            "upload_pic": request.form.get("upload_pic"),
            "created_by": session["user"],
        }
        """insert_one recipe creating a new id to recipes DB"""
        mongo.db.recipes.insert_one(upload)
        flash("Recipe Successfully added!")
        """redirect to profile if submitted correctly"""
        return redirect(url_for("profile", username=session["user"]))
    return render_template("add_recipe.html")


# Edit Recipes for id's in DB
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """Update recipe to recipes DB"""
    if request.method == "POST":
        """submit and set the edit for the DB"""
        submit = {'$set': {
            "timestamp": datetime.datetime.now(),
            "recipe_name": request.form.get("recipe_name"),
            "category": request.form.get("category"),
            "prep_time": int(request.form.get("prep_time")),
            "cooking_time": int(request.form.get("cooking_time")),
            "difficulty_level": request.form.get("difficulty_level"),
            "serves": int(request.form.get("serves")),
            "ingredient": request.form.getlist("ingredient"),
            "instruction": request.form.getlist("instruction"),
            "upload_pic": request.form.get("upload_pic"),
            "created_by": session["user"],
        }}
        """Update_one recipe along the id to recipes DB"""
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        """redirect to profile if submitted correctly"""
        return redirect(url_for("profile", username=session["user"]))
    recipe_to_edit = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe_id=recipe_id,
                           recipe=recipe_to_edit)


# Delete Recipes in DB
@app.route("/delete_recipe/<recipe_id>", methods=["GET"])
def delete_recipe(recipe_id):
    """Delete recipe to recipes DB"""
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    recipe_id = mongo.db.recipes.find_one()
    flash("Recipe Successfully deleted!")
    """ recipes on the page to show 3 """
    per_page = 3
    page = request.args.get(get_page_parameter(), type=int, default=1)
    recipes = mongo.db.recipes.find().sort("timestamp", -1)
    """pagination for users to flip through different recipes"""
    pagination = Pagination(page=page, total=recipes.count(),
                            per_page=per_page,
                            search=False, record_name='recipes',
                            css_framework='bootstrap4', alignment='center')
    recipe_page = recipes.skip((page - 1) * per_page).limit(per_page)
    """redirect to profile if submitted correctly"""
    return redirect(url_for("profile", username=session["user"]))
    return render_template("profile.html", username=session["user"],
                           recipe=recipe_page, recipe_id=recipe_id,
                           pagination=pagination)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
