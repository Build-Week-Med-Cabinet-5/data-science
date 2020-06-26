'''
Code here was build from this article:
https://medium.com/@kellylougheed/make-a-flask-app-with-a-csv-as-a-flat-file-database-373632a2fba4
'''

import csv
from flask import Flask, render_template, jsonify

APP = Flask(__name__)

@APP.route("/")
def row():
    with open('cannabis.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        strains = []
        for row in data:
            if not first_line:
                strains.append({
                    "strain": row[0],
                    "type": row[1],
                    "rating": row[2],
                    "effects": row[3],
                    "flavor": row[4],
                    "description": row[5]
                })
            else:
                first_line = False
    return str(strains)


@APP.route("/pretty")
def index():
    with open('cannabis.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        strains = []
        for row in data:
            if not first_line:
                strains.append({
                    "strain": row[0],
                    "type": row[1],
                    "rating": row[2],
                    "effects": row[3],
                    "flavor": row[4],
                    "description": row[5]
                })
            else:
                first_line = False
    return render_template("base.html", strains=strains)


@APP.route('/<strain>')
def strain_url(strain):
    with open('cannabis.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        dict_strain = {}
        for row in data:
            if row[0] == strain:
                dict_strain = {
                    "strain": row[0],
                    "type": row[1],
                    "rating": row[2],
                    "effects": row[3],
                    "flavor": row[4],
                    "description": row[5]
                }
                break
    return dict_strain


@APP.route("/<strain>/pretty")
def pretty_url(strain):
    with open('cannabis.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        strains = []
        for row in data:
            if row[0] == strain:
                strains.append({
                    "strain": row[0],
                    "type": row[1],
                    "rating": row[2],
                    "effects": row[3],
                    "flavor": row[4],
                    "description": row[5]
                })
                break
    return render_template("base.html", strains=strains)




# command line code
#  FLASK_APP=exp.py flask run