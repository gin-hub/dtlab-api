from flask import Blueprint
from db import Switch, getSession
from sqlalchemy import select

switches_blueprint = Blueprint('switches', __name__)

# @switches_blueprint.route("/", methods=['GET'])
# def all() -> None:
#     return 'all endpoint'


@switches_blueprint.route("/", methods=['GET'])
def example() -> str:
    return 'example'
