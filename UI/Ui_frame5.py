# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\畢專\MusicE\PyQt5\UI\frame5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame5(object):
    def setupUi(self, Frame5):
        Frame5.setObjectName("Frame5")
        Frame5.resize(1123, 794)
        Frame5.setMinimumSize(QtCore.QSize(1123, 794))
        Frame5.setMaximumSize(QtCore.QSize(1123, 794))
        self.centralwidget = QtWidgets.QWidget(Frame5)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_import = QtWidgets.QPushButton(self.centralwidget)
        self.menu_import.setEnabled(False)
        self.menu_import.setGeometry(QtCore.QRect(533, 81, 119, 33))
        self.menu_import.setText("")
        self.menu_import.setObjectName("menu_import")
        self.menu_selection = QtWidgets.QPushButton(self.centralwidget)
        self.menu_selection.setEnabled(False)
        self.menu_selection.setGeometry(QtCore.QRect(669, 67, 151, 51))
        self.menu_selection.setText("")
        self.menu_selection.setObjectName("menu_selection")
        self.menu_download = QtWidgets.QPushButton(self.centralwidget)
        self.menu_download.setEnabled(False)
        self.menu_download.setGeometry(QtCore.QRect(845, 81, 60, 33))
        self.menu_download.setText("")
        self.menu_download.setObjectName("menu_download")
        self.menu_finish = QtWidgets.QPushButton(self.centralwidget)
        self.menu_finish.setEnabled(False)
        self.menu_finish.setGeometry(QtCore.QRect(949, 81, 59, 33))
        self.menu_finish.setText("")
        self.menu_finish.setObjectName("menu_finish")
        self.menu_main = QtWidgets.QPushButton(self.centralwidget)
        self.menu_main.setEnabled(False)
        self.menu_main.setGeometry(QtCore.QRect(412, 80, 89, 34))
        self.menu_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_main.setMouseTracking(False)
        self.menu_main.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menu_main.setText("")
        self.menu_main.setObjectName("menu_main")
        self.label_loading2 = QtWidgets.QLabel(self.centralwidget)
        self.label_loading2.setGeometry(QtCore.QRect(356, 267, 380, 54))
        self.label_loading2.setText("")
        self.label_loading2.setObjectName("label_loading2")
        Frame5.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame5)
        QtCore.QMetaObject.connectSlotsByName(Frame5)

    def retranslateUi(self, Frame5):
        _translate = QtCore.QCoreApplication.translate
        Frame5.setWindowTitle(_translate("Frame5", "MusicE"))

