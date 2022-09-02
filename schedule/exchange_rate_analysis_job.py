from datetime import datetime, timezone, timedelta
from sendEmail.send_email import send_email
from dataAccess.postgresql.data_access import get_currency_exchange_rate_by_date
from dataAccess.redis.connection import get_redis

#job
def three_day_alert():
    target_list = ['USD', 'JPY']

    for currency in target_list:
        check_spot_selling(currency)

#action
def check_spot_selling(currency):
    tody = datetime.now(timezone.utc).date() - timedelta(days = 1)

    currency_obj = get_currency_exchange_rate_by_date(tody, currency)

    currency = currency_obj.currency
    spot_selling = currency_obj.spot_selling

    redis = get_redis()

    if redis.exists('%s_count' % currency) is 0:
        redis.set('%s_count' % currency, 0)

    if redis.exists('%s_yestary_spot_selling' % currency) is 0:
        redis.set('%s_yestary_spot_selling' % currency, spot_selling)
    
    if redis.get('%s_yestary_spot_selling' % currency) > spot_selling:
        redis.incr('%s_count' % currency)
        redis.set('%s_yestary_spot_selling' % currency, spot_selling)  
    else:
        redis.decr('%s_count' % currency)
        redis.set('%s_yestary_spot_selling' % currency, spot_selling)

    #check spot selling and send email
    if redis.get('%s_count' % currency) == 3:
        redis.set('%s_count' % currency, 0)

        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "{} spot selling has been up for three days in a row.".format(currency)
        content = """
                    Date: {} \n 
                    Description: {} spot selling has been up for three days in a row. \n 
                    Suggestion: Today is a good sell point for {}.
                    """.format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'), currency, currency)
        send_email(title, content)
    
    if redis.get('%s_count' % currency) == -3:
        redis.set('%s_count' % currency, 0)

        now = datetime.now(timezone.utc)
        local_datetime = now + timedelta(hours = 8)

        title = "{} spot selling has been down for three days in a row.".format(currency)
        content = """
                    Date: {} \n 
                    Description: {} spot selling has been down for three days in a row. \n 
                    Suggestion: Today is a good buy point for {}.
                    """.format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'), currency, currency)
        send_email(title, content)
