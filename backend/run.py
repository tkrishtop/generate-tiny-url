from flask import Flask, render_template, flash, request, get_flashed_messages, redirect
from wtforms import Form, validators, StringField

import logging
import os
import string
from random import choice


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


HOST = "0.0.0.0"
PORT_FLASK = os.getenv('PORT', 5555)
APP_NAME = "https://generate-tiny-url.herokuapp.com/"

# ------------logging---------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('flask-backend')
# ----------------------------------------------------------------------------------

# ------------------- Codec --------------------------------------------------------
class Codec:
    def __init__(self):
        self.alphabet = string.ascii_letters + '0123456789'
        self.long2short = {}
        self.short2long = {}

    def encode(self, long_url):
        while long_url not in self.long2short:
            short_url = ''.join(choice(self.alphabet) for _ in range(6))
            if short_url not in self.short2long:
                self.short2long[short_url] = long_url
                self.long2short[long_url] = short_url
        return APP_NAME + self.long2short[long_url]

    def decode(self, short_url):
        suffix = short_url[-6:]
        if suffix in self.short2long:
            return self.short2long[suffix]
        else:
            return APP_NAME

# ----------------------------------------------------------------------------------

# ------------------- APIs ---------------------------------------------------------
class UrlForm(Form):
    name = StringField('Please enter long URL:', validators=[validators.Length(min=3), validators.url()])


@app.route("/", methods=['GET', 'POST'])
def home():
    form = UrlForm(request.form)

    if request.method == 'POST':
        name = request.form['name']

        if form.validate():
            logger.info(f"[OK] Form is validated: {name}")
            flash(codec.encode(name), 'info')
        else:
            logger.info(f"[Error] Form is NOT validated: {name}")
            flash('Please enter long URL in the correct format', 'error')
    else:
        logger.info('method GET')

    return render_template('home.html', form=form)


@app.route("/<short_url>", methods=['GET', 'POST'])
def togo(short_url):
    logger.info(f"[Redirect] Redirection request: {short_url}")
    long_url = codec.decode(short_url)
    logger.info(f"[Redirect2] Going to redirect to: {long_url}")
    if long_url == APP_NAME:
        flash(f"Short URL {APP_NAME + short_url} not found in DB, please try another one", 'error')
    return redirect(long_url)

# ---------------------------------------------------------------------------------

if __name__ == '__main__':
    codec = Codec()
    app.run(host=HOST, port=PORT_FLASK, debug=False)
