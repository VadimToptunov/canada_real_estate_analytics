import os

from flask import Flask, jsonify, render_template
from app.server import db

template_dir = os.path.abspath('./client/templates/')
static_dir = os.path.abspath('./client/static/')
appFlask = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


@appFlask.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@appFlask.route('/data', methods=['GET'])
def get_data_from_db():
    flats = [b.serialize() for b in db.view()]
    return jsonify({
                'res': flats,
                'status': '200',
                'no_of_prices': len(flats)
            })


if __name__ == '__main__':
    appFlask.run()