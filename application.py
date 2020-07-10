from flask import Flask, request, render_template, jsonify
import numpy as np
from main import response

application = app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_test.html")

@app.route("/chat", methods = ["POST"])
def chat():     
    message = request.form.get("message")
    reply = response(str(message))
    return jsonify({"bot":reply,"user":message})
    

if __name__=="__main__":
    app.run(debug = True)
    