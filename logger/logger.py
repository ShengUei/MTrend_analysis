from datetime import datetime, timezone
import logging
import os

#設定 logs 目錄
dir_path = './logger/logs/'

#設定 log 資料夾
info_log_folder = 'info_log/'
error_log_folder = 'error_log/'

#設定檔名
filename = "{:%Y-%m-%d}".format(datetime.now(timezone.utc)) + '.log'

def get_logger():
                                
    #檢查目錄是否存在
    check_or_create_folder(info_log_folder)
    check_or_create_folder(error_log_folder)
                                
    #log config
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y/%m/%d %H:%M:%s %z')
    logger = logging.getLogger()
   
    #info file handler
    infoFileHandler = logging.FileHandler(dir_path + info_log_folder + '/' + filename, 'a', 'utf-8')
    infoFileHandler.setFormatter(formatter)
    infoFileHandler.setLevel(logging.INFO)                          
    logger.addHandler(infoFileHandler)   
    
    #error file handler
    errorFileHandler = logging.FileHandler(dir_path + error_log_folder + '/' + filename, 'a', 'utf-8')
    errorFileHandler.setFormatter(formatter)
    errorFileHandler.setLevel(logging.ERROR)
    logger.addHandler(errorFileHandler)

    #console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    consoleHandler.setLevel(logging.ERROR)
    logger.addHandler(consoleHandler)

    return logger

def check_or_create_folder(log_folder):
  
    #如果目錄不存，則建新的
    if not os.path.exists(dir_path + log_folder):
        os.makedirs(dir_path + log_folder)
