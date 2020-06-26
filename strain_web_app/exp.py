'''
Code here was build from this article:
https://medium.com/@kellylougheed/make-a-flask-app-with-a-csv-as-a-flat-file-database-373632a2fba4

Command line code to run: FLASK_APP=exp.py flask run 
'''

import csv
from flask import Flask, render_template


APP = Flask(__name__)

# route to display dictionary list
@APP.route("/")
def row():
    '''
    For loops the cannabis.csv file appending each row to a list.
    Does not include the first line, since that is our headers in the csv file.
    Returning that list.
    '''
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

# route to display dictionary list via template
@APP.route("/pretty")
def index():
    '''
    For loops the cannabis.csv file appending each row to a list.
    Does not include the first line, since that is our headers in the csv file.
    Returning the list via a template.
    '''
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

# route to display single dictionary list item as JSON object
@APP.route('/<strain>')
def strain_url(strain):
    '''
    Parameters: name of strain from database as a string.
    For loops the cannabis.csv file, creating a dictionary.
    Returning only the strain that was given as a parameter.
    '''
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

# route to display single dictionary list item via template
@APP.route("/<strain>/pretty")
def pretty_url(strain):
    '''
    Parameters: name of strain from database as a string.
    For loops the cannabis.csv file appending each row to a list.
    Returning only the strain that was given as a parameter.
    '''
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
