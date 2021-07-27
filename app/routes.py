from app import app
from flask import render_template, jsonify, send_from_directory, request, abort
from flask import Response
from app.services import search
from config import config


def __generate_response_error(message: str) -> Response:
    return jsonify({"error": {"message": message}})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/image/")
def get_image():
    filename = request.args.get('filename')
    if not filename:
        abort(404)
    return send_from_directory(config.IMAGES_FOLDER, filename)


@app.route("/api/search/")
def api_search_param_exception():
    return __generate_response_error("search api requires query param: /api/search/<query>")


@app.route("/api/search/<query>")
def api_search(query: str):
    return jsonify(search.find_images(query))

