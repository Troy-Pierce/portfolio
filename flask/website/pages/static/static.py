from flask import Blueprint, send_from_directory

static = Blueprint('static', __name__)

@static.route('/<path:path>/<path:name>')
def home(path, name):
    return send_from_directory('pages/Static/'+path,name)
