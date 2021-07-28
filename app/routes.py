from flask import render_template, jsonify, send_from_directory, request, abort
from flask import Response, Blueprint
from app.services import search
from config import config

bp = Blueprint('main', __name__, template_folder='templates', url_prefix=config.URL_PREFIX)


def __generate_response_error(message: str) -> Response:
    return jsonify({"error": {"message": message}})


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/image/")
def get_image():
    filename = request.args.get('filename')
    if not filename:
        abort(404)
    return send_from_directory(config.IMAGES_FOLDER, filename)


@bp.route("/api/search/")
def api_search_param_exception():
    return __generate_response_error("search api requires query param: /api/search/<query>")


@bp.route("/api/search/<query>")
def api_search(query: str):
    return jsonify(search.find_images(query))

