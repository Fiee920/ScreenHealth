from win32 import win32gui
import win32print
import win32con

import VAR


def getindex1index2(w,h):
    global W,H
    W=w
    H=h

def get_screen_size():
    hDC = win32gui.GetDC(0)
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def Screen_Size_Fix(index1, index2):
    global DPI, scaling_index, size
    if index1 == 3456 and index2 == 2160:
        VAR.size = str(int(index1 * 0.75)) + 'x' + str(int(index2 * 0.42)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 180
        VAR.scaling_index = 6
    elif index1 == 2560 and index2 == 1440:
        VAR.size = str(int(index1 * 0.7)) + 'x' + str(int(index2 * 0.4)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 130
        VAR.scaling_index = 4
    elif index1 == 1920 and index2 == 1440:
        VAR.size = str(int(index1 * 0.7)) + 'x' + str(int(index2 * 0.4)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 100
        VAR.scaling_index = 3
    elif index1 == 1920 and index2 == 1080:
        VAR.size = str(int(index1 * 0.7)) + 'x' + str(int(index2 * 0.4)) + '+' + str(int(index1 * 0.2)) + '+' + str(int(index2 * 0.25))
        VAR.DPI = 100
        VAR.scaling_index = 2.5
    return VAR.DPI