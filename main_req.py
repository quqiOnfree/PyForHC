import json
import socket
import sys
import webbrowser
import random
import gc
import time
import ctypes
import os
import json5

from PyQt5 import sip
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QMessageBox, QWidget, QFontComboBox, QSystemTrayIcon, QAction, QMenu, QListView
from PyQt5.QtCore import QThread, Qt, pyqtSignal, QAbstractListModel, QVariant, QSize, QRect

import command
from ui import Ui_reg, Ui_update, Ui_ver, Ui_announcement, Ui_Login, Ui_tellroom_2


def init():
    global open_receive, img, str_version, int_version, update, must_update, can_update, update_data, cant, cant_connect, public_msg, receive_msg, receive_msg_num, unreceive, unpublic, exe_name, s, public_msg_2, load_rsa_key, username, password, connect
    global official_address  # 官网地址变量
    global comm_dll
    global __version__
    global chat_msg
    # 全局变量
    open_receive = 0
    img = "./library/imgs/image.png"  # 软件图标
    exe_name = "氢冷HC"  # 软件名称
    official_address = "https://hcteam.top/"  # 官网地址变量

    load_rsa_key = 0

    __version__ = "1.0.0.0"
    str_version = "1.0.0.0"  # 文字版本号
    int_version = 0  # 数字版本号
    # 版本号，需与服务端统一
    update = 0
    must_update = 0
    can_update = 0
    update_data = 0

    username = ""
    password = ""

    connect = 0

    cant = 0
    cant_connect = 0

    chat_msgs = {}
    public_msg = []
    public_msg_2 = ""
    receive_msg = []
    receive_msg_num = 0
    unreceive = 0
    unpublic = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 连接初始化

    # 程序初始化
    comm_dll = ctypes.cdll.LoadLibrary("./library/dll/comm.dll")

    QFontDatabase.addApplicationFont("高端黑.ttf")
    QFontDatabase.addApplicationFont("快乐体.ttf")
    QFontDatabase.addApplicationFont("文艺体.ttf")

    try:
        os.mkdir("./library/datas")
    except:
        pass


def dell():
    global open_receive, img, str_version, int_version, update, must_update, can_update, update_data, cant, cant_connect, public_msg, receive_msg, receive_msg_num, unreceive, unpublic, exe_name, s, public_msg_2
    global official_address
    del open_receive, img, str_version, int_version, update, must_update, can_update, update_data, cant, cant_connect, public_msg, receive_msg, receive_msg_num, unreceive, unpublic, exe_name, official_address, public_msg_2


def receive_if():
    global unreceive
    while True:
        if unreceive == 1:
            try:
                msg = receive_msg[receive_msg_num]
                unreceive = 0
                break
            except:
                pass
    return msg


def update_command():
    global update, new_version_num, max_version_num, can_update, must_update

    if update == 0:
        global comm_dll
        s.sendall("edition".encode("GB2312"))
        version = receive_if()
        version2 = version.split("：")
        new_version = int(version2[1])
        max_version = int(version2[2])
        new_version_num = version2[3]
        max_version_num = version2[4]
        can_update = 0
        must_update = 0
        must_update = comm_dll.update_1(max_version, int_version, new_version)
        can_update = comm_dll.update_2(max_version, int_version, new_version)
        update = 1
        try:
            with open("./library/datas/update.json", "r") as f:
                global update_data
                update_data = json.load(f)[0]
        except:
            pass


class conn(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            global s, connect
            if connect == 0:
                s = command.connect(3000)
                if s == False or s == type(""):
                    self.signal.emit("1")
                else:
                    self.signal.emit("2")
                    connect = 1
                    return
                time.sleep(10)
                self.signal.emit("3")
            else:
                self.signal.emit("2")
                return


class moniter(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super(moniter, self).__init__()
        self.work = True

    def no(self):
        self.work = False

    def run(self):
        global unpublic
        while self.work == True:
            time.sleep(0.1)
            if unpublic == 1:
                self.signal.emit("1")
                unpublic = 0


class receive(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global receive_msg, public_msg, receive_msg_num, unreceive, unpublic
        while True:
            while True:
                try:
                    data = s.recv(1024).decode("GB2312")
                except:
                    return
                if open_receive == 1:
                    # print(s)
                    print(data)
                if not len(data):
                    break
                if command.msg_command(data) == 0:
                    lit = data.split("：")
                    if lit[0] == "chatting_server":  # 以后需要更改
                        pass

                    receive_msg.append(data)
                    receive_msg_num = len(receive_msg)-1
                    unreceive = 1
                elif command.msg_command(data) == 1:
                    public_msg.append(data)
                    unpublic = 1


class init_(QThread):
    signal = pyqtSignal(str)

    def __init__(self, label):
        super().__init__()
        self.label = label

    def run(self):
        self.label.setStyleSheet("color:Black")
        global public, private, load_rsa_key
        if load_rsa_key == 0:
            self.change = command.changlabel(self.label, "正在加载全局变量")
            self.change.start()
            init()
            self.change.terminate()
            self.change.wait()
            self.change = command.changlabel(self.label, "正在加载加密key")
            self.change.start()
            public, private = command.rsa_key(2048)
            self.change.terminate()
            self.change.wait()
            load_rsa_key = 1
            del self.change
            gc.collect()
        self.signal.emit("1")


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.createMenu()

    def createMenu(self):
        self.menu = QMenu()
        self.showAction1 = QAction("启动", self, triggered=self.show_window)
        self.quitAction = QAction("退出", self, triggered=self.quit)

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        self.setIcon(QIcon("./library/imgs/image_2.png"))
        self.icon = self.MessageIcon()

        self.activated.connect(self.onIconClicked)

    def show_window(self):
        global main_win
        main_win.setWindowFlags(Qt.Window)
        main_win.setWindowFlags(Qt.FramelessWindowHint)
        main_win.setAttribute(Qt.WA_TranslucentBackground)
        main_win.showNormal()
        main_win.activateWindow()
        self.show()

    def quit(self):
        sys.exit()

    def onIconClicked(self, reason):
        global main_win
        if reason == 2 or reason == 3:
            if main_win.isMinimized() or not main_win.isVisible():
                main_win.setWindowFlags(Qt.Window)
                main_win.setWindowFlags(Qt.FramelessWindowHint)
                main_win.setAttribute(Qt.WA_TranslucentBackground)
                main_win.showNormal()
                main_win.activateWindow()
                self.show()
            else:
                pass


class announ(QWidget, Ui_announcement):
    def __init__(self):
        super(announ, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(img))
        self.setWindowTitle("公告")
        self.fontComboBox.setFontFilters(QFontComboBox.AllFonts)
        self.fontComboBox.currentFontChanged(self.changefont)
        self.spinBox.valueChanged.connect(self.changefont)
        self.spinBox.setRange(1, 300, 1)
        self.spinBox.setValue(15)
        self.changefont()

    def changefont(self):
        # self.textBrowser.setFont(self.fontComboBox.currentFont())
        font = QFont()
        font.setFamily(self.fontComboBox.currentFont())
        font.setPointSize(self.spinBox.value())
        self.textBrowser.setFont(font)


class updateForm(QMainWindow, Ui_update):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('更新')
        self.setWindowIcon(QIcon(img))
        self.setFixedSize(331, 141)
        self.myv.setText(str_version)
        self.newv.setText(new_version_num)
        self.pushButton.clicked.connect(self.update)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton_3.clicked.connect(self.zan)

    def info(self):
        self.myv.setText(str_version)
        self.newv.setText(new_version_num)

    def update(self):
        webbrowser.open(official_address, 2)  # 打开官网

    def zan(self):
        with open("./library/datas/update.json", "w") as f:
            json.dump([1, 0], f)
        self.close()
        sip.delete(self)

    def Close(self):
        command.gc_Close(self)


class MyMainForm(QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('登录')
        img = "./library/imgs/image.png"
        self.setWindowIcon(QIcon(img))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.display)
        self.pushButton_2.clicked.connect(self.reg)
        self.pushButton_4.clicked.connect(self.Close)
        self.pushButton_5.clicked.connect(self.showMinimized)
        self.bg.setPixmap(
            QPixmap("./library/imgs/bgs/{}.png".format(str(random.randint(1, 4)))))  # 生成登录左图片
        self.label_7.setPixmap(
            QPixmap("./library/imgs/login_bg.png"))  # 登录界面背景
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet(
            command.css_load("./library/css/login_1.css"))
        self.pushButton_2.setStyleSheet(
            command.css_load("./library/css/login_1.css"))
        try:
            with open("./library/datas/data.json", 'r') as f:
                logdata = json.load(f)
            if logdata[0]:
                self.checkBox.setChecked(True)
                self.lineEdit.setText(logdata[2])
                password_ = ''
                for i in logdata[3].split(" "):
                    password_ += chr(int(i, 16))
                self.lineEdit_2.setText(password_)
            if logdata[1]:
                self.checkBox_2.setChecked(True)
                self.display()
        except:
            pass
        self.load = init_(self.label_4)
        self.load.signal.connect(self.start_connect)
        self.load.start()
        self.m_flag = False

    def Close(self):
        command.gc_Close(self)

    def display(self):
        global username, password

        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        if len(username) == 0 and len(password) == 0:
            QMessageBox.warning(self, "警告", "用户名和密码都没有输入！", QMessageBox.Ok)
            return
        elif len(username) == 0:
            QMessageBox.warning(self, "警告", "请输入用户名！", QMessageBox.Ok)
            return
        elif len(password) == 0:
            QMessageBox.warning(self, "警告", "请输入密码！", QMessageBox.Ok)
            return

        if cant_connect == 1:
            self.start_connect()
            try:
                self.show()
            except:
                pass
            return
        s.sendall("login_no_password：{a}：{b}".format(
            a=username, b=password).encode("GB2312"))

        global des_key
        des_key = receive_if()

        if command.command(self, des_key) == 0:
            try:
                self.show()
            except:
                pass
            return
        else:
            des_key = des_key.split("：")[-1]
            try:
                self.close()
            except:
                pass
            logdata = [False, False, "", ""]
            # if self.checkBox_2.isChecked():
            #     logdata[1] = True
            #     self.checkBox.setChecked(True)
            if self.checkBox.isChecked():
                logdata[0] = True
                logdata[2] = username
                password_2 = ''
                for i in range(len(password)):
                    password_2 += hex(ord(password[i]))
                    if not i >= len(password)-1:
                        password_2 += " "
                logdata[3] = password_2
            with open("./library/datas/data.json", "w") as f:
                json.dump(logdata, f)
            global main_win, ti
            main_win = MyMainmain()
            main_win.show()

            ti = TrayIcon()
            ti.show()
            self.close()
            sip.delete(self)
            del self

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def start_connect(self, Str=""):
        global cant_connect, cant_connect
        cant_connect = 0
        self.label_4.setText("正在连接服务器...")
        self.label_4.setStyleSheet("color:Black")
        self.change = command.changlabel(self.label_4, "正在连接服务器")
        self.change.start()

        self.conn = conn()
        self.conn.signal.connect(self.conne)
        self.conn.start()

    def conne(self, Str):
        if Str == "2":
            try:
                self.change.terminate()
                self.change.wait()
                del self.change
            except:
                pass
            gc.collect()
            self.label_4.setStyleSheet("color:Green")
            self.label_4.setText("服务器连接成功！")
            self.pushButton.setStyleSheet(
                command.css_load("./library/css/login_2.css"))
            self.pushButton_2.setStyleSheet(
                command.css_load("./library/css/login_2.css"))
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            global Receive_
            Receive_ = receive()
            Receive_.start()
            update_command()
            self.update()

        elif Str == "1":
            self.change.terminate()
            self.change.wait()
            try:
                self.change.terminate()
                self.change.wait()
                del self.change
            except:
                pass
            gc.collect()
            self.label_4.setStyleSheet("color:Red")
            self.label_4.setText("服务器无法连接！")

        else:
            self.change = command.changlabel(self.label_4, "正在连接服务器")
            self.change.start()

    def update(self):
        if must_update == 2:
            QMessageBox.warning(self, "警告", "你的版本过高！（手动滑稽，话说你怎么弄到这个的）\n最新版本是：{a}\n最低支持版本是：{c}\n你的版本是：{b}".format(
                a=new_version_num, c=max_version_num, b=str_version))
            webbrowser.open(official_address, 2)  # 打开官网
            sys.exit()

        elif must_update == 1:
            QMessageBox.warning(self, "警告", "你的版本过低！\n最新版本是：{a}\n最低支持版本是：{c}\n你的版本是：{b}".format(
                a=new_version_num, c=max_version_num, b=str_version))
            webbrowser.open(official_address, 2)  # 打开官网
            sys.exit()

        elif update_data == 0:
            if can_update == 1:
                self.update_gui = updateForm()
                self.update_gui.info()
                self.update_gui.show()

    def reg(self):
        global reg_
        reg_ = MyMainReg()
        self.close()
        reg_.show()
        sip.delete(self)
        del self


class MyMainReg(QWidget, Ui_reg):
    def __init__(self, parent=None):
        super(MyMainReg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('注册')
        self.setWindowIcon(QIcon(img))
        self.label_7.setPixmap(
            QPixmap("./library/imgs/login_bg.png"))  # 注册界面背景
        self.bg.setPixmap(
            QPixmap("./library/imgs/bgs/{}.png".format(str(random.randint(5, 7)))))  # 生成注册右图片
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.display)
        self.pushButton_2.clicked.connect(self.login)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_4.clicked.connect(self.Close)
        self.pushButton_5.clicked.connect(self.showMinimized)
        self.m_flag = False

    def display(self):
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        email = self.lineEdit_3.text().strip()

        if len(username) == 0 or len(password) == 0 or len(email) == 0:
            QMessageBox.warning(self, "警告", "至少一个空没有输入！", QMessageBox.Ok)
            return

        if email == "":
            QMessageBox.warning(self, "警告", "邮箱错误！", QMessageBox.Ok)
            return
        else:
            try:
                if email.split("@")[-1] == '':
                    QMessageBox.warning(self, "警告", "邮箱错误！", QMessageBox.Ok)
                    return
                elif email.split(".")[-1] == '':
                    QMessageBox.warning(self, "警告", "邮箱错误！", QMessageBox.Ok)
                    return
                elif email.split(".")[-2][-1] == '@':
                    QMessageBox.warning(self, "警告", "邮箱错误！", QMessageBox.Ok)
                    return
            except:
                QMessageBox.warning(self, "警告", "邮箱错误！", QMessageBox.Ok)
                return

        # s.sendall("Sign_up：{a}：{b}：{c}：{d}：{e}".format(
        #     a=username, b=password, c=email, d="pyforhc", e="win10").encode("GB2312"))
        s.sendall("Sign_up_nopassword：{a}：{b}：{c}：{d}：{e}".format(
            a=username, b=password, c=email, d="pyforhc", e="windows").encode("GB2312"))
        global reg_id
        reg_id = receive_if()

        if command.command(self, reg_id) == 0:
            return

        self.ver = MyMainVer()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.ver.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def Close(self):
        sys.exit()

    def login(self):
        global win
        win = MyMainForm()
        self.close()
        win.show()
        sip.delete(self)
        del self
        gc.collect()


class MyMainVer(QWidget, Ui_ver):
    def __init__(self, parent=None):
        super(MyMainVer, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('验证')
        self.setWindowIcon(QIcon(img))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.display)

    def display(self):
        data = self.lineEdit.text()
        data2 = reg_id.split("：")[1]
        if data == data2:
            QMessageBox.information(self, "信息", "验证成功！")
            global reg_
            self.login = MyMainForm()
            reg_.close()
            self.login.show()
            del data, data2
            try:
                sip.delete(reg_)
            except:
                pass
            sip.delete(self)
            self.Close()
        else:
            QMessageBox.warning(self, "警告", "验证失败，请重新输入")

    def Close(self):
        command.gc_Close(self)


class friend_model(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.ListItemData = []

    def data(self, index, role):
        if index.isValid() or (0 <= index.row() < len(self.ListItemData)):
            if role == Qt.DisplayRole:  # 名字
                return QVariant(self.ListItemData[index.row()]['name'])
            elif role == Qt.DecorationRole:  # 图像
                return QVariant(QIcon(self.ListItemData[index.row()]['icon_path']))
            elif role == Qt.SizeHintRole:
                return QVariant(QSize(70, 50))
            elif role == Qt.TextAlignmentRole:  # 宽高
                return QVariant(int(Qt.AlignHCenter | Qt.AlignVCenter))
            elif role == Qt.FontRole:  # 字体
                font = QFont()
                font.setPixelSize(15)
                font.setFamily('./library/ttfs/高端黑.ttf')
                return QVariant(font)

    def rowCount(self, index):
        return len(self.ListItemData)

    def data_init(self, name, icon_path):
        item_data = {}
        item_data["name"] = name
        item_data["icon_path"] = icon_path
        self.ListItemData.append(item_data)

    def deleteItem(self, index):
        del self.ListItemData[index]

    def getItem(self, index):
        if index > -1 and index < len(self.ListItemData):
            return self.ListItemData[index]


class ListView(QListView):
    left_clicked = pyqtSignal(int)
    right_clicked = pyqtSignal()

    def __init__(self, tab):
        super().__init__(tab)
        self.friend_model = friend_model()

    def contextMenuEvent(self, e):
        hitIndex = self.indexAt(e.pos()).column()
        if hitIndex > -1:
            pmenu = QMenu(self)
            pDeleteAct = QAction("删除", pmenu)
            pmenu.addAction(pDeleteAct)
            pDeleteAct.triggered.connect(self.deleteItemSlot)
            pmenu.popup(self.mapToGlobal(e.pos()))

    def deleteItemSlot(self):
        index = self.currentIndex().row()
        if index > -1:
            friend = self.friend_model.getItem(index)
            name = friend['name']
            s.sendall("get_id：".encode('gb2312')+name.encode("gb2312"))
            msg = receive_if()
            command.command(self, msg)
            msg = msg.split("：")
            if msg[0] == "get_id_ok":
                name_id = msg[1]
            else:
                QMessageBox.information(self, '信息', '删除好友失败')
                return
            s.sendall("del_friends：{a}：{b}：{c}：{d}".format(
                a=username, b=des_key, c=name_id, d=name).encode('gb2312'))
            msg = receive_if()
            command.command(self, msg)
            msg = msg.split('：')
            if msg[1] == "删除成功":
                self.friend_model.deleteItem(index)
                self.right_clicked.emit()

    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            hitIndex = self.indexAt(e.pos()).column()
            if hitIndex > -1:
                self.left_clicked.emit(hitIndex)

    def mouseDoubleClickEvent(self, e):
        hitIndex = self.indexAt(e.pos()).column()
        if hitIndex > -1:
            self.left_clicked.emit(hitIndex)


class MyMainmain(QMainWindow, Ui_tellroom_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('pyforhc')
        self.setWindowIcon(QIcon(img))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.label_2.setPixmap(QPixmap("./library/imgs/main/bg.png"))
        self.label_6.setPixmap(QPixmap("./library/imgs/image.png"))
        self.label_56.setPixmap(QPixmap("./library/imgs/image.png"))
        self.tabWidget.setCurrentWidget(self.tab)
        self.tabWidget_2.setCurrentWidget(self.tab_9)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.zui_xiao_hua)
        self.pushButton.clicked.connect(self.page1)
        self.pushButton.setIcon(QIcon("./library/imgs/main/2.png"))
        self.pushButton_2.clicked.connect(self.page2)
        self.pushButton_2.setIcon(QIcon("./library/imgs/main/1.png"))
        self.pushButton_3.clicked.connect(self.page3)
        self.pushButton_3.setIcon(QIcon("./library/imgs/main/user.png"))
        self.pushButton_7.clicked.connect(self.send)
        self.pushButton_9.clicked.connect(self.duihuan)
        self.pushButton_6.setIcon(QIcon("./library/imgs/main/friend.png"))
        self.pushButton_6.clicked.connect(self.page4)
        self.pushButton_8.setIcon(QIcon("./library/imgs/main/setting.png"))
        self.pushButton_8.clicked.connect(self.page5)
        self.pushButton_10.clicked.connect(self.page6)
        self.textBrowser.verticalScrollBar().setStyleSheet(
            command.css_load("./library/css/scroll_bar.css"))
        self.textEdit.verticalScrollBar().setStyleSheet(
            command.css_load("./library/css/scroll_bar.css"))

        self.pushButton_14.clicked.connect(self.open_dir)
        self.pushButton_11.clicked.connect(self.examine_update)
        self.pushButton_15.clicked.connect(self.switch_account)
        self.label_55.setVisible(False)
        self.pushButton_18.setVisible(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_18.setEnabled(False)

        self.pushButton_13.clicked.connect(self.search_friend)
        self.label_47.setVisible(False)
        self.label_48.setVisible(False)
        self.label_49.setVisible(False)
        self.label_50.setVisible(False)
        self.label_51.setVisible(False)
        self.label_52.setVisible(False)
        self.pushButton_17.setVisible(False)

        self.add_friend = ''
        self.enter = command.press()
        self.moni = moniter()
        self.moni.signal.connect(self.moniter_)
        self.enter.signal.connect(self.send_)
        self.enter.start()
        self.moni.start()
        self.close_num = 0
        self.m_flag = False
        try:
            if len(public_msg_2) != 0:
                self.textBrowser.setText(public_msg_2)
        except:
            pass
        for i in range(len(public_msg)):
            self.textBrowser.append(public_msg[i])
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        self.kong = "  "
        for i in username:
            if u'\u4e00' <= i <= u'\u9fff':
                self.kong += "  "
            else:
                self.kong += " "

        self.show_data()

        self.listView = ListView(self.tab_5)
        self.listView.setGeometry(QRect(0, 40, 161, 441))
        self.listView.setObjectName("listView")
        self.listView.setModel(self.listView.friend_model)
        self.listView.left_clicked.connect(self.open_telling_room)
        self.listView.right_clicked.connect(self.page9)

        s.sendall("get_friends：{a}：{b}".format(
            a=username, b=des_key).encode("gb2312"))
        msg = receive_if()
        msg_2 = msg.split('：')
        if msg_2[0] == "list_friends":
            self.friend_list = json5.loads(msg_2[1])["friend"]
        else:
            self.friend_list = []
        self.update_friend_list()

    def open_telling_room(self, index):
        friend = self.listView.friend_model.getItem(index)
        if friend == None:
            return
        name = friend["name"]
        self.label_59.setText(name)
        self.tabWidget_2.setCurrentWidget(self.tab_10)

    def update_friend_list(self):
        if len(self.listView.friend_model.ListItemData) == 0:
            for i in self.friend_list:
                self.listView.friend_model.data_init(i["name"], '')  # 以后需要修改
        else:
            s.sendall("get_friends：{a}：{b}".format(
                a=username, b=des_key).encode("gb2312"))
            msg = receive_if()
            command.command(self, msg)
            msg_2 = msg.split('：')
            if msg_2[0] == "list_friends":
                self.friend_list = json5.loads(msg_2[1])["friend"]
            else:
                self.friend_list = []
            self.listView.friend_model.ListItemData = []
            for i in self.friend_list:
                self.listView.friend_model.data_init(i["name"], '')  # 以后需要修改

    def show_data(self):
        global s

        s.sendall("get_user_data：{a}：{b}".format(
            a=username, b=des_key).encode("gb2312"))
        user_data = receive_if()
        if command.command(self, user_data) != 0:
            user_data = user_data.split("：")
            try:
                self.label_25.setText(user_data[1])  # 用户名
                self.label_26.setText(user_data[4])  # ID
                self.label_27.setText(user_data[2])  # 金币
                self.label_28.setText(user_data[3])  # 钻石
                self.label_38.setText(user_data[9])  # 邮箱
                self.label_40.setText(user_data[10])  # 手机
                self.label_42.setText(user_data[12])  # 微博
                self.label_29.setText(user_data[11])  # 微信
                self.label_30.setText(user_data[6])  # 注册时间
                self.label_31.setText(user_data[5])  # 上一次登录时间
                self.label_32.setText(user_data[8])  # 注册IP
                self.label_33.setText(user_data[7])  # 登录IP
                self.label_34.setText(user_data[14])  # 注册使用软件
                self.label_36.setText(user_data[13])  # 注册使用系统
            except:
                pass

    def search_friend(self):
        research = self.lineEdit.text().strip()
        if len(research) == 0:
            return

        s.sendall("get_id：".encode('gb2312')+research.encode("gb2312"))
        msg = receive_if()
        command.command(self, msg)
        msg = msg.split("：")
        if msg[0] == "get_id_no":
            self.label_51.setText("未搜到")
            self.label_51.setVisible(True)
            self.label_52.setVisible(True)
        elif msg[0] == "get_id_ok":
            self.label_51.setText("搜到")
            self.label_48.setText(msg[1])
            self.label_49.setText(research)
            self.add_friend = "add_friends：{a}：{b}：{c}：{d}".format(
                a=username, b=des_key, c=msg[1], d=research)
            self.pushButton_17.clicked.connect(self.add_friend_func)

            self.label_47.setVisible(True)
            self.label_48.setVisible(True)
            self.label_49.setVisible(True)
            self.label_50.setVisible(True)
            self.label_51.setVisible(True)
            self.label_52.setVisible(True)
            self.pushButton_17.setVisible(True)

    def add_friend_func(self):
        s.sendall(self.add_friend.encode('gb2312'))
        msg = receive_if()
        command.command(self, msg)

        self.label_47.setVisible(False)
        self.label_48.setVisible(False)
        self.label_49.setVisible(False)
        self.label_50.setVisible(False)
        self.label_51.setVisible(False)
        self.label_52.setVisible(False)
        self.pushButton_17.setVisible(False)

        self.update_friend_list()

    def page1(self):
        self.tabWidget.setCurrentWidget(self.tab_2)

    def page2(self):
        self.tabWidget.setCurrentWidget(self.tab_3)

    def page3(self):
        self.tabWidget.setCurrentWidget(self.tab_4)

    def page4(self):
        self.tabWidget.setCurrentWidget(self.tab_5)

    def page5(self):
        self.tabWidget.setCurrentWidget(self.tab_6)

    def page6(self):
        self.tabWidget.setCurrentWidget(self.tab_7)

    def page9(self):
        self.tabWidget_2.setCurrentWidget(self.tab_9)

    def page10(self):
        self.tabWidget_2.setCurrentWidget(self.tab_10)

    def send(self):
        text = self.textEdit.toPlainText()
        if not len(text) == 0:
            self.msg = text.split("\n")
            self.msg2 = ""
            for i in range(len(self.msg)):
                if not i == len(self.msg)-1:
                    self.msg2 += self.msg[i] + "\n" + self.kong
                else:
                    self.msg2 += self.msg[i]
            self.msg2 += "\n"
            self.num = 0
            for i in range(len(self.msg2)-1, 0, -1):
                if self.msg2[i] == " " or self.msg2[i] == "\n":
                    self.num += 1
                else:
                    break
            self.msg3 = ""
            for i in range(0, len(self.msg2)-self.num):
                self.msg3 += self.msg2[i]
            if len(self.msg3.split("\n")) > 10:
                QMessageBox.warning(self, "警告", "换行过多！")
                return
            try:
                s.sendall("chatting：public：{a}：{b}：{c}".format(
                    a=username, b=des_key, c=self.msg3).encode("GB2312"))
            except UnicodeEncodeError:
                QMessageBox.warning(
                    self, "警告", "codec can't encode character！")
                return
            self.textEdit.setText("")

    def send_(self, Str):
        self.send()

    def moniter_(self, Str):
        global public_msg
        for i in range(len(public_msg)):
            if command.command(self, public_msg[i]) != 0:
                self.textBrowser.append(public_msg[i].split("：")[2]+"\n")
        public_msg = []
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def duihuan(self):
        duihuanma = self.lineEdit_3.text().strip()
        mima = self.lineEdit_2.text().strip()
        if len(mima) == 0:
            mima = 0

        s.sendall("code：{}：{}：{}：{}".format(
            username, des_key, duihuanma, mima).encode("GB2312"))

        zhuang = receive_if()
        re = command.command(self, zhuang)
        if re == 0:
            return
        elif re == 1:
            QMessageBox.information(self, "信息", "兑换成功！", QMessageBox.Ok)
            self.lineEdit_3.setText("")
            self.lineEdit_2.setText("")

    def open_dir(self):
        os.system("explorer "+os.getcwd())

    def examine_update(self):
        if can_update == 1:
            self.label_55.setText("有新版本！")
            self.label_55.setStyleSheet("color:Green")
            self.label_55.setVisible(True)
            self.pushButton_18.setVisible(True)
        else:
            self.label_55.setText("您已是最新版！")
            self.label_55.setStyleSheet("color:Blue")
            self.label_55.setVisible(True)

    def closeEvent(self, event):
        if not self.close_num == 1:
            reply = QMessageBox.question(
                self, "关闭", "你确定要关闭程序吗？", QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                sys.exit()
            else:
                event.ignore()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def zui_xiao_hua(self):
        self.showMinimized()
        self.setWindowFlags(Qt.SplashScreen)
        self.show()

    def switch_account(self):
        reply = QMessageBox.question(
            self, "关闭", "你确定要切换账户吗？", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.close_num = 1
        self.close()

        try:
            with open("./library/datas/data.json", "r") as f:
                logdata = json.load(f)
            logdata[1] = False
            with open("./library/datas/data.json", "w") as f:
                json.dump(logdata, f)
        except:
            pass

        self.close_num = 0
        global s
        global Receive_
        Receive_.terminate()
        Receive_.wait()
        s.close()
        del Receive_, s
        dell()
        init()
        self.login = MyMainForm()
        self.login.show()
        sip.delete(self)
        del self
        gc.collect()


def main():
    global app, win, ju, logdata, public, private, load_rsa_key
    load_rsa_key = 0
    app = QApplication(sys.argv)
    win = MyMainForm()
    ju = True
    try:
        with open("data.json", "r") as f:
            logdata = json.load(f)
        if logdata[1]:
            ju = False
    except:
        pass
    if ju:
        try:
            win.show()
        except:
            pass

    sys.exit(app.exec_())
