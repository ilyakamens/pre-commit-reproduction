from flask import Blueprint, Flask, jsonify

app = Flask(__name__)

bp = Blueprint("foo", __name__)


@bp.route("/status")
def status():
    """Return the status."""
    return jsonify("foo: OK")


app.register_blueprint(bp, url_prefix="/foo")
