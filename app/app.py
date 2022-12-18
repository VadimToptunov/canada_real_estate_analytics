from flask import Flask, jsonify
from app.server import db

appFlask = Flask(__name__)


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