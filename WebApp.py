import os
import requests
import markdown
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

<<<<<<< HEAD
# Path to the local README file
README_PATH = "C:/GitHub/New folder/Capstone_Portfolio/README.md"

def fetch_readme():
    with open(README_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        return markdown.markdown(content)
=======
# Environment variables for configuration
README_URL = os.getenv('README_URL', 'https://raw.githubusercontent.com/SamRobinson123/Capstone_Portfolio/main/README.md')

def fetch_readme():
    try:
        response = requests.get(README_URL)
        response.raise_for_status()
        content = response.text
        return markdown.markdown(content)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Failed to fetch README file: {e}")
        return f"Failed to fetch README file: {e}"
>>>>>>> 3c4e2eb9539769fdff6479ce62d65e7d8ef088db

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/default-model")
def default_model():
    readme_content = fetch_readme()
    return render_template("default_model.html", readme_content=readme_content)

<<<<<<< HEAD
@app.route("/<username>")
def user(username):
    return f"<h1>{username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

=======
>>>>>>> 3c4e2eb9539769fdff6479ce62d65e7d8ef088db
@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

<<<<<<< HEAD
@app.route("/default-model")
def default_model():
    readme_content = fetch_readme()
    return render_template("default_model.html", readme_content=readme_content)

=======
>>>>>>> 3c4e2eb9539769fdff6479ce62d65e7d8ef088db
@app.route("/<username>")
def user(username):
    return f"<h1>{username}</h1>"

if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1'], host='0.0.0.0', port=8080)
