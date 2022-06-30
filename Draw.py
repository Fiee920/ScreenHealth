from datetime import datetime
from matplotlib import pyplot as plt
import VAR

dic = VAR.dic
DPI = VAR.DPI

def Draw(dic, DPI, ntime='None'):
    global W, H
    if ntime == 'None':
        now1 = datetime.now()
        title = now1.strftime("%Y-%m-%d %H:%M:%S")[:10]
    else:
        title = ntime
    newdic_ = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    newdic = {}
    if len(newdic_) <= 10:
        for i in newdic_:
            newdic[i[0]] = i[1]
    if len(newdic_) > 10:
        for i in range(10):
            newdic[i[0]] = i[1]
    x_data = []
    y_data = []
    color_use = ['palegreen', 'tomato', 'sandybrown', 'darkseagreen', 'paleturquoise', 'lightsteelblue', 'lightgreen',
                 'skyblue', 'bisque', 'lightcoral']
    for key in newdic:
        x_data.append(key)
    for value in newdic.values():
        value = round((value / 60), 2)
        y_data.append(value)
    plt.figure(dpi=DPI, figsize=(10, 4))
    plt.xticks(fontsize=12)

    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    for i in range(len(x_data)):
        p1 = plt.bar(x_data[i], y_data[i], color=color_use[i])
        plt.bar_label(p1, label_type='edge')
    plt.title(title)
    plt.xlabel("应用程序")
    plt.ylabel("分钟")
    plt.savefig('.\data\Pic.jpg')
    plt.close()


def ToDraw(DPI):
    global dic
    now = datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")[:10]
    backup_path = r'./data/' + today + r'_backup.txt'
    f = open(backup_path, 'r')
    a = f.read()
    dic = eval(a)
    f.close()
    Draw(dic, DPI)
