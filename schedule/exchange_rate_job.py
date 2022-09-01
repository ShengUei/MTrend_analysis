from datetime import datetime, timezone, timedelta
from sendEmail.send_email import send_email
from webCrawler.foreign_exchange_rate import get_daily_rate
from dataAccess.postgresql.data_access import insert_all_exchange_rate

def get_and_save_exchange_rate():
    dailyRateList = get_daily_rate()

    if not dailyRateList:
        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "Get Daily Exchange Rate Failure From web"
        content = "Get Daily Exchange Rate Failure From web at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
        send_email(title, content)
    
    else:
        insert_all_exchange_rate(dailyRateList)

        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "Get Daily Exchange Rate Success"
        content = "Get Daily Exchange Rate Success at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
        send_email(title, content)
