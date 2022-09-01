import threading
import os
from datetime import datetime, timezone, timedelta

#設定目錄
dir_path = '/home'

#設定資料夾
pid_folder = '/pid'


def show_pid():
    pid = threading.get_native_id()
    filename = 'pid_output.txt'

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    #如果目錄不存，則建新的
    if not os.path.exists(dir_path + pid_folder):
        os.makedirs(dir_path + pid_folder)

    #設定檔名
    filename = "{:%Y-%m-%d}".format(now) + '.txt'

    f = open(dir_path + pid_folder + '/' + filename, 'a')
    f.write('PID: %s at %s \n' % (pid, local_datetime.strftime('%Y/%m/%d %H:%M:%S')))
    f.close()