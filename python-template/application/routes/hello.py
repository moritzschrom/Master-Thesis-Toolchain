from flask import Blueprint

hello_blueprint = Blueprint("hello", __name__)

@hello_blueprint.route("/hello-world")
def hello_world():
    return "Hello, World!", 200
