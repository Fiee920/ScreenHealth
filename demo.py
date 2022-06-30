from datetime import datetime
from win32 import win32gui
import win32process
import psutil
import time
import os

import AppTime
import Draw
import VAR

dic = VAR.dic
DPI = VAR.DPI


def main(DPI):
    global dic
    while True:
        try:
            now = datetime.now()
            today = now.strftime("%Y-%m-%d %H:%M:%S")[:10]
            backup_path = r'./data/' + today + r'_backup.txt'

            if os.path.exists(backup_path):
                f = open(backup_path, 'r')
                a = f.read()
                dic = eval(a)

            Title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            AppID, ProcessID = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
            ProcessName = psutil.Process(ProcessID)
            AppName = ProcessName.name()
            AppName = AppName[:-4].title()
            AppTime.AppTime(AppName)
            Draw.ToDraw(DPI)
            time.sleep(1)
        except:
            time.sleep(1)
            main(DPI)
