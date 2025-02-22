from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from projects import projects_json
import os


app = Flask(__name__)
ckeditor = CKEditor(app)
Bootstrap5(app)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lumen'

projects_folder = os.listdir('projects')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/about")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    projects_json()
    app.run(debug=True)
