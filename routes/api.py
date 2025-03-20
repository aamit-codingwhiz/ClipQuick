from flask import Blueprint, request, jsonify
from services.shorten_url_service import ShortenURLService


api_bp = Blueprint("api", __name__)

@api_bp.route("/api/shorten", methods=["POST"])
def api_shorten():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    original_url = data.get("original_url")

    if not original_url:
        return jsonify({"error": "Missing URL"}), 400

    short_code, qr_filename = ShortenURLService.shorten_url(original_url)
    short_url = request.host_url.rstrip("/") + "/" + short_code
    print(f"api > short_url: {short_url}")

    return jsonify({"short_url": short_url})
