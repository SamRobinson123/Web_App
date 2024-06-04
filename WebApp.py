import os
import requests
import markdown
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Path to the local README file
README_PATH = "C:/GitHub/New folder/Capstone_Portfolio/README.md"

def fetch_readme():
    with open(README_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        return markdown.markdown(content)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/default-model")
def default_model():
    readme_content = fetch_readme()
    return render_template("default_model.html", readme_content=readme_content)

@app.route("/<username>")
def user(username):
    return f"<h1>{username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/default-model")
def default_model():
    readme_content = fetch_readme()
    return render_template("default_model.html", readme_content=readme_content)

@app.route("/<username>")
def user(username):
    return f"<h1>{username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)