from flask import Blueprint, render_template, jsonify
from .smart import get_smart_status

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")
