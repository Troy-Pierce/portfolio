from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
from logging import getLogger
from os import path

app = Flask(__name__, subdomain_matching=True)

gunicorn_logger = getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
def create_app():
    app.config['SECRET_KEY'] = '5d72d3cf91ba2f44710b6efa9a079a97c8de571bd35e29bb9824fa23dfed08a301a2750aa30cb5208f52a15eb88a3e5600e231609a5e4439b51f823937afcdc14dfd20ebfd223a6a561dc995b23e8cf118fa16dff779f85b89381ebdba76744f8a54491f'
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

    # now you're handling non-HTTP exceptions only
    return render_template("error.html", error=error), 500