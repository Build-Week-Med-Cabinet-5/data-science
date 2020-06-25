# Directory.py



# Import

from flask import Blueprint, render_template


# Make Blueprint for __init__.py

Directory = Blueprint("Directory", __name__)


# App Welcome Page

@Directory.route('/')
def index():
    return render_template("home.html", message = "DS Med Cabinet API using natural language processing to recommend the best cannabis strains to Med Cabinet members.")


# Strain JSON Page

@Directory.route("/strainjson")
def df():
    return render_template("json.html")


# Strain Table Page

@Directory.route("/straintable")
def dataframe():
    return render_template("df.html")
