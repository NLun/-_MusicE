# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\畢專\MusicE\PyQt5\UI\frame1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame1(object):
    def setupUi(self, Frame1):
        Frame1.setObjectName("Frame1")
        Frame1.resize(1123, 794)
        Frame1.setMinimumSize(QtCore.QSize(1123, 794))
        Frame1.setMaximumSize(QtCore.QSize(1123, 794))
        self.centralwidget = QtWidgets.QWidget(Frame1)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(272, 584, 163, 51))
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setText("")
        self.btn_start.setObjectName("btn_start")
        self.menu_import = QtWidgets.QPushButton(self.centralwidget)
        self.menu_import.setEnabled(False)
        self.menu_import.setGeometry(QtCore.QRect(533, 81, 119, 33))
        self.menu_import.setText("")
        self.menu_import.setObjectName("menu_import")
        self.menu_selection = QtWidgets.QPushButton(self.centralwidget)
        self.menu_selection.setEnabled(False)
        self.menu_selection.setGeometry(QtCore.QRect(689, 81, 118, 33))
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
        self.menu_main.setGeometry(QtCore.QRect(380, 68, 138, 50))
        self.menu_main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menu_main.setMouseTracking(False)
        self.menu_main.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menu_main.setText("")
        self.menu_main.setObjectName("menu_main")
        Frame1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame1)
        QtCore.QMetaObject.connectSlotsByName(Frame1)

    def retranslateUi(self, Frame1):
        _translate = QtCore.QCoreApplication.translate
        Frame1.setWindowTitle(_translate("Frame1", "MusicE"))
