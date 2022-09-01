# Note: the module name is psycopg, not psycopg3
import psycopg
from psycopg.rows import dict_row
from setting.connect_setting import get_conn_setting

# Connect to database
def openConnection():
    conn = psycopg.connect(get_conn_setting(), row_factory = dict_row)
    return conn
