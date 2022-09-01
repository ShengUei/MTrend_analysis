from dataAccess.postgresql.connection import openConnection
from model import Currency
from logger.logger import get_logger


def get_currency_exchange_rate(date, currency):
    # logger = get_logger()

    conn = openConnection()
    
    try:
        record = conn.execute("""
                                 SELECT quoted_date, currency, cash_buy, cash_sell, spot_buy, spot_sell
                                 FROM foreign_exchange_rate
                                 WHERE quoted_date::date = %(quoted_date)s AND currency ILIKE %(currency)s;
                                 """,
                                 {'quoted_date' : date, 
                                 'currency' : '%{}%'.format(currency)}).fetchall()

    except BaseException as e:
        conn.rollback()
        print("BaseException : %s" % e)
        # logger.error("BaseException : %s" % e)
        return None

    else:
        conn.commit()
        print("Get %s Exchange Rate is Success" % currency)
        # logger.info("Get %s Exchange Rate is Success" % currency)
        # currency_obj = Currency()
        # for row in record:
        #     currency_obj.quoted_date = row
        # return currency_obj
        return record
        
    finally:
        conn.close()
