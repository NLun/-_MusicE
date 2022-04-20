# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\畢專\MusicE\PyQt5\UI\frame3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame3(object):
    def setupUi(self, Frame3):
        Frame3.setObjectName("Frame3")
        Frame3.resize(1123, 794)
        Frame3.setMinimumSize(QtCore.QSize(1123, 794))
        Frame3.setMaximumSize(QtCore.QSize(1123, 794))
        self.centralwidget = QtWidgets.QWidget(Frame3)
        self.centralwidget.setObjectName("centralwidget")
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
        self.menu_main.setEnabled(False)
        self.menu_main.setGeometry(QtCore.QRect(412, 80, 89, 34))
        self.menu_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_main.setMouseTracking(False)
        self.menu_main.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menu_main.setText("")
        self.menu_main.setObjectName("menu_main")
        self.label_loading1 = QtWidgets.QLabel(self.centralwidget)
        self.label_loading1.setEnabled(True)
        self.label_loading1.setGeometry(QtCore.QRect(380, 294, 343, 54))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_loading1.sizePolicy().hasHeightForWidth())
        self.label_loading1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(48)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_loading1.setFont(font)
        self.label_loading1.setStyleSheet("")
        self.label_loading1.setText("")
        self.label_loading1.setObjectName("label_loading1")
        Frame3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame3)
        QtCore.QMetaObject.connectSlotsByName(Frame3)

    def retranslateUi(self, Frame3):
        _translate = QtCore.QCoreApplication.translate
        Frame3.setWindowTitle(_translate("Frame3", "MusicE"))

