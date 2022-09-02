from datetime import datetime, timezone, timedelta
from sendEmail.send_email import send_email
from dataAccess.postgresql.data_access import get_currency_exchange_rate_by_date

def three_day_alert():

    tody = datetime.now(timezone.utc).date() - timedelta(days = 1)

    currency_obj = get_currency_exchange_rate_by_date(tody, 'usd')

    if not currency_obj is None:
        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "Get Daily Exchange Rate Failure From web"
        content = "Get Daily Exchange Rate Failure From web at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
        send_email(title, content)
    
    else:

        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "Get Daily Exchange Rate Success"
        content = "Get Daily Exchange Rate Success at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
        send_email(title, content)
