# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
# Created by: PyQt5 UI code generator 5.13.2
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 650)      
        MainWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/image/login_form_bg.jpg);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid grey;\n"
"border-top: 0px;\n"
"border-right: 0px;\n"
"border-left: 0px;\n"
"border-bottom-color: rgb(6, 6, 6);\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgba(217, 217, 217, 50);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid grey;\n"
"border-top: 0px;\n"
"border-right: 0px;\n"
"border-left: 0px;\n"
"border-bottom-color: rgb(6, 6, 6);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(85, 125, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-style: groove;\n"
"border-bottom-right-radius: 4px;\n"
"border-top-left-radius: 4px;\n"
"font: 11pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-style: groove;\n"
"border-bottom-right-radius: 4px;\n"
"border-top-left-radius: 4px;\n"
"font: 13pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:pressed:!hover{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-style: groove;\n"
"border-bottom-right-radius: 4px;\n"
"border-top-left-radius: 4px;\n"
"font: 13pt \"MS Reference Sans Serif\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.pushButton_login)
        self.pushButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_register.setObjectName("pushButton_register")
        self.verticalLayout.addWidget(self.pushButton_register)
        self.gridLayout.addLayout(self.verticalLayout, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_username.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout_2.addWidget(self.lineEdit_username)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_2.addWidget(self.lineEdit_password)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Form"))
        self.pushButton_login.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_register.setText(_translate("MainWindow", "REGISTER"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
from . import login_form_rc
