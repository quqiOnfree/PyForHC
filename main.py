import sys, json, webbrowser, command
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from ui import Ui_Form, Ui_reg, Ui_ver, Ui_MainWindow, Ui_duihuan, Ui_update

img = "image.png"
str_version = "1.0.0.0"
int_version = 1
update = 0
must_update = 0
can_update = 0

def update_command():
    global update

    if update == 0:
        s = command.connect()
        if not s == False:
            s.sendall("edition".encode("GB2312"))
            version = s.recv(1023).decode("GB2312")
            version2 = version.split("：")
            new_version = int(version2[1])
            max_version = int(version2[2])
            global new_version_num,max_version_num
            new_version_num = version2[3]
            max_version_num = version2[4]

            global can_update,must_update
            can_update = 0
            must_update =0
            if max_version > int_version:
                must_update = 1
            if new_version > int_version:
                can_update = 1
            update = 1

class updateForm(QMainWindow, Ui_update):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('更新')
        self.setWindowIcon(QIcon(img))
        self.setFixedSize(331,141)
        self.myv.setText(str_version)
        self.newv.setText(new_version_num)
        self.pushButton.clicked.connect(self.update)
        self.pushButton_2.clicked.connect(self.Close)

    def info(self):
        self.myv.setText(str_version)
        self.newv.setText(new_version_num)

    def update(self):
        webbrowser.open("https://hcteam.top/")
    
    def Close(self):
        self.close()

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setFixedSize(372,252)
        self.setupUi(self)
        self.setWindowTitle('登录')
        self.setWindowIcon(QIcon(img))
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

    def update(self):
        if must_update == 1:
            QMessageBox.warning(self,"警告","你的版本过低！\n最新版本是：{a}\n最低支持版本是：{c}\n你的版本是：{b}".format(a=new_version_num,c=max_version_num,b=str_version))
            webbrowser.open("https://hcteam.top/")
            sys.exit()
        if can_update == 1:
            self.update_gui = updateForm()
            self.update_gui.info()
            self.update_gui.show()
        
    def display(self):
        global username,password

        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        if len(username) == 0:
            QMessageBox.warning(self,"警告","请输入用户名！",QMessageBox.Ok)
        if len(password) == 0:
            QMessageBox.warning(self,"警告","请输入密码！",QMessageBox.Ok)
        if len(username) == 0 or len(password) == 0:
            return

        s = command.connect()
        if s == False:
            QMessageBox.warning(self,"警告","无法连接至服务器！")
            return

        s.sendall("login_no_password：{a}：{b}".format(a=username,b=password).encode("GB2312"))
        
        global des_key
        des_key = s.recv(1024).decode("GB2312")

        if command.command(self,des_key) == 0:
            return
        else:
            des_key = des_key.split("：")[-1]
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
        self.close()
        self.reg.show()

    def close(self):
        return super().close()

class MyMainReg(QMainWindow, Ui_reg):
    def __init__(self, parent=None):
        super(MyMainReg, self).__init__(parent)
        self.setFixedSize(401,300)
        self.setupUi(self)
        self.setWindowTitle('注册')
        self.setWindowIcon(QIcon(img))
        self.pushButton.clicked.connect(self.display)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

    def display(self):
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        email = self.lineEdit_3.text().strip()

        if len(username) == 0 or len(password) == 0 or len(email) == 0:
            QMessageBox.warning(self,"警告","至少一个空没有输入！",QMessageBox.Ok)
            return
        
        if email == "":
            QMessageBox.warning(self,"警告","邮箱错误！",QMessageBox.Ok)
            return
        else:
            try:
                if email.split("@")[-1] == '':
                    QMessageBox.warning(self,"警告","邮箱错误！",QMessageBox.Ok)
                    return
                elif email.split(".")[-1] == '':
                    QMessageBox.warning(self,"警告","邮箱错误！",QMessageBox.Ok)
                    return
                elif email.split(".")[-2][-1] == '@':
                    QMessageBox.warning(self,"警告","邮箱错误！",QMessageBox.Ok)
                    return
            except:
                QMessageBox.warning(self,"警告","邮箱错误！",QMessageBox.Ok)
                return

        s = command.connect()
        if s == False:
            QMessageBox.warning(self,"警告","无法连接至服务器！")
            return

        s.sendall("Sign_up：{a}：{b}：{c}：{d}：{e}".format(a=username,b=password,c=email,d="pyforhc",e="win10").encode("GB2312"))
        global reg_id
        reg_id = s.recv(1024).decode("GB2312")

        if command.command(self,reg_id) == 0:
            return

        self.ver = MyMainVer()
        self.ver.show()

class MyMainVer(QMainWindow, Ui_ver):
    def __init__(self, parent=None):
        super(MyMainVer, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('验证')
        self.setWindowIcon(QIcon(img))
        self.pushButton.clicked.connect(self.display)
    
    def display(self):
        data = self.lineEdit.text()
        data2 = reg_id.split("：")[1]
        if data == data2:
            QMessageBox.information(self,"信息","验证成功！")
            self.login = MyMainForm()
            self.login.show()
            self.close()
        else:
            QMessageBox.warning(self,"警告","验证失败，请重新输入")

class MyMaindui(QMainWindow, Ui_duihuan):
    def __init__(self, parent=None):
        super(MyMaindui, self).__init__(parent)
        self.setFixedSize(290,141)
        self.setupUi(self)
        self.setWindowTitle('兑换码系统')
        self.setWindowIcon(QIcon(img))
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.nook)

    def ok(self):
        duihuanma = self.lineEdit.text().strip()
        mima = self.lineEdit_2.text().strip()
        if len(mima) == 0:
            mima = 0

        s = command.connect()
        if s == False:
            QMessageBox.warning(self,"警告","无法连接至服务器！")
            return

        s.sendall("code：{}：{}：{}：{}".format(username,des_key,duihuanma,mima).encode("GB2312"))
        zhuang = s.recv(1024).decode("GB2312")
        re = command.command(self,zhuang)
        if re == 0:
            return
        elif re == 1:
            QMessageBox.information(self,"信息","兑换成功！",QMessageBox.Ok)
            self.close()
    
    def nook(self):
        self.close()

class MyMainmain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainmain, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('pyforhc')
        self.setWindowIcon(QIcon(img))
        self.shuaxin.clicked.connect(self.display)
        self.duihuan.clicked.connect(self.dui)
        self.actionexit.triggered.connect(self.exit)
        self.actionswitch_account.triggered.connect(self.switch_account)
        self.set.setTitle("设置")
        self.actionswitch_account.setText("切换账户")
        self.actionexit.setText("退出")

    def switch_account(self):
        self.close()

        try:
            with open("data.json","r") as f:
                logdata = json.load(f)
            logdata[1] = False
            with open("data.json","w") as f:
                json.dump(logdata,f)
        except:
            pass

        self.login = MyMainForm()
        self.login.show()

    def exit(self):
        sys.exit()

    def display(self):
        self.username.setText(u"{}".format(username))

        s = command.connect()
        if s == False:
            QMessageBox.warning(self,"警告","无法连接至服务器！")
            return
        
        s.sendall("get_user_data：{a}：{b}".format(a=username,b=des_key).encode("GB2312"))
        user_data = s.recv(1024).decode("GB2312")
        command.command(self,user_data)
        
        user_data = user_data.split("：")
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
    key = command.rsa_key(100,1000)
    public,private = key["public"],key["private"]
    update_command()
    win.update()

    sys.exit(app.exec_())
