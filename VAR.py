from datetime import datetime
import os

now = datetime.now()
today = now.strftime("%Y-%m-%d %H:%M:%S")[:10]
backup_path = r'./data/' + today + r'_backup.txt'
if os.path.exists(backup_path):
    f = open(backup_path, 'r')
    a = f.read()
    dic = eval(a)


num1 = 0
img_png = None
DPI = 100
size = "950x550+450+370"
scaling_index = 3