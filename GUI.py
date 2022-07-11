from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from datetime import datetime
from ttkbootstrap import Style
import tkinter.messagebox
import multiprocessing
import ttkbootstrap
import tkinter
import psutil
import os

import demo
import Draw
import Screen
import VAR
import week


class Application(tkinter.Frame):
    now = datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")[:10]

    def sum_time(self, ndate=today):
        sum = 0
        backup_path = r'./data/' + ndate + r'_backup.txt'

        if os.path.exists(backup_path):
            f = open(backup_path, 'r')
            a = f.read()
            temp_dic = eval(a)
            for each in temp_dic.values():
                sum = sum + each
            sum = round((sum / 60), 2)
            return sum
        else:
            return 0

    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.pack()
        self.Win()

    def Win(self):
        global img_png, DPI, frame, date1
        v = ttkbootstrap.IntVar()
        v.set(int(VAR.darkmode))
        frame = ttkbootstrap.Frame()
        if VAR.darkmode == '1':
            ttkbootstrap.Label(frame, text="ScreenHealth", bootstyle='light').pack(side=TOP, anchor=CENTER)
        else:
            ttkbootstrap.Label(frame, text="ScreenHealth", bootstyle='dark').pack(side=TOP, anchor=CENTER)
        dic1 = {}
        Draw.Draw(dic1, VAR.DPI)
        img_open = Image.open(".\data\Pic.jpg")
        VAR.img_png = ImageTk.PhotoImage(img_open)
        label_img = ttkbootstrap.Label(frame, image=VAR.img_png)
        label_img.pack(side=RIGHT)
        self.update_idletasks()
        ttkbootstrap.Button(frame, text="启动屏幕时间采集", style='success.TButton', command=lambda: self.click(1),
                            width=20).pack(side=TOP, anchor=N, fill=X)
        ttkbootstrap.Button(frame, style='danger', text="终止采集", command=lambda: self.click(2)).pack(side=TOP, anchor=N,
                                                                                                    fill=X)
        ttkbootstrap.Button(frame, style='success.Outline.TButton', text="采集暂停/继续", command=lambda: self.click(3)).pack(
            side=TOP, anchor=N, fill=X)
        ttkbootstrap.Button(frame, text="刷新今日图表", style='primary', command=lambda: self.reDraw()).pack(side=TOP,
                                                                                                       anchor=N, fill=X)
        date1 = ttkbootstrap.DateEntry(frame)
        date1.pack()
        ttkbootstrap.Button(frame, text="刷新该日图表", style='info', command=lambda: self.ToreDraw()).pack(side=TOP,
                                                                                                      anchor=S, fill=X)
        ttkbootstrap.Button(frame, text="7日统计", style='info.Outline.TButton', command=lambda: self.weekDraw()).pack(
            side=TOP, anchor=N, fill=X)
        ttkbootstrap.Button(frame, text="版本信息", style='warning.Outline', command=lambda: self.click(5)).pack(side=TOP,
                                                                                                             anchor=N,
                                                                                                             fill=X)
        ttkbootstrap.Checkbutton(frame, text='深色模式', variable=v, bootstyle="success-round-toggle",
                                 command=lambda: self.setDarkMode()).pack(side=TOP, anchor=N, fill=X)
        ttkbootstrap.Label(frame, text="日总时长：{} 分钟".format(self.sum_time()), font=('宋体', 6)).place(relx=0.7, rely=0.2)
        frame.pack()

    def weekDraw(self):
        week.LastWeek()
        self.reDraw(mode=1)

    def ToreDraw(self):
        date1_ = str(date1.entry.get())
        i = date1_.index('/')
        year = date1_[:i]
        j = date1_.rindex('/')
        month = date1_[i + 1:j]
        day = date1_[j + 1:]
        date1_ = '{0}-{1:0>2s}-{2:0>2s}'.format(year, month, day)
        self.reDraw(ndate=date1_)

    def reDraw(self, ndate=today, mode=0):
        global frame, date1, num1
        v = ttkbootstrap.IntVar()
        v.set(int(VAR.darkmode))
        if mode == 0:
            backup_path = r'./data/' + str(ndate) + r'_backup.txt'
            if os.path.exists(backup_path):
                f = open(backup_path, 'r')
                cc = f.read()
                newDic = eval(cc)
                Draw.Draw(newDic, VAR.DPI, ndate)
                VAR.num1 = 1
            else:
                tkinter.messagebox.showinfo(title='提示', message="错误：无该日数据记录")
        if mode == 1:
            pass

        if VAR.num1 != 0 or mode == 1:
            frame.destroy()
            frame = ttkbootstrap.Frame()
            if VAR.darkmode == '1':
                ttkbootstrap.Label(frame, text="ScreenHealth", bootstyle='light').pack(side=TOP, anchor=CENTER)
            else:
                ttkbootstrap.Label(frame, text="ScreenHealth", bootstyle='dark').pack(side=TOP, anchor=CENTER)
            global img_png
            img_open = Image.open(".\data\Pic.jpg")
            VAR.img_png = ImageTk.PhotoImage(img_open)
            label_img = ttkbootstrap.Label(frame, image=VAR.img_png)
            label_img.pack(side=RIGHT)
            ttkbootstrap.Button(frame, text="启动屏幕时间采集", style='success.TButton', command=lambda: self.click(1),
                                width=20).pack(side=TOP, anchor=N, fill=X)
            ttkbootstrap.Button(frame, style='danger', text="终止采集", command=lambda: self.click(2)).pack(side=TOP,
                                                                                                        anchor=N,
                                                                                                        fill=X)
            ttkbootstrap.Button(frame, style='success.Outline.TButton', text="采集暂停/继续",
                                command=lambda: self.click(3)).pack(side=TOP, anchor=N, fill=X)
            ttkbootstrap.Button(frame, text="刷新今日图表", style='primary', command=lambda: self.reDraw()).pack(side=TOP,
                                                                                                           anchor=N,
                                                                                                           fill=X)

            date1 = ttkbootstrap.DateEntry(frame)
            date1.pack()
            ttkbootstrap.Button(frame, text="刷新该日图表", style='info', command=lambda: self.ToreDraw()).pack(side=TOP,
                                                                                                          anchor=S,
                                                                                                          fill=X)
            ttkbootstrap.Button(frame, text="7日统计", style='info.Outline.TButton', command=lambda: self.weekDraw()).pack(
                side=TOP, anchor=N, fill=X)
            ttkbootstrap.Button(frame, text="版本信息", style='warning.Outline', command=lambda: self.click(5)).pack(
                side=TOP, anchor=N, fill=X)
            ttkbootstrap.Checkbutton(frame, text='深色模式', variable=v, bootstyle="success-round-toggle",
                                     command=lambda: self.setDarkMode()).pack(side=TOP, anchor=N, fill=X)
            if mode == 0:
                if ndate != self.__class__.today:
                    ttkbootstrap.Label(frame, text="日总时长：{} 分钟".format(self.sum_time(ndate=ndate)),
                                       font=('宋体', 6)).place(relx=0.7, rely=0.2)
                else:
                    ttkbootstrap.Label(frame, text="日总时长：{} 分钟".format(self.sum_time()), font=('宋体', 6)).place(relx=0.7,
                                                                                                               rely=0.2)
            frame.pack()
        else:
            tkinter.messagebox.showinfo(title='提示', message="今日暂无采集记录，刷新图片前请开启时间管理采集")
            VAR.num1 = 0

    def setDarkMode(self):
        if VAR.darkmode == '1':
            f = open(".\data\settings.txt", 'w')
            f.write('0')
            f.close()
        else:
            f = open(".\data\settings.txt", 'w')
            f.write('1')
            f.close()
        tkinter.messagebox.showinfo(title='提示', message="主题已变更，手动重启软件立即生效")

    def click(self, num):
        global num1, W, H
        if num == 1:
            mp1.start()
            VAR.num1 = 1
        if num == 2:
            if VAR.num1 != 0:
                mp1.terminate()
                VAR.num1 = 0
                tkinter.messagebox.showinfo(title='提示', message="采集进程已终止，当前版本无法再次直接启用！如需启用，请退出后重新打开应用！")
            else:
                tkinter.messagebox.showinfo(title='提示', message="错误：无法终止采集进程（您还未开启时间管理采集进程）")
        if num == 3:
            if VAR.num1 != 0:
                VAR.num1 = VAR.num1 + 1
                pid = mp1.pid
                pause = psutil.Process(pid)
                if VAR.num1 % 2 == 0:
                    pause.suspend()
                    tkinter.messagebox.showinfo(title='提示', message="采集进程已暂停")
                else:
                    pause.resume()
                    tkinter.messagebox.showinfo(title='提示', message="采集进程已开始")
            else:
                tkinter.messagebox.showinfo(title='提示', message="还未开启采集，无法操作此项")
        if num == 4:
            global img_png
            img_open = Image.open(".\data\Pic.jpg")
            VAR.img_png = ImageTk.PhotoImage(img_open)
            label_img = ttkbootstrap.Label(self, image=img_png)
            label_img.pack(side=RIGHT)
        self.update_idletasks()
        if num == 5:
            message = """
# Author：Fiee920
# Version：2.0
# E-Mail: zfw0920@163.com

# 注意：删除软件目录下的data文件会导致记录数据丢失！

# 已知问题：
*电脑休眠后，采集进程会被杀掉，只能在手动重启软件恢复（可尝试在Windows休眠前手动暂停）
*部分显示器分辨率未适配导致显示不协调或组件异常
*应用名太长且过多时图表x轴文字重叠
*图表无法自动刷新，需手动            

# 更新日志：            
*1.1 Release:
==>GUI支持

*1.2 Release:
==>在文件目录下创建data文件用于存储数据
==>修复在未开启采集进程时终止报错的bug
==>在生成时长文件时对时长绘图保存
==>图片内嵌到GUI内，取消弹窗

*1.3 Release：
==>修复前序版本中采集进程频繁报错问题
==>图片刷新方法变更
==>删除冗余代码

*2.0 Release：
==>支持分辨率与绘图DPI适应（目前支持分辨率：3456*2160 2560*1440 1920*1440 1920*1080）
==>GUI界面美化，添加点击提示，同时弃用网格布局，新的布局方式以更好进行分辨率适应
==>数据以日期形式保存，当日可累加，支持对历史单日数据的查看
==>支持采集进程的暂停/继续以及终止（终止后不能再打开！）
==>修复了运行一段时间后RAM爆满崩溃的问题
==>逻辑改为按秒计时按分绘图，结果更准确
==>图表仅显示排名前10的应用
==>图表标题变为对应日期
==>添加日总时长
==>新增应用图标

*2.1 Release：
==>新增DarkMode(深色模式)
==>支持查看过去一周统计
==>优化3456*2160|1920*1080窗口
            """
            result = tkinter.messagebox.showinfo(title='版本说明', message=message)


if __name__ == '__main__':

    multiprocessing.freeze_support()

    if VAR.start():
        W, H = Screen.get_screen_size()
        VAR.size = str(int(W * 0.55)) + 'x' + str(int(H * 0.5)) + '+' + str(int(W * 0.25)) + '+' + str(int(H * 0.25))
        VAR.DPI = Screen.Screen_Size_Fix(W, H)
        mp1 = multiprocessing.Process(target=demo.main, args=(VAR.DPI,))
        root = ttkbootstrap.Window(scaling=VAR.scaling_index)
        if VAR.darkmode == '1':
            style = Style(theme='darkly')
        else:
            style = Style(theme='litera')
        root = style.master
        root.title("Screen Health")
        root.geometry(VAR.size)
        application = Application(root=root)
        print(VAR.darkmode)
        application.mainloop()
