import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/listings.html')
def listings():
    return render_template("listings.html")

@app.route('/input.html')
def input():
    return render_template("input.html")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
