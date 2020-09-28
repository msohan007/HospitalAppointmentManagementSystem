# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Appointment_Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 598)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/image/image_3.jpg);\n"
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
"border-style: outset;\n"
"border-bottom-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"font: 11pt \"MS Reference Sans Serif\";\n"
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
"}\n"
"\n"
"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"    color: rgb(238, 238, 236);\n"
"    font: 57 11pt \"Ubuntu\";\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(153, 209, 246, 255), stop:0.487562 rgba(72, 136, 139, 246), stop:0.810945 rgba(88, 161, 193, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_docname = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_docname.setObjectName("comboBox_docname")
        self.comboBox_docname.addItem("")
        self.comboBox_docname.addItem("")
        self.comboBox_docname.addItem("")
        self.gridLayout.addWidget(self.comboBox_docname, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_userId = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_userId.setFont(font)
        self.label_userId.setObjectName("label_userId")
        self.gridLayout.addWidget(self.label_userId, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setReadOnly(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.listwidget_userdetails = QtWidgets.QListWidget(self.centralwidget)
        self.listwidget_userdetails.setStyleSheet("background-color: rgba(46, 52, 54,80);")
        self.listwidget_userdetails.setObjectName("listwidget_userdetails")
        self.gridLayout_2.addWidget(self.listwidget_userdetails, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_check_availability = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check_availability.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButton_check_availability.setStyleSheet("padding: 5px;")
        self.pushButton_check_availability.setObjectName("pushButton_check_availability")
        self.horizontalLayout.addWidget(self.pushButton_check_availability)
        self.pushButton_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirm.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButton_confirm.setStyleSheet("padding: 5px;")
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.horizontalLayout.addWidget(self.pushButton_confirm)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Appointment Form"))
        self.label_4.setText(_translate("MainWindow", "Time:"))
        self.label_3.setText(_translate("MainWindow", "Appontment Date:"))
        self.comboBox_docname.setItemText(0, _translate("MainWindow", "--Select Doctor--"))
        self.comboBox_docname.setItemText(1, _translate("MainWindow", "Andy"))
        self.comboBox_docname.setItemText(2, _translate("MainWindow", "Charlie"))
        self.label_5.setText(_translate("MainWindow", "Doctor Name:"))
        self.label_2.setText(_translate("MainWindow", "User Name:"))
        self.label_userId.setText(_translate("MainWindow", "User Id-Value null"))
        self.pushButton_check_availability.setText(_translate("MainWindow", "Check Availability"))
        self.pushButton_confirm.setText(_translate("MainWindow", "Confirm Availability"))
from . import login_form_rc
