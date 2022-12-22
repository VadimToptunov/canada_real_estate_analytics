import asyncio
import os

from app.server import db
from apscheduler.schedulers.background import BackgroundScheduler
from data_gatherer import gather_rent_data
from flask import Flask, jsonify, render_template, send_from_directory

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


@appFlask.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(static_dir, 'images/'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def background_job():
    asyncio.get_event_loop().run_until_complete(gather_rent_data())


if __name__ == '__main__':
    appFlask.run()
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(background_job, 'cron', days_of_week='mon-sun', minutes=30, hours=19)
    scheduler.start()
