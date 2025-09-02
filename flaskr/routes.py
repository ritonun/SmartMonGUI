from flask import Blueprint, render_template, jsonify, request
from .smart import get_devices

main = Blueprint('main', __name__)

@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "scan" in request.form:
            devices = get_devices()
            for device in devices:
                print(f"Found {device}")

    return render_template("index.html")
