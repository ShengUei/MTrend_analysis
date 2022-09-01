# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime, timezone, timedelta

from schedule.exchange_rate_job import get_and_save_exchange_rate
from schedule.show_pid_job import show_pid
from sendEmail.send_email import send_email

get_and_save_exchange_rate()

# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()

print("Run schedule.py at %s" % datetime.now(timezone.utc))

try:
    print("Add Jobs to Scheduler at %s" % datetime.now(timezone.utc))

    #每週一 ~ 五 18:00 ，由網路抓匯率與存匯率至DB
    scheduler.add_job(get_and_save_exchange_rate, 'cron', day_of_week = '1-5', hour = 18, minute = 0, timezone = 'Asia/Taipei')

    scheduler.add_job(show_pid, 'interval', hours = 1)

    scheduler.start()

except Exception as e:
    scheduler.shutdown()

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    title = "Run scheduler Failure"
    content = "Run scheduler Failure at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
    send_email(title, content)
