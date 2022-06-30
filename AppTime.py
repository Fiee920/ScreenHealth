from datetime import datetime
import VAR

dic = VAR.dic

def AppTime(appname):
    global dic

    now = datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")[:10]
    backup_path = r'./data/' + today + r'_backup.txt'

    if appname in dic.keys():
        dic[appname] = dic[appname] + 1
    else:
        dic[appname] = 1

    f = open(backup_path, 'w')
    f.write(str(dic))
    f.close()