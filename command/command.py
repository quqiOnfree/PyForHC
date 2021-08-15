import socket
import sys
import time
import keyboard
import os
import gc

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal


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
            s.sendall("loading".encode("GB2312"))
            s.recv(1024)
            return s
        else:
            return False
    except:
        s.close()
        return False


def connect_2(Port):
    start1 = time.time()
    s = connect_3("1cdnhcolda.com", Port)
    end1 = time.time()
    start2 = time.time()
    s2 = connect_3("2cdn.hcolda.com", Port)
    end2 = time.time()

    if s == False:
        s = connect_3("1cdn.hcolda.com", Port)

    if s2 == False:
        s2 = connect_3("2cdn.hcolda.com", Port)

    if s == False and s2 == False:
        return False
    elif s == False:
        return s2
    elif s2 == False:
        return s
    else:
        yan = end1-start1
        yan2 = end2-start2
        if yan >= yan2:
            return s2
        else:
            return s


def connect(Port):
    return connect_2(Port)


def command(self, msg):
    lit = msg.split("：")

    if lit[0] == "tip":
        QMessageBox.warning(self, "警告", lit[1], QMessageBox.Ok)
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
