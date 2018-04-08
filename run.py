from facultybot_new import app
from facultybot_new.models import Remark
from datetime import datetime, timedelta
from threading import Timer
import random
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import atexit


def post_message(message):
    requests.post(app.config['SLACK_WEBHOOK_URL'], json={"text": message})


def tweet():
    post_message("本日の名言:%s" % get_random_remark())
    print('aa')


def get_random_remark():
    total = Remark.query.count()
    if total == 0:
        return None

    todays_id = random.randrange(0, total)
    remark = Remark.query.offset(todays_id).first()
    return "『%s』 - %s" % (remark.body, remark.faculty.name)


def init_slack_timer():
    scheduler = BackgroundScheduler(timezone='Asia/Tokyo')
    scheduler.start()
    scheduler.add_job(tweet, 'cron', hour=10, minute=0)
    atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    init_slack_timer()
    app.run()
