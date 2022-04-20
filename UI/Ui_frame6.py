# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\畢專\MusicE\PyQt5\UI\frame6.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame6(object):
    def setupUi(self, Frame6):
        Frame6.setObjectName("Frame6")
        Frame6.resize(1123, 794)
        Frame6.setMinimumSize(QtCore.QSize(1123, 794))
        Frame6.setMaximumSize(QtCore.QSize(1123, 794))
        self.centralwidget = QtWidgets.QWidget(Frame6)
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
        self.menu_download.setEnabled(False)
        self.menu_download.setGeometry(QtCore.QRect(820, 68, 111, 50))
        self.menu_download.setText("")
        self.menu_download.setObjectName("menu_download")
        self.menu_finish = QtWidgets.QPushButton(self.centralwidget)
        self.menu_finish.setEnabled(False)
        self.menu_finish.setGeometry(QtCore.QRect(949, 81, 59, 33))
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
        self.btn_finish = QtWidgets.QPushButton(self.centralwidget)
        self.btn_finish.setGeometry(QtCore.QRect(492, 589, 138, 50))
        self.btn_finish.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_finish.setText("")
        self.btn_finish.setObjectName("btn_finish")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(707, 400, 49, 40))
        self.btn_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_right.setText("")
        self.btn_right.setObjectName("btn_right")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(369, 400, 49, 40))
        self.btn_left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_left.setText("")
        self.btn_left.setObjectName("btn_left")
        self.icon_instrument = QtWidgets.QLabel(self.centralwidget)
        self.icon_instrument.setGeometry(QtCore.QRect(492, 260, 141, 141))
        self.icon_instrument.setText("")
        self.icon_instrument.setObjectName("icon_instrument")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(529, 462, 67, 67))
        self.btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_download.setText("")
        self.btn_download.setObjectName("btn_download")
        Frame6.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame6)
        QtCore.QMetaObject.connectSlotsByName(Frame6)

    def retranslateUi(self, Frame6):
        _translate = QtCore.QCoreApplication.translate
        Frame6.setWindowTitle(_translate("Frame6", "MusicE"))

