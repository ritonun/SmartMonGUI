from flask import Blueprint, render_template, jsonify, request
from .smart import get_smart_status, get_devices

main = Blueprint('main', __name__)

@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "scan" in request.form:
            get_devices()

    return render_template("index.html")
