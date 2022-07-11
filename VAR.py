from datetime import datetime
import os


c1 = 0
dic = {}
now = datetime.now()
today = now.strftime("%Y-%m-%d %H:%M:%S")[:10]
backup_path = r'./data/' + today + r'_backup.txt'

if os.path.exists(".\data\settings.txt"):
    list1 = []
    with open('.\data\settings.txt', 'r') as f:
        for line in f:
            list1.append(line)
        c1 = list1[0].strip()
        f.close()

def start():
    global dic, c1
    folder_path = ".\data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if not os.path.exists(".\data\settings.txt"):
        f = open(".\data\settings.txt", 'w')
        f.write('0')
        f.close()

    if os.path.exists(backup_path):
        f = open(backup_path, 'r')
        a = f.read()
        dic = eval(a)
        f.close()
    return True


num1 = 0
img_png = None
DPI = 100
size = "950x550+450+370"
scaling_index = 3
darkmode = c1
