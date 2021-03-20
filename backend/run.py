from flask import Flask, jsonify
import logging
import os


app = Flask(__name__)

HOST = "0.0.0.0"
PORT_FLASK = os.getenv('PORT', 5555)

# ------------logging---------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('flask-backend')
# ----------------------------------------------------------------------------------


# ------------------- APIs ---------------------------------------------------------
@app.route('/')
def home():
    message = dict()
    data = dict()

    message['message'] = 'Hello World from Flask!'
    data['status'] = 200
    data['data'] = message

    return jsonify(data)

# ---------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(host=HOST, port=PORT_FLASK, debug=False)