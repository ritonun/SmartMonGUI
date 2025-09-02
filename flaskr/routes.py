from flask import Blueprint, render_template, jsonify
from .smart import get_smart_status

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return """<h1>SmartMonGUI</h1>"""
