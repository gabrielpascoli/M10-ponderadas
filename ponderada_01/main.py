import requests as http_request
from flask import make_response, Flask, jsonify, request, render_template
from database.database import db
from database.models import Task
from flask_jwt_extended import JWTManager, set_access_cookies

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "goku-vs-vegeta" 
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)

# Método para criar um token
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route("/token", methods=["POST"])
def generate_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    task = Task.query.filter_by(username=username, password=password).first()
    if task is None:
        return jsonify({"msg": "Bad username or password"}), 401
    
    access_token = create_access_token(identity=task.id)
    return jsonify({ "token": access_token, "task_id": task.id })

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return_tasks = []
    for task in tasks:
        return_tasks.append(task.serialize())
    return jsonify(return_tasks)

# Adicione outras rotas CRUD para tarefas conforme necessário

@app.route("/user-login", methods=["GET"])
def user_login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_user():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if username is None or password is None:
        return render_template("error.html", message="Bad username or password")
    
    token_data = http_request.post("http://localhost:5000/token", json={"username": username, "password": password})
    if token_data.status_code != 200:
        return render_template("error.html", message="Bad username or password")
    
    response = make_response(render_template("content.html"))
    set_access_cookies(response, token_data.json()['token'])
    return response

@app.route("/user-register", methods=["GET"])
def user_register_page():
    return render_template("register.html")

@app.route("/content", methods=["GET"])
@jwt_required()
def secret_content():
    return render_template("content.html")

@app.route("/error", methods=["GET"])
def error_page():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
