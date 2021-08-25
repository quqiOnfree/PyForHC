# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reg(object):
    def setupUi(self, reg):
        reg.setObjectName("reg")
        reg.resize(672, 459)
        reg.setAutoFillBackground(False)
        reg.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(reg)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/logsure.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(reg)
        self.label.setGeometry(QtCore.QRect(20, 140, 31, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(reg)
        self.label_3.setGeometry(QtCore.QRect(530, 420, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:White")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(reg)
        self.lineEdit.setGeometry(QtCore.QRect(70, 140, 141, 31))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(reg)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 190, 141, 31))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(reg)
        self.pushButton.setGeometry(QtCore.QRect(40, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 15px;\n"
"    font-family:微软雅黑;\n"
"    background:#008B8B;\n"
"    border:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#00CED1;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#00CED1;\n"
"}")
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(reg)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 15px;\n"
"    font-family:微软雅黑;\n"
"    background:#008B8B;\n"
"    border:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#00CED1;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#00CED1;\n"
"}")
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.bg = QtWidgets.QLabel(reg)
        self.bg.setGeometry(QtCore.QRect(270, 0, 401, 461))
        self.bg.setStyleSheet("border-radius: 15px;border:15px")
        self.bg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("../../hc_code/code/imgs/bg.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.label_5 = QtWidgets.QLabel(reg)
        self.label_5.setGeometry(QtCore.QRect(70, 160, 141, 16))
        self.label_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(reg)
        self.label_6.setGeometry(QtCore.QRect(70, 210, 141, 16))
        self.label_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(reg)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 671, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../hc_code/code/imgs/login_bg.png"))
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(reg)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 10, 16, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 7px;\n"
"    font-family:微软雅黑;\n"
"    background:#FF0000;\n"
"    border:7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#BC1717;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#BC1717;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(reg)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 10, 16, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 7px;\n"
"    font-family:微软雅黑;\n"
"    background:#C0C0C0;\n"
"    border:7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#A8A8A8;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#A8A8A8;\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(reg)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 240, 141, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(reg)
        self.label_8.setGeometry(QtCore.QRect(70, 260, 141, 16))
        self.label_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(reg)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/素材/邮箱/1.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_7.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.bg.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.lineEdit_3.raise_()
        self.label_8.raise_()
        self.label_9.raise_()

        self.retranslateUi(reg)
        QtCore.QMetaObject.connectSlotsByName(reg)

    def retranslateUi(self, reg):
        _translate = QtCore.QCoreApplication.translate
        reg.setWindowTitle(_translate("reg", "Form"))
        self.label_3.setText(_translate("reg", "氢冷团队@2021"))
        self.lineEdit.setPlaceholderText(_translate("reg", "账号"))
        self.lineEdit_2.setPlaceholderText(_translate("reg", "密码"))
        self.pushButton.setText(_translate("reg", "注册"))
        self.pushButton_2.setText(_translate("reg", "登录"))
        self.lineEdit_3.setPlaceholderText(_translate("reg", "邮箱"))
import ui.login.login_rc
import ui.reg_rc
