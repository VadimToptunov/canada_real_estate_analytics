from flask import Flask, jsonify
import db

appFlask = Flask(__name__)


@appFlask.route('/', methods=['GET'])
def getRequest():
    flats = [b.serialize() for b in db.view()]
    return jsonify({
                'res': flats,
                'status': '200',
                'no_of_prices': len(flats)
            })


if __name__ == '__main__':
    appFlask.run()
