from dataAccess.postgresql.connection import openConnection
from model.Currency import Currency
from logger.logger import get_logger, close_handler


def get_currency_exchange_rate_by_date(date, currency):
    logger = get_logger()

    conn = openConnection()
    
    try:
        record = conn.execute("""
                                 SELECT quoted_date, currency, cash_buy, cash_sell, spot_buy, spot_sell
                                 FROM foreign_exchange_rate
                                 WHERE quoted_date::date = %(quoted_date)s AND currency ILIKE %(currency)s;
                                 """,
                                 {'quoted_date' : date, 
                                 'currency' : '%{}%'.format(currency)}).fetchone()

    except BaseException as e:
        conn.rollback()
        logger.error("BaseException : %s" % e, exc_info=True)
        return None

    else:
        conn.commit()
        currency_obj = Currency()
        
        currency_obj.quoted_date = record.get('quoted_date')
        currency_obj.currency = record.get('currency')
        currency_obj.cash_buying = record.get('cash_buy')
        currency_obj.cash_selling = record.get('cash_sell')
        currency_obj.spot_buying = record.get('spot_buy')
        currency_obj.spot_selling = record.get('spot_sell')

        return currency_obj
        
    finally:
        conn.close()
        close_handler(logger)
