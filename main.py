import datetime
import sys
import os
import shutil
import time
import datetime
import filecmp



arg = sys.argv
source_path = arg[1]
copy_path = arg[2]
sync_period = sys.argv[3]


def cr_dirs(source, copy):
    check = filecmp.cmp(source, copy)
    if check == False:
        #shutil.copytree(source, copy, dirs_exist_ok=True)
        shutil.rmtree(copy)
        shutil.copytree(source, copy)
    elif check == True:
        None


def log_file(file_path, date):
    log_file_path = os.path.join(file_path, 'log.txt')
    try:
        if os.path.exists(log_file_path):
            method = 'a'
        else:
            method = 'w'
    except:
        None
    with open(log_file_path, method) as file:
            file.write(f"{date} - Change detected, synchronization performed.\n")

def periods(sync_interval):
    time.sleep(sync_interval)

while True:
    log_file(source_path, datetime.datetime.now())
    cr_dirs(source_path, copy_path)
    periods(int(sync_period))

