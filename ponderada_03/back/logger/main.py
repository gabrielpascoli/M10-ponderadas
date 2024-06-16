from flask import Flask, request, jsonify
from database.database import db
from database.models import Log

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

prefix = '/logger/'

import sys
if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    # cria o banco de dados
    with app.app_context():
        db.create_all()
    # Finaliza a execução do programa
    print("Database created successfully")
    sys.exit(0)

@app.route(f"{prefix}log", methods=['POST'])
def log_event():
    data = request.json
    log = Log(username=data['username'], email=data['email'], action=data['action'], datetime=data['datetime'])
    db.session.add(log)
    db.session.commit()
    return jsonify(log.serialize()), 201

@app.route(f"{prefix}log", methods=['GET'])
def get_logs():
    logs = Log.query.all()
    return jsonify([log.serialize() for log in logs]), 200