from flask import Blueprint, render_template, abort

home = Blueprint('home', __name__)

@home.route('/')
def landing():
    return render_template('home.html')

@home.route('/information')
def info():
    return render_template('information.html')

@home.route('/projects')
def projects():
    return render_template('projects.html')

@home.route('/test')
def test():
    abort(418)