import sys,socket,json,base64,pyDes,binascii
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from pyDes import *
from login import Ui_Form
from error import Ui_error
from reg import Ui_reg
from ver import Ui_ver
from msg import Ui_msg
from mainwin import Ui_MainWindow
from duihuan import Ui_duihuan

def endes(key,data):
    try:
            k = pyDes.des(key,pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None,padmode=pyDes.PAD_PKCS5)
    except:
        return "error"
    d = binascii.hexlify(k.encrypt(data))
    return d

def DesEncrypt(str):
    Des_Key = "5GTS&$#G" # Key
    Des_IV = "\0\0\0\0\0\0\0\0" # 自定IV向量
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)

    EncryptStr = k.encrypt(str)

    return base64.b64encode(EncryptStr)

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('登录')
        self.pushButton.clicked.connect(self.display)
        self.pushButton_2.clicked.connect(self.reg)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        try:
            with open("data.json",'r') as f:
                logdata = json.load(f)
            if logdata[0]:
                self.checkBox.setChecked(True)
                self.lineEdit.setText(logdata[2])
                self.lineEdit_2.setText(logdata[3])
            if logdata[1]:
                self.checkBox_2.setChecked(True)
                self.display()
        except:
            pass
        
    def display(self):
        global username,password

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if len(username) == 0:
            self.yonghu = MyMainError(error="请输入用户名！")
            self.yonghu.show()
        if len(password) == 0:
            self.mima = MyMainError(error="请输入密码！")
            self.mima.show()
        if len(username) == 0 or len(password) == 0:
            return
        
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('118.195.172.203',3000))
        except:
            pass

        try:
            s.sendall("loading".encode("GB2312"))
            data = s.recv(1024).decode("GB2312")
            if data == "off":
                self.child_win = MyMainError(error="服务器不在线！")
                s.close()
                self.child_win.show()
                return
        except:
            self.child_win = MyMainError(error="无法连接至服务器！")
            s.close()
            self.child_win.show()
            return

        d = DesEncrypt(password)
        e = endes("5GTS&$#G",password)
        print(d.decode("GB2312"),e.decode("GB2312"))
        # s.sendall("login：{a}：{b}".format(a=username,b=d.decode("UTF-8")).encode("GB2312"))
        s.sendall("login_no_password：{a}：{b}".format(a=username,b=password).encode("GB2312"))
        
        global des_key
        des_key = s.recv(1024).decode("GB2312").split("：")[-1]
        print(des_key)
        if des_key == "密码错误":
            self.logerror = MyMainError(error="密码错误！")
            s.close()
            self.logerror.show()
        else:
            try:
                self.close()
            except:
                pass
            logdata = [False,False,"",""]
            if self.checkBox_2.isChecked():
                logdata[1] = True
                self.checkBox.setChecked(True)
            if self.checkBox.isChecked():
                logdata[0] = True
                logdata[2] = username
                logdata[3] = password
            with open("data.json","w") as f:
                json.dump(logdata,f)
            self.main = MyMainmain()
            self.main.display()
            self.main.show()

    def reg(self):
        self.reg = MyMainReg()
        self.reg.show()

    def close(self):
        return super().close()

class MyMainError(QMainWindow, Ui_error):
    def __init__(self, parent=None, error=""):
        super(MyMainError, self).__init__(parent)
        self.setupUi(self, error)
        self.setWindowTitle('错误')

class MyMainReg(QMainWindow, Ui_reg):
    def __init__(self, parent=None):
        super(MyMainReg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('注册')
        self.pushButton.clicked.connect(self.display)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

    def display(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()

        if len(username) == 0:
            self.yonghu = MyMainError(error="请输入用户名！")
            self.yonghu.show()
        if len(password) == 0:
            self.mima = MyMainError(error="请输入密码！")
            self.mima.show()
        if len(email) == 0:
            self.youxiang = MyMainError(error="请输入邮箱！")
            self.youxiang.show()
        if len(username) == 0 or len(password) == 0 or len(email) == 0:
            return

        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('118.195.172.203',3000))
        except:
            pass

        try:
            s.sendall("loading".encode("GB2312"))
            data = s.recv(1024).decode("UTF-8")
            if data == "off":
                self.child_win = MyMainError(error="服务器不在线！")
                s.close()
                self.child_win.show()
                return
        except:
            self.child_win = MyMainError(error="无法连接至服务器！")
            s.close()
            self.child_win.show()
            return

        s.sendall("Sign_up：{a}：{b}：{c}：{d}：{e}".format(a=username,b=password,c=email,d="pyforhc",e="win10").encode("GB2312"))
        global reg_id
        reg_id = s.recv(1024).decode("GB2312")
        print(reg_id)
        if reg_id == 'message：服务端发送错误：错误':
            self.regerror = MyMainError(error="服务端发送错误！")
            s.close()
            self.regerror.show()
        elif reg_id == "message：邮箱错误：错误":
            self.regerror = MyMainError(error="邮箱错误！")
            s.close()
            self.regerror.show()
        elif reg_id == "message：这个用户已经被注册了：错误":
            self.regerror = MyMainError(error="这个用户已经被注册了！")
            s.close()
            self.regerror.show()
        else:
            self.ver = MyMainVer()
            self.ver.show()

class MyMainVer(QMainWindow, Ui_ver):
    def __init__(self, parent=None):
        super(MyMainVer, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('验证')
        self.pushButton.clicked.connect(self.display)
    
    def display(self):
        data = self.lineEdit.text()
        data2 = reg_id.split("：")[1]
        if data == data2:
            self.msg = MyMainMsg(msg="验证成功！")
            self.msg.show()

class MyMainMsg(QMainWindow, Ui_msg):
    def __init__(self, parent=None, msg=""):
        super(MyMainMsg, self).__init__(parent)
        self.setupUi(self,msg)
        self.setWindowTitle('验证')

class MyMaindui(QMainWindow, Ui_duihuan):
    def __init__(self, parent=None):
        super(MyMaindui, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('兑换码系统')
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.nook)

    def ok(self):
        duihuanma = self.lineEdit.text()

        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('118.195.172.203',3000))
        except:
            pass

        try:
            s.sendall("loading".encode("GB2312"))
            data = s.recv(1024).decode("UTF-8")
            if data == "off":
                self.child_win = MyMainError(error="服务器不在线！")
                s.close()
                self.child_win.show()
                return
        except:
            self.child_win = MyMainError(error="无法连接至服务器！")
            s.close()
            self.child_win.show()
            return

        d = endes("5GTS&$#G",password)
        s.sendall("code：{}：{}：{}：{}".format(username,des_key,duihuanma,d).encode("GB2312"))
        zhuang = s.recv(1024).decode("GB2312")
        print(zhuang)
        if zhuang.split("：")[0] == "code_on":
            self.msg = MyMainMsg(msg="兑换成功！")
            self.close()
            self.msg.show()
        elif zhuang == "message：兑换码不可用":
            self.duierror = MyMainError(error="兑换码不可用！")
            s.close()
            self.duierror.show()
        elif zhuang == "message：兑换码已被兑换完":
            self.duierror = MyMainError(error="兑换码已被兑换完！")
            s.close()
            self.duierror.show()
    
    def nook(self):
        self.close()

class MyMainmain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainmain, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('pyforhc')
        self.shuaxin.clicked.connect(self.display)
        self.duihuan.clicked.connect(self.dui)
        self.actionexit.triggered.connect(self.exit)
        self.actionswitch_account.triggered.connect(self.switch_account)

    def switch_account(self):
        self.close()

        # logdata = [False,False,"",""]
        try:
            with open("data.json","r") as f:
                logdata = json.load(f)
            logdata[1] = False
            with open("data.json","w") as f:
                json.dump(logdata,f)
        except:
            pass

        self.login = MyMainForm()

        try:
            s.close()
        except:
            pass

        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('118.195.172.203',3000))
        except:
            pass

        try:
            s.sendall("loading".encode("GB2312"))
            data = s.recv(1024).decode("UTF-8")
            if data == "off":
                self.child_win = MyMainError(error="服务器不在线！")
                s.close()
                self.child_win.show()
                return
        except:
            self.child_win = MyMainError(error="无法连接至服务器！")
            s.close()
            self.child_win.show()
            return

        self.login.show()

    def exit(self):
        sys.exit()

    def display(self):
        self.username.setText(u"{}".format(username))

        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('118.195.172.203',3000))
        except:
            pass

        try:
            s.sendall("loading".encode("GB2312"))
            data = s.recv(1024).decode("UTF-8")
            if data == "off":
                self.child_win = MyMainError(error="服务器不在线！")
                s.close()
                self.child_win.show()
                return
        except:
            self.child_win = MyMainError(error="无法连接至服务器！")
            s.close()
            self.child_win.show()
            return
        
        s.sendall("get_user_data：{a}：{b}".format(a=username,b=des_key).encode("GB2312"))
        user_data = s.recv(1024).decode("GB2312").split("：")
        self.username.setText(user_data[-3])
        self.gold.setText(user_data[-2])
        self.dim.setText(user_data[-1])

    def dui(self):
        self.duiwin = MyMaindui()
        self.duiwin.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainForm()
    ju = True
    try:
        with open("data.json","r") as f:
            logdata = json.load(f)
        if logdata[1]:
            ju = False
    except:
        pass
    if ju:
        win.show()
    sys.exit(app.exec_())