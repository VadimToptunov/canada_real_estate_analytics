from flask import Flask, request, jsonify
from app import db

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    flats = [b.serialize() for b in db.view()]
    if content_type == 'application/json':
        return jsonify({
            'res': flats,
            'status': '200',
            'msg': 'Success getting all books in library!👍😀',
            'no_of_books': len(flats)
        })


if __name__ == '__main__':
    pass
