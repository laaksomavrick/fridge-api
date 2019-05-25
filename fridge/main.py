from flask import Flask, jsonify
from fridge import users
app = Flask(__name__)

app.register_blueprint(users.routes.blueprint)

@app.route("/")
def hello():
    return jsonify({'hello': 'world'})
