import socket
import sys
import time
import keyboard
import os
import gc
import multiprocessing

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal


def fast_sort(arr: list):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    left = []
    right = []
    key = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= key:
            right.append(arr[i])
        if arr[i] < key:
            left.append(arr[i])
    return fast_sort(left) + [key] + fast_sort(right)


def get_cwd():
    a = os.getcwd()
    b = a.split("\\")
    c = ''
    for i in range(len(b)):
        c += b[i]
        if not i == len(b)-1:
            c += "/"
    return c


def gc_Close(self):
    try:
        self.close()
    except:
        pass
    try:
        del self
        gc.collect()
    except:
        pass


def connect_3(yuming, port):
    socket.setdefaulttimeout(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(((yuming, port)))
        s.sendall("loading".encode("GB2312"))
        data = s.recv(1024).decode("gb2312")
        s.close()
        if data == "on":
            socket.setdefaulttimeout(None)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(((yuming, port)))
            start = time.time()
            s.sendall("loading".encode("GB2312"))
            s.recv(1024)
            end = time.time()
            return s, end-start
        else:
            return False, False
    except:
        s.close()
        return False, False


def connect_fast(addr: str, port: int):
    global yanchi,yanchi2
    s, yan = connect_3(addr, port)
    yanchi2.append((s, yan))
    if not yan == False:
        yanchi.append(yan)
    #     print(addr,round(yan*1000),"ms")
    # if yan == False:
    #     print(addr,False)


def closes(yanchis, j):
    for i in range(len(yanchis)):
        if not i == j:
            try:
                yanchis[i][0].close()
            except:
                pass


def connect_2(Port):
    global yanchi, yanchi2
    yanchi = []
    yanchi2 = []

    connect_fast("1cdn.hcolda.com", Port)
    connect_fast("2cdn.hcolda.com", Port)
    connect_fast("3cdn.hcolda.com", Port)

    sock = False
    if not len(yanchi) == 0:
        fast = fast_sort(yanchi)
        for j in range(len(yanchi2)):
            if fast[0] == yanchi2[j][1]:
                sock = yanchi2[j][0]
                multiprocessing.Process(target=closes, args=(yanchi2, j)).start()

    return sock


def connect(Port):
    return connect_2(Port)


def command(self, msg):
    lit = msg.split("：")

    if lit[0] == "tip":
        QMessageBox.critical(self, "警告", lit[1], QMessageBox.Ok)
        sys.exit()

    elif lit[0] == "message":
        QMessageBox.warning(self, "警告", lit[1]+"："+lit[2], QMessageBox.Ok)
        return 0

    elif lit[0] == "login_no":
        QMessageBox.warning(self, "警告", lit[1], QMessageBox.Ok)
        return 0

    return 1


def command_no_self(msg):
    lit = msg.split("：")

    if lit[0] == "tip":
        sys.exit()

    elif lit[0] == "message":
        return 0

    elif lit[0] == "login_no":
        return 0

    return 1


def msg_command(msg):
    lit = msg.split("：")

    if lit[0] == "chatting_server":
        if lit[1] == "public":
            return 1

    return 0


def css_load(name):
    with open(name, "r", encoding="utf-8") as f:
        return f.read()


class changlabel(QThread):
    def __init__(self, label, msg):
        super().__init__()
        self.label = label
        self.msg = msg

    def run(self):
        Time = 0
        while True:
            try:
                self.label.setStyleSheet("color:Black")
                self.label.setText("{a}{b}".format(
                    a=self.msg, b="."*(Time % 4)))
                Time += 1
                time.sleep(0.5)
            except:
                break


class press(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super(press, self).__init__()
        self.work = True

    def no(self):
        self.work = False
        self.wait()

    def run(self):
        keyboard.add_hotkey('ctrl + enter', self.st)

    def st(self):
        if self.work == True:
            self.signal.emit("1")
        else:
            self.wait()
