# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\畢專\MusicE\PyQt5\UI\frame2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame2(object):
    def setupUi(self, Frame2):
        Frame2.setObjectName("Frame2")
        Frame2.resize(1123, 794)
        Frame2.setMinimumSize(QtCore.QSize(1123, 794))
        Frame2.setMaximumSize(QtCore.QSize(1123, 794))
        self.centralwidget = QtWidgets.QWidget(Frame2)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file.setGeometry(QtCore.QRect(492, 288, 140, 118))
        self.btn_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_file.setText("")
        self.btn_file.setObjectName("btn_file")
        self.menu_import = QtWidgets.QPushButton(self.centralwidget)
        self.menu_import.setEnabled(False)
        self.menu_import.setGeometry(QtCore.QRect(519, 67, 155, 51))
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
        self.menu_main.setEnabled(True)
        self.menu_main.setGeometry(QtCore.QRect(412, 80, 89, 34))
        self.menu_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_main.setMouseTracking(False)
        self.menu_main.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menu_main.setText("")
        self.menu_main.setObjectName("menu_main")
        self.btn_selectinst = QtWidgets.QPushButton(self.centralwidget)
        self.btn_selectinst.setGeometry(QtCore.QRect(591, 591, 225, 80))
        self.btn_selectinst.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_selectinst.setText("")
        self.btn_selectinst.setObjectName("btn_selectinst")
        self.btn_onestep = QtWidgets.QPushButton(self.centralwidget)
        self.btn_onestep.setGeometry(QtCore.QRect(314, 615, 225, 54))
        self.btn_onestep.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_onestep.setText("")
        self.btn_onestep.setObjectName("btn_onestep")
        self.label_filepth = QtWidgets.QLabel(self.centralwidget)
        self.label_filepth.setGeometry(QtCore.QRect(275, 504, 600, 54))
        self.label_filepth.setText("")
        self.label_filepth.setObjectName("label_filepth")
        Frame2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame2)
        QtCore.QMetaObject.connectSlotsByName(Frame2)

    def retranslateUi(self, Frame2):
        _translate = QtCore.QCoreApplication.translate
        Frame2.setWindowTitle(_translate("Frame2", "MusicE"))

