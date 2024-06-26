import os
from flask import Flask, redirect, url_for, render_template
from urllib.parse import quote
import requests
import markdown

application = Flask(__name__)

# Environment variables for configuration
README_URL = os.getenv('README_URL', 'https://raw.githubusercontent.com/SamRobinson123/Capstone_Portfolio/main/README.md')

def fetch_readme():
    try:
        response = requests.get(README_URL)
        response.raise_for_status()
        content = response.text
        return markdown.markdown(content)
    except requests.exceptions.RequestException as e:
        application.logger.error(f"Failed to fetch README file: {e}")
        return f"Failed to fetch README file: {e}"

@application.route("/")
def home():
    return render_template("index.html")

@application.route("/default-model")
def default_model():
    readme_content = fetch_readme()
    return render_template("default_model.html", readme_content=readme_content)

@application.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@application.route("/<username>")
def user(username):
    return f"<h1>{username}</h1>"

if __name__ == "__main__":
    application.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1'], host='0.0.0.0', port=8080)
