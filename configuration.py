from flask import Blueprint

configuration_blueprint = Blueprint('configuration', __name__)

@configuration_blueprint.route("/")
def example() -> None:
    return 'example'