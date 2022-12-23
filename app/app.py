import asyncio
import os

from flask_sqlalchemy import SQLAlchemy

from app.server import models
from apscheduler.schedulers.background import BackgroundScheduler
from data_gatherer import gather_rent_data
from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS, cross_origin

template_dir = os.path.abspath('./app/client/templates/')
static_dir = os.path.abspath('./app/client/static/')
db_path = "./gathering_scripts/rent-data-canada/database/apptdata.db"
appFlask = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
cors = CORS(appFlask)
appFlask.config['CORS_HEADERS'] = 'Content-Type'
appFlask.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(db_path)
appFlask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(appFlask)


@appFlask.route('/', methods=['GET'])
@cross_origin()
def index():
    return render_template("index.html")


@appFlask.route('/data', methods=['GET'])
@cross_origin()
def get_data_from_db():
    flats = models.Flats
    flats_data = db.session.query(flats)
    db.session.commit()
    for flat in flats_data:
        return jsonify({
            'status': 200,
            'homeid': flat.homeid,
            'latlong': flat.latlong,
            'latitude': flat.latitude,
            # self.longitude = self.db.Column(self.db.String)
            # self.postal_code = self.db.Column(self.db.String)
            # self.fsa = self.db.Column(self.db.String)
            # self.rent_price = self.db.Column(self.db.Integer)
        })

    # flats = [b.serialize() for b in db.view()]
    return jsonify({
        'res': flatsData,
        'status': '200',
        'no_of_prices': len(flatsData)
    })


@appFlask.route('/favicon.ico')
@cross_origin()
def favicon():
    return send_from_directory(os.path.join(static_dir, 'images/'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def background_job():
    asyncio.get_event_loop().run_until_complete(gather_rent_data())


if __name__ == '__main__':
    appFlask.run()
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(background_job, 'cron', day_of_week='mon-sun', hour=19, minute=30)
    scheduler.start()
