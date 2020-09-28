# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 659)
        MainWindow.setMinimumSize(QtCore.QSize(913, 659))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/image/image_4.jpg);\n"
"}\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Myanmar Text\";\n"
"padding: 5px;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid grey;\n"
"border-top: 0px;\n"
"border-right: 0px;\n"
"border-left: 0px;\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgba(217, 217, 217, 50);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid grey;\n"
"border-top: 0px;\n"
"border-right: 0px;\n"
"border-left: 0px;\n"
"border-bottom-color: rgb(255, 255, 255);\n"
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
"border-bottom-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"font: 13pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:pressed:!hover{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-style: groove;\n"
"border-bottom-right-radius: 4px;\n"
"border-top-left-radius: 4px;\n"
"font: 13pt \"MS Reference Sans Serif\";\n"
"}\n"
"QRadioButton{\n"
"font: 10pt \"MS Reference Sans Serif\";\n"
"color: rgb(255,255,255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(50, 69, 101, 31))
        self.label_username.setObjectName("label_username")
        self.label_passwd = QtWidgets.QLabel(self.centralwidget)
        self.label_passwd.setGeometry(QtCore.QRect(50, 130, 100, 30))
        self.label_passwd.setObjectName("label_passwd")
        self.label_fname = QtWidgets.QLabel(self.centralwidget)
        self.label_fname.setGeometry(QtCore.QRect(50, 188, 100, 30))
        self.label_fname.setObjectName("label_fname")
        self.label_lname = QtWidgets.QLabel(self.centralwidget)
        self.label_lname.setGeometry(QtCore.QRect(50, 239, 100, 30))
        self.label_lname.setObjectName("label_lname")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(50, 290, 51, 30))
        self.label_age.setObjectName("label_age")
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        self.label_gender.setGeometry(QtCore.QRect(50, 400, 81, 30))
        self.label_gender.setObjectName("label_gender")
        self.label_city = QtWidgets.QLabel(self.centralwidget)
        self.label_city.setGeometry(QtCore.QRect(50, 350, 41, 30))
        self.label_city.setObjectName("label_city")
        self.label_addr = QtWidgets.QLabel(self.centralwidget)
        self.label_addr.setGeometry(QtCore.QRect(50, 460, 71, 31))
        self.label_addr.setObjectName("label_addr")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(150, 70, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(150, 130, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_fname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fname.setGeometry(QtCore.QRect(150, 190, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_fname.setFont(font)
        self.lineEdit_fname.setObjectName("lineEdit_fname")
        self.lineEdit_lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lname.setGeometry(QtCore.QRect(150, 240, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_lname.setFont(font)
        self.lineEdit_lname.setObjectName("lineEdit_lname")
        self.lineEdit_city = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_city.setGeometry(QtCore.QRect(130, 350, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_city.setFont(font)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_address.setGeometry(QtCore.QRect(130, 460, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_address.setFont(font)
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.pushButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register.setGeometry(QtCore.QRect(724, 582, 91, 41))
        self.pushButton_register.setObjectName("pushButton_register")
        self.radioButton_male = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_male.setGeometry(QtCore.QRect(140, 410, 51, 17))
        self.radioButton_male.setObjectName("radioButton_male")
        self.radioButton_female = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_female.setGeometry(QtCore.QRect(200, 410, 71, 17))
        self.radioButton_female.setObjectName("radioButton_female")
        self.radioButton_other = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_other.setGeometry(QtCore.QRect(270, 410, 61, 17))
        self.radioButton_other.setObjectName("radioButton_other")
        self.lineEdit_age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_age.setGeometry(QtCore.QRect(220, 300, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_age.setFont(font)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.label_cover = QtWidgets.QLabel(self.centralwidget)
        self.label_cover.setGeometry(QtCore.QRect(140, 290, 81, 51))
        self.label_cover.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.136364, y1:0.585, x2:1, y2:0, stop:0 rgba(8, 64, 113, 255), stop:0.528409 rgba(14, 79, 137, 255), stop:1 rgba(14, 83, 140, 255));")
        self.label_cover.setText("")
        self.label_cover.setObjectName("label_cover")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_username, self.lineEdit_password)
        MainWindow.setTabOrder(self.lineEdit_password, self.lineEdit_fname)
        MainWindow.setTabOrder(self.lineEdit_fname, self.lineEdit_lname)
        MainWindow.setTabOrder(self.lineEdit_lname, self.lineEdit_age)
        MainWindow.setTabOrder(self.lineEdit_age, self.lineEdit_city)
        MainWindow.setTabOrder(self.lineEdit_city, self.radioButton_male)
        MainWindow.setTabOrder(self.radioButton_male, self.radioButton_female)
        MainWindow.setTabOrder(self.radioButton_female, self.radioButton_other)
        MainWindow.setTabOrder(self.radioButton_other, self.lineEdit_address)
        MainWindow.setTabOrder(self.lineEdit_address, self.pushButton_register)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registration Window"))
        self.label_username.setText(_translate("MainWindow", "Username:"))
        self.label_passwd.setText(_translate("MainWindow", "Password:"))
        self.label_fname.setText(_translate("MainWindow", "First Name:"))
        self.label_lname.setText(_translate("MainWindow", "Last Name:"))
        self.label_age.setText(_translate("MainWindow", "Age:"))
        self.label_gender.setText(_translate("MainWindow", "Gender:"))
        self.label_city.setText(_translate("MainWindow", "City:"))
        self.label_addr.setText(_translate("MainWindow", "Address:"))
        self.pushButton_register.setText(_translate("MainWindow", "Register"))
        self.radioButton_male.setText(_translate("MainWindow", "Male"))
        self.radioButton_female.setText(_translate("MainWindow", "Female"))
        self.radioButton_other.setText(_translate("MainWindow", "Other"))
from . import login_form_rc
