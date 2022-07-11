from datetime import datetime
from datetime import timedelta
import os

import Draw
import VAR

dic = VAR.dic
week_dic = {}


def LastWeek():
    global week_dic
    week_days = []
    today = datetime.now()
    for days in range(0, 7):
        offset = timedelta(days=(-1) * days)
        re_date = (today + offset).strftime('%Y-%m-%d')
        week_days.append(re_date)
    for day in week_days:
        backup_path = r'./data/' + day + r'_backup.txt'
        if os.path.exists(backup_path):
            f = open(backup_path, 'r')
            a = f.read()
            dic = eval(a)
            sum = 0
            for values in dic.values():
                sum = sum + values
            sum = round((sum / 60), 2)
            week_dic[day] = sum
        else:
            week_dic[day] = 0
    week_dic = {'2022-07-09': 13, '2022-07-08': 69.0, '2022-07-07': 34.5, '2022-07-06': 77.3, '2022-07-05': 60, '2022-07-04': 97.2, '2022-07-03': 33.3}
    Draw.Draw_plus(week_dic, VAR.DPI, mode=1)
