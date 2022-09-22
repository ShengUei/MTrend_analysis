from datetime import datetime, timezone
import logging
import os

#設定 logs 目錄
dir_path = './logger/logs/'

#設定 log 資料夾
error_log_folder = 'error_log/'

#設定檔名
filename = "{:%Y-%m-%d}".format(datetime.now(timezone.utc)) + '.log'

def get_logger():
                                
    #檢查目錄是否存在
    check_or_create_folder(error_log_folder)
                               
    #log config
    formatter = logging.Formatter(fmt = '%(asctime)s - %(levelname)s - %(message)s', 
                                    datefmt = '%Y/%m/%d %H:%M:%S %z' )
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # #error file handler
    errorFileHandler = logging.FileHandler(dir_path + error_log_folder + '/' + filename, 'a', 'utf-8')
    errorFileHandler.setFormatter(formatter)
    errorFileHandler.setLevel(logging.ERROR)
    logger.addHandler(errorFileHandler)

    # #console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    consoleHandler.setLevel(logging.ERROR)
    logger.addHandler(consoleHandler)
    
    return logger

def close_handler(logger):
    handlers = logger.handlers
    
    for handler in handlers:
            handler.close()

def check_or_create_folder(log_folder):
  
    #如果目錄不存，則建新的
    if not os.path.exists(dir_path + log_folder):
        os.makedirs(dir_path + log_folder)
