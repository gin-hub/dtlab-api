from flask import Blueprint

router_blueprint = Blueprint('routers', __name__)

@router_blueprint.route("/")
def example() -> None:
    return 'example'