import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/listings')
def listings():
    return render_template("listings.html")


app.config["IMAGES"] = "/workspace/PRO3-RecipeCloud/static/img"


@app.route("/input", methods=["GET", "POST"])
def input():

    if request.method == "POST":

        if request.files:
            image = request.files["image"]

            image.save(os.path.join(app.config["IMAGES"], image.filename))

            print("Saved Image")

            return redirect(request.url)

    return render_template("input.html")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
