from flask import Flask, request, jsonify, render_template, abort
from tinydb import TinyDB, Query
from datetime import datetime   

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = TinyDB('db.json')

@app.route('/ping', methods=['GET'])
def ping():
    db.insert({
    "metodo": str(request.method),
    "hora":str(datetime.now()),
    "acao": "ping",
    "resposta": "pong"
    })
    return jsonify({'resposta': 'pong'})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data or 'dados' not in data:
        abort(400, description="Invalid data. Missing 'dados' key")
    resposta = {"resposta": data["dados"]}
    db.insert({
    "metodo": str(request.method),
    "hora":str(datetime.now()),
    "acao": "echo",
    "resposta": data["dados"]
    })
    return jsonify(resposta)
    
@app.route("/dash")
def dash():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html", logs=db.all())