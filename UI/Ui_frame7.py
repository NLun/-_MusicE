# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\畢專\MusicE\PyQt5\UI\frame7.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame7(object):
    def setupUi(self, Frame7):
        Frame7.setObjectName("Frame7")
        Frame7.resize(1123, 794)
        Frame7.setMinimumSize(QtCore.QSize(1123, 794))
        Frame7.setMaximumSize(QtCore.QSize(1123, 794))
        self.centralwidget = QtWidgets.QWidget(Frame7)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_import = QtWidgets.QPushButton(self.centralwidget)
        self.menu_import.setEnabled(True)
        self.menu_import.setGeometry(QtCore.QRect(533, 81, 119, 33))
        self.menu_import.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_import.setText("")
        self.menu_import.setObjectName("menu_import")
        self.menu_selection = QtWidgets.QPushButton(self.centralwidget)
        self.menu_selection.setEnabled(True)
        self.menu_selection.setGeometry(QtCore.QRect(689, 81, 118, 33))
        self.menu_selection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_selection.setText("")
        self.menu_selection.setObjectName("menu_selection")
        self.menu_download = QtWidgets.QPushButton(self.centralwidget)
        self.menu_download.setEnabled(True)
        self.menu_download.setGeometry(QtCore.QRect(845, 81, 60, 33))
        self.menu_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_download.setText("")
        self.menu_download.setObjectName("menu_download")
        self.menu_finish = QtWidgets.QPushButton(self.centralwidget)
        self.menu_finish.setEnabled(False)
        self.menu_finish.setGeometry(QtCore.QRect(925, 67, 111, 51))
        self.menu_finish.setText("")
        self.menu_finish.setObjectName("menu_finish")
        self.menu_main = QtWidgets.QPushButton(self.centralwidget)
        self.menu_main.setEnabled(True)
        self.menu_main.setGeometry(QtCore.QRect(412, 80, 89, 34))
        self.menu_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_main.setMouseTracking(False)
        self.menu_main.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menu_main.setText("")
        self.menu_main.setObjectName("menu_main")
        self.btn_restart = QtWidgets.QPushButton(self.centralwidget)
        self.btn_restart.setGeometry(QtCore.QRect(378, 549, 162, 50))
        self.btn_restart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_restart.setText("")
        self.btn_restart.setObjectName("btn_restart")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(587, 549, 207, 51))
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setText("")
        self.btn_exit.setObjectName("btn_exit")
        Frame7.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame7)
        QtCore.QMetaObject.connectSlotsByName(Frame7)

    def retranslateUi(self, Frame7):
        _translate = QtCore.QCoreApplication.translate
        Frame7.setWindowTitle(_translate("Frame7", "MusicE"))

