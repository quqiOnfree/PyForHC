# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tellroom_2(object):
    def setupUi(self, tellroom_2):
        tellroom_2.setObjectName("tellroom_2")
        tellroom_2.resize(852, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tellroom_2.sizePolicy().hasHeightForWidth())
        tellroom_2.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(tellroom_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(9, 9, 831, 551))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../library/imgs/main/bg.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 30, 16, 16))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(790, 30, 16, 16))
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
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 64, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 15px;\n"
"    font-family:微软雅黑;\n"
"    background:#FFFFFF;\n"
"    border:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#F0F0F0;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#F0F0F0;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../library/imgs/main/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 15px;\n"
"    font-family:微软雅黑;\n"
"    background:#FFFFFF;\n"
"    border:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#F0F0F0;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#F0F0F0;\n"
"}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../library/imgs/main/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 15px;\n"
"    font-family:微软雅黑;\n"
"    background:#FFFFFF;\n"
"    border:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#F0F0F0;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#F0F0F0;\n"
"}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../library/imgs/main/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 40, 741, 511))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background:#FFFFFF")
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 741, 491))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 2, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(190, 200))
        self.groupBox.setMaximumSize(QtCore.QSize(190, 200))
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 20, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(70, 70))
        self.label_6.setMaximumSize(QtCore.QSize(70, 70))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../library/imgs/image.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 171, 101))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 290, 731, 151))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(-10, 270, 741, 20))
        self.label_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 10px;\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 731, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(-10, -10, 751, 501))
        self.label_12.setStyleSheet("background:#FFFFFF")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(500, 450, 111, 31))
        self.label_13.setObjectName("label_13")
        self.label_12.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        self.pushButton_7.raise_()
        self.textBrowser.raise_()
        self.label_13.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    border-radius: 15px;\n"
"    font-family:宋体;\n"
"    background:#008B8B;\n"
"    border:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#00CED1;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#00CED1;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(160, 200, 111, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(327, 200, 171, 31))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(160, 120, 71, 31))
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(327, 120, 171, 31))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(320, 220, 181, 20))
        self.label_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(320, 140, 181, 16))
        self.label_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(-7, -9, 751, 501))
        self.label_11.setStyleSheet("background:#FFFFFF")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.pushButton_9.raise_()
        self.label_8.raise_()
        self.lineEdit_2.raise_()
        self.label_9.raise_()
        self.lineEdit_3.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("background:#FFFFFF")
        self.tab_4.setObjectName("tab_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(210, 0, 341, 481))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_25)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_26)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_29)
        self.label_30 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_30)
        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_31)
        self.label_32 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_32)
        self.label_33 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_33)
        self.label_34 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_34)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 741, 31))
        self.label_3.setStyleSheet("background:#FFFFFF")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 831, 20))
        self.label_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("Color:#345E8C")
        self.label.setObjectName("label")
        self.label_2.raise_()
        self.gridLayoutWidget.raise_()
        self.tabWidget.raise_()
        self.label_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label.raise_()
        self.label_14.raise_()
        tellroom_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(tellroom_2)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(tellroom_2)

    def retranslateUi(self, tellroom_2):
        _translate = QtCore.QCoreApplication.translate
        tellroom_2.setWindowTitle(_translate("tellroom_2", "MainWindow"))
        self.label_5.setText(_translate("tellroom_2", "@氢冷团队2021\n"
"\n"
"曲奇Onfree\n"
"皓\n"
"ad973\n"
"Lovely简世"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("tellroom_2", "Tab 1"))
        self.pushButton_7.setText(_translate("tellroom_2", "发送"))
        self.label_13.setText(_translate("tellroom_2", "(ctrl+enter 发送)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("tellroom_2", "Tab 2"))
        self.pushButton_9.setText(_translate("tellroom_2", "兑换"))
        self.label_8.setText(_translate("tellroom_2", "密码（没有不用填）"))
        self.lineEdit_2.setPlaceholderText(_translate("tellroom_2", "密码"))
        self.label_9.setText(_translate("tellroom_2", "兑换码"))
        self.lineEdit_3.setPlaceholderText(_translate("tellroom_2", "兑换码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("tellroom_2", "页"))
        self.label_15.setText(_translate("tellroom_2", "用户名"))
        self.label_16.setText(_translate("tellroom_2", "ID"))
        self.label_17.setText(_translate("tellroom_2", "金币"))
        self.label_18.setText(_translate("tellroom_2", "钻石"))
        self.label_19.setText(_translate("tellroom_2", "邮箱"))
        self.label_20.setText(_translate("tellroom_2", "注册时间"))
        self.label_21.setText(_translate("tellroom_2", "上一次登录时间"))
        self.label_22.setText(_translate("tellroom_2", "注册IP"))
        self.label_23.setText(_translate("tellroom_2", "上次登录IP"))
        self.label_24.setText(_translate("tellroom_2", "注册使用软件"))
        self.label_25.setText(_translate("tellroom_2", "TextLabel"))
        self.label_26.setText(_translate("tellroom_2", "TextLabel"))
        self.label_27.setText(_translate("tellroom_2", "TextLabel"))
        self.label_28.setText(_translate("tellroom_2", "TextLabel"))
        self.label_29.setText(_translate("tellroom_2", "TextLabel"))
        self.label_30.setText(_translate("tellroom_2", "TextLabel"))
        self.label_31.setText(_translate("tellroom_2", "TextLabel"))
        self.label_32.setText(_translate("tellroom_2", "TextLabel"))
        self.label_33.setText(_translate("tellroom_2", "TextLabel"))
        self.label_34.setText(_translate("tellroom_2", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("tellroom_2", "页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("tellroom_2", "页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("tellroom_2", "页"))
        self.label.setText(_translate("tellroom_2", "氢聊"))
