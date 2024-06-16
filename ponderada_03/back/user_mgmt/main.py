from flask import Flask, jsonify, request
from database.database import db
from database.models import User
import requests

from flask_jwt_extended import JWTManager, set_access_cookies, create_access_token, jwt_required, get_jwt_identity

# Create the Flask app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "goku-vs-vegeta" 
# Seta o local onde o token será armazenado
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)

prefix = '/user_mgmt/'

# Verifica se o parâmetro create_db foi passado na linha de comando
import sys
if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    # cria o banco de dados
    with app.app_context():
        db.create_all()
    # Finaliza a execução do programa
    print("Database created successfully")
    sys.exit(0)

@app.route(f"{prefix}login", methods=["POST"])
async def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id, "username": user.username})

@app.route(f"{prefix}protected", methods=["GET"])
@jwt_required()
async def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route(f"{prefix}")
async def hello_world():
    return "<p>Hello, World!</p>"

# Adicionando as rotas CRUD para a entidade User
@app.route(f"{prefix}users", methods=["GET"])
async def get_users():
    users = User.query.all()
    return_users = []
    for user in users:
        return_users.append(user.serialize())
    return jsonify(return_users)

@app.route(f"{prefix}users/<int:id>", methods=["GET"])
async def get_user(id):
    user = User.query.get(id)
    return jsonify(user.serialize())

@app.route(f"{prefix}users", methods=["POST"])
async def create_user():
    data = request.json
    user = User(username=data["username"], email=data["email"], password=data["password"])
    exists = User.query.filter_by(email=user.email).first()
    if exists: return jsonify({"error": "Email already in use!"}), 400
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

@app.route(f"{prefix}users/<int:id>", methods=["PUT"])
async def update_user(id):
    data = request.json
    user = User.query.get(id)
    user.name = data["username"]
    user.email = data["email"]
    user.password = data["password"]
    db.session.commit()
    return jsonify(user.serialize())

@app.route(f"{prefix}users/<int:id>", methods=["DELETE"])
async def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize())