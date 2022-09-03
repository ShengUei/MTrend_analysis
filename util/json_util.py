from datetime import datetime, date, time
from decimal import Decimal
import json
import types

class json_encoder(json.JSONEncoder):
    def default(self, obj):
            if types.FunctionType == type(obj):
                return obj.__name__
            # sets become lists
            if isinstance(obj, set):
                return list(obj)
            # datetimes become strings
            if isinstance(obj, datetime):
                return obj.isoformat()
            # dates become strings
            if isinstance(obj, date):
                return obj.isoformat()
            # times become strings
            if isinstance(obj, time):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return float(obj)
            if isinstance(obj, type):
                return str(obj)

            return json.JSONEncoder.default(self, obj)


def object_to_json(obj):
    return json.dumps(obj.__dict__, cls = json_encoder)
