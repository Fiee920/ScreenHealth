# **ScreenHealth 2.1**

Only For Windows

仅Windows可用

所有Python模块下载到同一目录，需要的库安装齐全情况下可运行，或直接下载ScreenHealth2.0release.exe（若有报毒请忽略） All Python modules can be downloaded to the same directory and run when the required libraries are fully installed, or directly download screenhealth2.0release exe

点击下载V2.0==> https://wwi.lanzoup.com/idPlP075z7fa  <==touch to download(2.0release)

点击下载V2.1==> None (打包版本有bug下次打包修复（2.2）)  <==touch to download(2.1release)


<img src="http://i.miaosu.bid/data/f_83699723.jpg" alt="jK5wzF.png" alt="image1" style="zoom:5%;" />

✅功能 | function

记录各个**前台窗口**应用使用的时长，将当日屏幕时间前10以图表方式查看，支持当日数据统计和往日数据查看（注意：生成的记录信息存储在应用目录下的data文件中，删除会导致数据清除！）

Record the duration of each **foreground window** application, view the top 10 screen times of the current day in the form of charts, and support the current day data statistics and previous days data viewing (Note: the generated record information is stored in the data file under the application directory, and deleting it will cause the data to be cleared!)

⛔已知问题 | Bugs

#Windows休眠后，采集进程会被终止，休眠结束后，目前版本需手动重启软件重新打开进程以继续

#部分显示器分辨率未适配，可能有显示不协调/组件异常

#图表无法自刷新，需要手动点击按钮

#多个应用程序名字过长时导致图表x轴显示重叠

#弹窗提示/阻止，在部分情况下逻辑问题

#After windows hibernates, the collection process will be terminated. After hibernation, the current version needs to manually restart the software and reopen the process to continue
#The resolution of some monitors is not adapted, and the display may be uncoordinated / abnormal components
#The chart cannot be self refreshed. You need to click the button manually
#When the names of multiple applications are too long, the x-axis display of the chart overlaps
#Pop up prompt / block, logic problem in some cases

✅使它更适合你的显示器 | Make it more suitable for your monitor

#ttkboostrap与自带的tkinter不同，其geometry函数控制的窗口大小为屏幕绝对分辨率值

#Ttkboostrap is different from its own Tkinter. The window size controlled by its geometry function is the absolute resolution of the screen

```python

def Screen_Size_Fix(index1, index2):
    global DPI, scaling_index, size
    if index1 == 3456 and index2 == 2160:
        VAR.size = str(int(index1 * 0.7)) + 'x' + str(int(index2 * 0.4)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 180
        VAR.scaling_index = 7
    elif index1 == 2560 and index2 == 1440:
        VAR.size = str(int(index1 * 0.7)) + 'x' + str(int(index2 * 0.4)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 130
        VAR.scaling_index = 4
    elif index1 == 1920 and index2 == 1440:
        VAR.size = str(int(index1 * 0.7)) + 'x' + str(int(index2 * 0.4)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 100
        VAR.scaling_index = 3
    elif index1 == 1920 and index2 == 1080:
        VAR.size = str(int(index1 * 0.7)) + 'x' + str(int(index2 * 0.43)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 100
        VAR.scaling_index = 2.5
    return VAR.DPI
```

root.geometry()参数需要使用一个格式为“分辨率长x分辨率宽+距离屏幕左侧的x轴坐标(绝对分辨率)+距离屏幕顶端的y轴坐标(绝对分辨率)”的字符串【注意：x而不是*】

root.geometry() parameter needs to use a string in the format of "resolution length x resolution width + X-axis coordinate from the left side of the screen (absolute resolution) + Y-axis coordinate from the top of the screen (absolute resolution)" [Note: X instead of *]

在Screen.py中提供Screen_Size_Fix函数，index1==>屏幕绝对分辨率长度，index2==>屏幕绝对分辨率宽度，DPI==>绘图DPI（数值越大图像越大），scaling_index==>窗口缩放比例（数值越大GUI窗口越大）

On screen PY_ Size_ Fix function, index1==> screen absolute resolution length, index2==> screen absolute resolution width, dpi==> drawing DPI (the larger the value, the larger the image), scaling_ Index==> window zoom ratio (the larger the value, the larger the GUI window)

```python
VAR.size = str(int(W * 0.55)) + 'x' + str(int(H * 0.5)) + '+' + str(int(W * 0.25)) + '+' + str(int(H * 0.25))
```

主程序GUI.py 200行，设置窗口大小，参数'W'为长度，参数'H'为宽度

Main program GUI.py line 200. Set the window size. The index 'w'is the length and the index 'H' is the width

✅图表配色 | Chart color matching

==>Draw.py==>line25

```python
color_use = ['palegreen', 'tomato', 'sandybrown', 'darkseagreen', 'paleturquoise', 'lightsteelblue', 'lightgreen',
             'skyblue', 'bisque', 'lightcoral']
```

遵循plt颜色规则  Follow PLT color rules

<img src="https://s1.ax1x.com/2022/06/30/jK5BM4.png" alt="image-20220630172911066" style="zoom: 33%;" />

🍳主题更换 | Themes

参考：https://ttkbootstrap.readthedocs.io/en/latest/

  深色模式 | DarkMode
  
图表配色：#333333

🍳计时逻辑 | Timing logic

==>AppTime.py==>AppTime

按秒计时：参数传入应用程序名称，在字典中现有的元素则累加1，若无则创建新键，实时文件存储，防止数据丢失

Time by second: the parameter is passed into the application name, and the existing elements in the dictionary are accumulated by 1. If none, a new key is created, and the real-time file is stored to prevent data loss

```python
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
```

🍳多进程 | Multiprocess

mp1为采集子进程，指向demo.py中main()函数   mp1 is a collection subprocess, pointing to main() function in demo.py. 

```python
mp1 = multiprocessing.Process(target=demo.main, args=(VAR.DPI,))
```

suspend()和resume()函数用于采集进程的暂停与恢复    The suspend() and resume() functions are used to pause and resume the collection process

```python
multiprocessing.freeze_support()
```

使用Pyinstaller打包多进程脚本，使用上述代码防止exe循环开启导致崩溃   Use pyinstaller to package multi process scripts, and use the above code to prevent the EXE cycle from starting and causing a crash

🍳用户图形界面 | GUI

图表图片须用全局变量，否则会被吞掉

ttkboostrap库美化

除日总时长采用绝对布局外，在2.0beta3之后的版本中采用pack()布局更好作分辨率适配

Chart pictures must use global variables, or they will be swallowed.
Ttkboostrap library beautification.
In addition to the absolute layout for daily total duration, the package () layout is better used for resolution adaptation in versions after 2.0beta3 release.

<img src="https://s1.ax1x.com/2022/06/30/jK5dRU.png" alt="image-20220630182311064" style="zoom: 33%;" />

✅异常处理 | Exception

```python
while True:
    try:
       ·····
       ····· #此处省略 Omitted here
    except:
        time.sleep(1)
        main(DPI)
```

静默处理，不抛出，在Draw()函数报错后睡眠1秒，回调至main()函数继续执行

Silent processing, no throw, sleep for 1 second after the Draw() function reports an error, and call back to the main() function to continue execution.

✅全局变量 | global variable

调取自VAR.py，附有默认值

Retrieved from var.py with default value

✅使用到的库 | Libraries used

os , multiprocessing , win32(win32gui) , win32process , time , datetime , psutil , matplotlib.pyplot , tkinter , ttkboostrap , PIL , win32print , win32con

💹更新日志 | Update logs

> ```
> # 更新日志：            
> *1.1 Release:
> ==>GUI
> 
> *1.2 Release:
> ==>在文件目录下创建data文件用于存储数据
> ==>修复在未开启采集进程时终止报错的bug
> ==>在生成时长文件时对时长绘图保存
> ==>图片内嵌到GUI内，取消弹窗
> 
> *1.3 Release：
> ==>修复前序版本中采集进程频繁报错问题
> ==>图片刷新方法变更
> ==>删除冗余代码
> 
> *2.0 Release：
> ==>支持分辨率与绘图DPI适应（目前支持分辨率：3456*2160 2560*1440 1920*1440 1920*1080）
> ==>GUI界面美化，添加点击提示，同时弃用网格布局，新的布局方式以更好进行分辨率适应
> ==>数据以日期形式保存，当日可累加，支持对历史单日数据的查看
> ==>支持采集进程的暂停/继续以及终止（终止后不能再打开！）
> ==>修复了运行一段时间后RAM爆满崩溃的问题
> ==>逻辑改为按秒计时按分绘图，结果更准确
> ==>图表仅显示排名前10的应用
> ==>图表标题变为对应日期
> ==>添加日总时长
> ==>新增应用图标

*2.1 Release：
==>新增DarkMode(深色模式)
==>支持查看过去一周统计
==>优化3456*2160|1920*1080窗口
> ```

