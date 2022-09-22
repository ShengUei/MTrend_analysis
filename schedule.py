# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime, timezone, timedelta

from schedule.exchange_rate_analysis_job import three_day_alert
from sendEmail.send_email import send_email

three_day_alert()

# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()

print("Run schedule.py at %s" % datetime.now(timezone.utc))

try:
    print("Add Jobs to Scheduler at %s" % datetime.now(timezone.utc))

    #每週一 ~ 五 09:00 ，由 DB 抓匯率並分析
    scheduler.add_job(three_day_alert, 'cron', day_of_week = '1-5', hour = 9, minute = 0, timezone = 'Asia/Taipei')

    scheduler.start()

except Exception as e:
    scheduler.shutdown()

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    title = "Run three_day_alert scheduler Failure"
    content = "Run three_day_alert scheduler Failure at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
    send_email(title, content)
