from datetime import datetime, timezone, timedelta

from sendEmail.send_email import send_email
from dataAccess.postgresql.data_access import get_currency_exchange_rate_by_date
from dataAccess.redis.connection import get_redis
from util.float_util import greatter_than

#job
def three_day_alert():
    target_list = ['USD', 'JPY']

    yesterday = datetime.now(timezone.utc).date() - timedelta(days = 1)

    for currency in target_list:
        check_spot_selling(yesterday, currency)

#action
def check_spot_selling(date, currency):
    currency_obj = get_currency_exchange_rate_by_date(date, currency)

    currency_abbr = currency_obj.currency.split('(')[1].split(')')[0]
    now_spot_selling = float(currency_obj.spot_selling)

    redis = get_redis()

    if redis.exists('%s_count' % currency_abbr) == 0:
        redis.set('%s_count' % currency_abbr, 0)

    if redis.exists('%s_yesterday_spot_selling' % currency_abbr) == 0:
        redis.set('%s_yesterday_spot_selling' % currency_abbr, now_spot_selling)
    
    if greatter_than(now_spot_selling, float(redis.get('%s_yesterday_spot_selling' % currency_abbr).decode("utf-8"))):
        redis.incr('%s_count' % currency_abbr)
        redis.set('%s_yesterday_spot_selling' % currency_abbr, now_spot_selling)  
    else:
        redis.decr('%s_count' % currency_abbr)
        redis.set('%s_yesterday_spot_selling' % currency_abbr, now_spot_selling)

    #check spot selling and send email
    if int(redis.get('%s_count' % currency_abbr).decode("utf-8")) == 3:
        redis.set('%s_count' % currency_abbr, 0)

        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "{} spot selling has been up for three days in a row.".format(currency_abbr)
        content = """
                    Date: {} \n 
                    Description: {} spot selling has been up for three days in a row. \n 
                    Suggestion: Today is a good sell point for {}.
                    """.format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'), currency_abbr, currency_abbr)
        send_email(title, content)
    
    if int(redis.get('%s_count' % currency_abbr).decode("utf-8")) == -3:
        redis.set('%s_count' % currency_abbr, 0)

        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "{} spot selling has been down for three days in a row.".format(currency_abbr)
        content = """
                    Date: {} \n 
                    Description: {} spot selling has been down for three days in a row. \n 
                    Suggestion: Today is a good buy point for {}.
                    """.format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'), currency_abbr, currency_abbr)
        send_email(title, content)
