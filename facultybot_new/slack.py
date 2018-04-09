import requests
import random
from facultybot_new import app
from facultybot_new.models import Remark


def post_message(message):
    requests.post(app.config['SLACK_WEBHOOK_URL'], json={"text": message})


def tweet():
    post_message("本日の名言:%s" % get_random_remark())


def get_random_remark():
    total = Remark.query.count()
    if total == 0:
        return None

    todays_id = random.randrange(0, total)
    remark = Remark.query.offset(todays_id).first()
    return "『%s』 - %s" % (remark.body, remark.faculty.name)



