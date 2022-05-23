from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
from logging import getLogger
from os import path

app = Flask(__name__, subdomain_matching=True)

gunicorn_logger = getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
def create_app():
    from keys import secret_key
    app.config['SECRET_KEY'] = secret_key
    app.config['SESSION_COOKIE_SECURE'] = True
    from .pages import home
    from .pages.static import static
    app.register_blueprint(static.static, url_prefix="/static")
    app.register_blueprint(home.home, url_prefix='/')

    app.config['SESSION_COOKIE_SAMESITE'] = "Lax"
    
    return app

@app.errorhandler(Exception)
def generic_error(error):
    if isinstance(error, HTTPException):
        return render_template('error.html', error=error), error.code
    return render_template("error.html", error=error), 500