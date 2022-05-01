from flask import Blueprint, jsonify
from models import Switch

switches_blueprint = Blueprint('switches', __name__)

@switches_blueprint.route('', methods=['GET'])
def example() -> str:
    return 'switch endpoint test'


@switches_blueprint.route("/detail/<id>", methods=['GET'])
def switch_by_id(id: str) -> str:
    if not id.isdigit():
        return jsonify(
            {
                'error': 'id must be an integer'
            }
        ), 400
    id=int(id)
    switch = Switch.query.filter_by(id=id).first()

    if switch is None:
        return jsonify({'error': '404 not found'}), 404
    return jsonify(switch.serialize())