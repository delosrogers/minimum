from flask import current_app as app
from flask import Blueprint
import minimum.api.models as models

api_bp = Blueprint(
    "api_bp", __name__, template_folder="templates", static_folder="static"
)


@api_bp.route("/api/v1/a/<id>", methods=["GET"])
def get_article(id):
    print(a)
    return f"you made it to an article {id}"
