from flask import Flask, request, render_template, jsonify, session
import numpy as np
from main import *
from create_db import *
import os


application = app = Flask(__name__)
app.secret_key = os.urandom(24)
db.init_app(application)

@app.route("/")
def index():
    return render_template("index_test.html")

@app.route("/chat", methods = ["POST"])
def chat():     
    message = request.form.get("message")
    reply = response(str(message))
    return jsonify({"bot":reply,"user":message})

def points(s):    
    if classify(s)[0][0] == "Exp_Fresher_level":
        session["exp_pts"] = 2
    elif classify(s)[0][0] == "Exp_Intermediate_level":
        session["exp_pts"] = 5
    elif classify(s)[0][0] == "Exp_Pro_level":
        session["exp_pts"] = 8
    elif classify(s)[0][0] == "Basic_proj":
        session["project_pts"] = 2
    elif classify(s)[0][0] == "Intermediate_proj":
        session["project_pts"] = 4
    elif classify(s)[0][0] == "Exp_proj_lvl1":
        session["project_pts"] = 6
    elif classify(s)[0][0] == "Exp_proj_lvl2":
        session["project_pts"] = 8
    elif classify(s)[0][0] == "Skill_Basic":
        session["skill_pts"] = 3
    elif classify(s)[0][0] == "Skill_Int":
        session["skill_pts"] = 6
    elif classify(s)[0][0] == "Skill_Pro":
        session["skill_pts"] = 10
    elif classify(s)[0][0] == "Acceptable_role":
        elements["jobrole"] = s
        
    elif s == ('exit' or 'Exit'):
        return elements
    

if __name__=="__main__":
    app.run(debug = True)
    