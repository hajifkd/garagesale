import atexit
from facultybot_new import app
from facultybot_new.slack import tweet
from apscheduler.schedulers.background import BackgroundScheduler


def init_slack_timer():
    scheduler = BackgroundScheduler(timezone='Asia/Tokyo')
    scheduler.start()
    scheduler.add_job(tweet, 'cron', hour=10, minute=0)
    atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    init_slack_timer()
    app.run()
