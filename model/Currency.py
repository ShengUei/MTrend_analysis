import json

class Currency():
    def __init__(self):
        self.__quoted_date = None # datetime object
        self.__currency = ''
        self.__cash_buying = 0
        self.__cash_selling = 0
        self.__spot_buying = 0
        self.__spot_selling = 0

    @property
    def quoted_date(self):
        return self.__quoted_date

    @quoted_date.setter
    def quoted_date(self, input_quoted_date):
        self.__quoted_date = input_quoted_date

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, input_currency):
        self.__currency = input_currency

    @property
    def cash_buying(self):
        return self.__cash_buying

    @cash_buying.setter
    def cash_buying(self, input_cash_buying):
        self.__cash_buying = input_cash_buying

    @property
    def cash_selling(self):
        return self.__cash_selling

    @cash_selling.setter
    def cash_selling(self, input_cash_selling):
        self.__cash_selling = input_cash_selling

    @property
    def spot_buying(self):
        return self.__spot_buying

    @spot_buying.setter
    def spot_buying(self, input_spot_buying):
        self.__spot_buying = input_spot_buying

    @property
    def spot_selling(self):
        return self.__spot_selling

    @spot_selling.setter
    def spot_selling(self, input_spot_selling):
        self.__spot_selling = input_spot_selling
    
    def to_json(self):
        #example: self.__currency = American Dollar (USD)
        abbr = self.__currency.split('(')[1].split(')')[0]

        dict = {"quoted_date": self.__quoted_date.strftime('%Y-%m-%d'),
                "currency": abbr,
                "cash_buying": float(self.__cash_buying),
                "cash_selling": float(self.__cash_selling),
                "spot_buying": float(self.__spot_buying),
                "spot_selling": float(self.__spot_selling)}

        return json.dumps(dict) 
