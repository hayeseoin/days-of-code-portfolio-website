from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from projects import markdown_processor
import os
import json
import os

app = Flask(__name__)
ckeditor = CKEditor(app)
Bootstrap5(app)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lumen'

DAYS_OF_CODE_PORTFOLIO = []

def get_days_of_code() -> None:
    global DAYS_OF_CODE_PORTFOLIO
    projects_list: list[str] = [
        f'./days-of-code-portfolio/{entry}' for entry
        in os.listdir('days-of-code-portfolio')
        ]
    DAYS_OF_CODE_PORTFOLIO = [markdown_processor(i) for i in projects_list]

@app.route("/portfolio/days-of-code")
def days_of_code_portfolio():
    get_days_of_code()
    return render_template("projects.html", projects=DAYS_OF_CODE_PORTFOLIO)

@app.route('/portfolio/days-of-code/<project_name>')
def days_of_code_entry(project_name):
    get_days_of_code()
    for i in DAYS_OF_CODE_PORTFOLIO:
        if not i.get('title_url') == project_name:
            continue
        project = i
        break
    return render_template('project_entry.html', project=project)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    content = markdown_processor('./pages/about.md')
    return render_template("general_content.html", content=content)

@app.route("/development")
def development():
    content = markdown_processor('./pages/plans.md')
    return render_template("general_content.html", content=content)


if __name__ == "__main__":
    app.run(debug=True)

