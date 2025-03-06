import os
from flask import Flask, render_template, request

app = Flask(__name__,
            static_url_path='/website',  # Defines the URL prefix for static files
            static_folder='website')     # Points to the directory containing static files


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("Home.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/contact")
def contact():
    return render_template("Contact.html")




if __name__ == "__main__":
    app.run(debug=True)
