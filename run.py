from facultybot_new import app
from facultybot_new.models import Remark
from datetime import datetime, timedelta
from threading import Timer
import random
import requests


def post_message(message):
    requests.post(app.config['SLACK_WEBHOOK_URL'], json={"text": message})


def set_timer():
    now = datetime.now()
    target = datetime(*(now.timetuple()[:3] + (10,)))
    if target < now:
        delta = timedelta(days=1)
        target += delta

    second = int((target - now).total_seconds())
    Timer(second, tweet, []).start()


def tweet():
    post_message("本日の名言:%s" % get_random_remark())
    set_timer()


def get_random_remark():
    total = Remark.query.count()
    if total == 0:
        return None

    todays_id = random.randrange(0, total)
    remark = Remark.query.offset(todays_id).first()
    return "『%s』 - %s" % (remark.body, remark.faculty.name)


def init_slack_timer():
    tweet()


if __name__ == '__main__':
    init_slack_timer()
    app.run()
