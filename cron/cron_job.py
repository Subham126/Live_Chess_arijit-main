from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
import shutil
from pathlib import Path
import re

def do(loc, file_name, file_src):
    path = Path(os.path.dirname(os.path.abspath(__file__)))
    # print(sid.__dict__)
    # for x in iter(sid.listFreqs()):
    #     print(x)
    # temp = re.compile("([a-zA-Z]+)([0-9]+)")
    # res = temp.match(file_src).groups()
    # name = file_src[:-5]
    # name = name + str(sid) + ".pgn"
    copy_file_loc = str(path.parent) + "\media\documents\\" + file_src
    if os.path.exists(copy_file_loc):
        shutil.copy(copy_file_loc, loc)
        src = loc + "\\" + file_src
        des = loc + "\\" + file_name + ".pgn"
        if os.path.exists(des):
            os.remove(des)
        os.rename(src, des)

def start(loc, file_name, file_src):
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: do(loc, file_name, file_src), 'interval', seconds=20, id="file_upload")
    scheduler.start()