# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QThread
from UI.Ui_frame1 import Ui_Frame1
from UI.Ui_frame2 import Ui_Frame2
from UI.Ui_frame3 import Ui_Frame3
from UI.Ui_frame4 import Ui_Frame4
from UI.Ui_frame5 import Ui_Frame5
from UI.Ui_frame6 import Ui_Frame6
from UI.Ui_frame7 import Ui_Frame7
from spleeter.separator import Separator
from omnizart.music import app as mapp
from omnizart.drum import app as dapp
from omnizart.vocal import app as vapp
import atexit
import sys
import shutil
import os
import pygame

pygame.init()

inst_select = [False, False, False]
filename = ''
vocalfile = ''
pianofile = ''
drumfile = ''
mod = ''


class moudel:

    def music_sep(inputfile):
        separator = Separator('spleeter:5stems', multiprocess=False)
        prediction = separator.separate_to_file(inputfile, 'music/output')

    def pred_vocal(vocalfile):
        vapp.transcribe(vocalfile, model_path=None, output='music/midi_output')

    def pred_piano(pianofile):
        mapp.transcribe(pianofile, model_path='Piano',
                        output='music/midi_output')

    def pred_drum(drumfile):
        dapp.transcribe(drumfile, model_path=None, output='music/midi_output')


# 多執行緒
class th_sep(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global filename
        moudel.music_sep(filename)


class th_pred(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global vocalfile, pianofile, drumfile, inst_select
        for i in range(0, 3):
            if inst_select[i] == True:
                if i == 0:
                    moudel.pred_vocal(vocalfile)
                elif i == 1:
                    moudel.pred_piano(pianofile)
                elif i == 2:
                    moudel.pred_drum(drumfile)


# 結束時清除資料
@atexit.register
def exit_cleanup():
    shutil.rmtree('music/midi_output')
    os.mkdir('music/midi_output')
    shutil.rmtree('music/output')
    os.mkdir('music/output')


# Frame1(main)
class ui_1(QtWidgets.QMainWindow):
    def __init__(self):
        super(ui_1, self).__init__()
        self.ui = Ui_Frame1()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('音之萃_MusicE')

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon('pic/icon.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load('pic/frame_01/BG_01.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # 物件樣式
        # menu
        self.ui.menu_main.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_main_on.png)}")
        self.ui.menu_import.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_import.png)}")
        self.ui.menu_selection.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_selection.png)}")
        self.ui.menu_download.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_download.png)}")
        self.ui.menu_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_finish.png)}")
        # btn
        self.ui.btn_start.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_01/btn_start.png)}")

        # 按鍵連接
        self.ui.btn_start.clicked.connect(self.btn_start_click)

    def btn_start_click(self):
        self.hide()
        self.ui2 = ui_2()
        self.ui2.show()


# Frame2(import)
class ui_2(QtWidgets.QMainWindow):
    def __init__(self):
        super(ui_2, self).__init__()
        self.ui = Ui_Frame2()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('音之萃_MusicE')

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon('pic/icon.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load('pic/frame_02/BG_02_1.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # 物件樣式
        # menu
        self.ui.menu_main.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_main.png)}")
        self.ui.menu_import.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_import_on.png)}")
        self.ui.menu_selection.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_selection.png)}")
        self.ui.menu_download.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_download.png)}")
        self.ui.menu_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_finish.png)}")
        # btn
        self.ui.btn_file.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_02/btn_file.png)}")
        self.ui.btn_selectinst.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_02/btn_selectinst.png)}")
        self.ui.btn_onestep.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_02/btn_onestep.png)}")
        # label
        self.ui.label_filepth.setStyleSheet(
            "QLabel{font: 18pt \"Microsoft JhengHei UI\";}")

        # 隱藏按鈕
        self.ui.btn_selectinst.setVisible(False)
        self.ui.btn_onestep.setVisible(False)

        # 按鍵連接
        self.ui.btn_file.clicked.connect(self.btn_file_click)
        self.ui.menu_main.clicked.connect(self.menu_main_click)
        self.ui.btn_onestep.clicked.connect(self.jump_onestep)
        self.ui.btn_selectinst.clicked.connect(self.jump_selectinst)

    def btn_file_click(self):
        global filename
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(
            self, '導入音檔', './', 'All Files(*.mp3 *.wav)')
        self.ui.label_filepth.setText(str(filename))
        self.ui.btn_file.setGeometry(495, 219, 140, 118)

        # 改背景
        image = QtGui.QPixmap()
        image.load('pic/frame_02/BG_02_2.png')
        image = image.scaled(self.width(), self.height())
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        self.ui.btn_selectinst.setVisible(True)
        self.ui.btn_onestep.setVisible(True)

    def menu_main_click(self):
        self.hide()
        self.ui1 = ui_1()
        self.ui1.show()

    def jump_selectinst(self):
        global filename
        if filename != '':
            global mod
            mod = 'select'
            self.hide()
            self.ui3 = ui_3()
            self.ui3.show()
        else:
            self.msgbox_check()

    def jump_onestep(self):
        global filename
        if filename != '':
            global mod
            mod = 'onestep'
            global inst_select
            inst_select = [True, True, True]
            self.hide()
            self.ui5 = ui_5()
            self.ui5.show()
        else:
            self.msgbox_check()

    def msgbox_check(self):
        msgbox = QtWidgets.QMessageBox.warning(
            self, '錯誤', '請選擇音檔！')


# Frame3(import_loading)
class ui_3(QtWidgets.QMainWindow):
    def __init__(self):
        super(ui_3, self).__init__()
        self.ui = Ui_Frame3()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('音之萃_MusicE')

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon('pic/icon.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load('pic/frame_03/BG_03.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # 物件樣式
        # menu
        self.ui.menu_main.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_main.png)}")
        self.ui.menu_import.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_import_on.png)}")
        self.ui.menu_selection.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_selection.png)}")
        self.ui.menu_download.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_download.png)}")
        self.ui.menu_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_finish.png)}")
        self.ui.label_loading1.setPixmap(
            QtGui.QPixmap("pic/frame_03/loading0.png"))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.sim_loading)
        self.total = 1
        self.sep = th_sep()
        self.sep.start()
        self.timer.start(1000)
        # global filename
        # moudel.music_sep(filename)

    def sim_loading(self):
        fn = "pic/frame_03/loading" + str(self.total % 3) + ".png"
        self.ui.label_loading1.setPixmap(
            QtGui.QPixmap(fn))
        self.total += 1
        if self.sep.isFinished() == True:
            self.timer.stop()
            self.jump_select()

    def jump_select(self):
        self.hide()
        self.ui4 = ui_4()
        self.ui4.show()


# Frame4(select_inst)
class ui_4(QtWidgets.QMainWindow):
    def __init__(self):
        super(ui_4, self).__init__()
        self.ui = Ui_Frame4()
        self.ui.setupUi(self)

        # 變數設定
        global filename
        temp = filename.split('/')[-1]
        sep_file = 'music/output/' + temp[:(len(temp)-4)]
        global vocalfile, pianofile, drumfile
        vocalfile = sep_file + '/vocals.wav'
        pianofile = sep_file + '/piano.wav'
        drumfile = sep_file + '/drums.wav'

        # MainWindow Title
        self.setWindowTitle('音之萃_MusicE')

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon('pic/icon.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load('pic/frame_04/BG_04.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # 物件樣式
        # menu
        self.ui.menu_main.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_main.png)}")
        self.ui.menu_import.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_import.png)}")
        self.ui.menu_selection.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_selection_on.png)}")
        self.ui.menu_download.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_download.png)}")
        self.ui.menu_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_finish.png)}")
        # btn
        self.ui.btn_vocal.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_vocal_off.png)}")
        self.ui.btn_vocal_play.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_play.png)}")
        self.ui.btn_vocal_stop.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_stop.png)}")
        self.ui.btn_piano.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_piano_off.png)}")
        self.ui.btn_piano_play.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_play.png)}")
        self.ui.btn_piano_stop.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_stop.png)}")
        self.ui.btn_drum.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_drum_off.png)}")
        self.ui.btn_drum_play.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_play.png)}")
        self.ui.btn_drum_stop.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_stop.png)}")
        self.ui.btn_confirm.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_04/btn_confirm.png)}")

        # 按鍵連接
        self.ui.menu_main.clicked.connect(self.menu_main_click)
        self.ui.menu_import.clicked.connect(self.menu_import_click)
        self.ui.btn_vocal.clicked.connect(lambda: self.inst_check(inst=0))
        self.ui.btn_piano.clicked.connect(lambda: self.inst_check(inst=1))
        self.ui.btn_drum.clicked.connect(lambda: self.inst_check(inst=2))
        self.ui.btn_confirm.clicked.connect(self.confirm_click)
        self.ui.btn_vocal_play.clicked.connect(
            lambda: self.play_audio(file=vocalfile, inst='vocal'))
        self.ui.btn_piano_play.clicked.connect(
            lambda: self.play_audio(file=pianofile, inst='piano'))
        self.ui.btn_drum_play.clicked.connect(
            lambda: self.play_audio(file=drumfile, inst='drum'))
        self.ui.btn_vocal_stop.clicked.connect(lambda: self.stop_audio())
        self.ui.btn_piano_stop.clicked.connect(lambda: self.stop_audio())
        self.ui.btn_drum_stop.clicked.connect(lambda: self.stop_audio())

        # 隱藏停止鍵
        self.ui.btn_drum_stop.setVisible(False)
        self.ui.btn_piano_stop.setVisible(False)
        self.ui.btn_vocal_stop.setVisible(False)

        # 重製選項
        self.selection = [False, False, False]

        # 計數器
        self.MUSIC_END = pygame.USEREVENT+1
        pygame.mixer.music.set_endevent(self.MUSIC_END)
        self.timer_checkEnd = QTimer(self)
        self.timer_checkEnd.timeout.connect(self.checkMusicEnd)

        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

    def inst_check(self, inst):
        self.selection[inst] = not self.selection[inst]
        # print(self.selection)
        if inst == 0:
            if self.selection[0] == True:
                self.ui.btn_vocal.setStyleSheet(
                    "QPushButton{border-image: url(pic/frame_04/btn_vocal_on.png)}")
            else:
                self.ui.btn_vocal.setStyleSheet(
                    "QPushButton{border-image: url(pic/frame_04/btn_vocal_off.png)}")
        if inst == 1:
            if self.selection[1] == True:
                self.ui.btn_piano.setStyleSheet(
                    "QPushButton{border-image: url(pic/frame_04/btn_piano_on.png)}")
            else:
                self.ui.btn_piano.setStyleSheet(
                    "QPushButton{border-image: url(pic/frame_04/btn_piano_off.png)}")
        if inst == 2:
            if self.selection[2] == True:
                self.ui.btn_drum.setStyleSheet(
                    "QPushButton{border-image: url(pic/frame_04/btn_drum_on.png)}")
            else:
                self.ui.btn_drum.setStyleSheet(
                    "QPushButton{border-image: url(pic/frame_04/btn_drum_off.png)}")

    def btnReset(self):
        self.ui.btn_drum_play.setVisible(True)
        self.ui.btn_piano_play.setVisible(True)
        self.ui.btn_vocal_play.setVisible(True)
        self.ui.btn_drum_stop.setVisible(False)
        self.ui.btn_piano_stop.setVisible(False)
        self.ui.btn_vocal_stop.setVisible(False)

    def play_audio(self, file, inst):
        self.btnReset()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        if inst == 'vocal':
            self.ui.btn_vocal_play.setVisible(False)
            self.ui.btn_vocal_stop.setVisible(True)
        elif inst == 'piano':
            self.ui.btn_piano_play.setVisible(False)
            self.ui.btn_piano_stop.setVisible(True)
        elif inst == 'drum':
            self.ui.btn_drum_play.setVisible(False)
            self.ui.btn_drum_stop.setVisible(True)
        self.timer_checkEnd.start(50)

    def stop_audio(self):
        pygame.mixer.music.stop()

    def checkMusicEnd(self):
        for event in pygame.event.get():
            if event.type == self.MUSIC_END:
                self.btnReset()
                self.timer_checkEnd.stop()

    def menu_main_click(self):
        self.hide()
        self.ui1 = ui_1()
        self.ui1.show()

    def menu_import_click(self):
        self.hide()
        self.ui2 = ui_2()
        self.ui2.show()

    def confirm_click(self):
        if self.selection == [False, False, False]:
            self.msgbox_check()
        else:
            global inst_select
            print("global:{}".format(inst_select))
            inst_select = self.selection
            print("change:{}".format(inst_select))
            self.hide()
            self.ui5 = ui_5()
            self.ui5.show()

    def msgbox_check(self):
        msgbox = QtWidgets.QMessageBox.warning(
            self, '錯誤', '至少選擇一樣樂器！')


# Frame5(predict_loading)
class ui_5(QtWidgets.QMainWindow):
    def __init__(self):
        super(ui_5, self).__init__()
        self.ui = Ui_Frame5()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('音之萃_MusicE')

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon('pic/icon.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load('pic/frame_05/BG_05.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # 物件樣式
        # menu
        self.ui.menu_main.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_main.png)}")
        self.ui.menu_import.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_import.png)}")
        self.ui.menu_selection.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_selection_on.png)}")
        self.ui.menu_download.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_download.png)}")
        self.ui.menu_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_finish.png)}")
        self.ui.label_loading2.setPixmap(
            QtGui.QPixmap("pic/frame_05/loading0.png"))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.sim_loading)
        self.total = 1
        self.pred = th_pred()
        self.pred.start()
        self.timer.start(1000)

    def sim_loading(self):
        fn = "pic/frame_05/loading" + str(self.total % 3) + ".png"
        self.ui.label_loading2.setPixmap(
            QtGui.QPixmap(fn))
        self.total += 1
        if self.pred.isFinished() == True:
            self.timer.stop()
            self.jump_download()

    def jump_download(self):
        self.hide()
        self.ui6 = ui_6()
        self.ui6.show()


# Frame6(download)
class ui_6(QtWidgets.QMainWindow):
    inst = []
    inst_num = 0

    def __init__(self):
        super(ui_6, self).__init__()
        self.ui = Ui_Frame6()
        self.ui.setupUi(self)

        # 變數初始化
        self.inst = []
        self.inst_num = 0

        # MainWindow Title
        self.setWindowTitle('音之萃_MusicE')

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon('pic/icon.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load('pic/frame_06/BG_06.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # 物件樣式
        # menu
        self.ui.menu_main.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_main.png)}")
        self.ui.menu_import.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_import.png)}")
        self.ui.menu_selection.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_selection.png)}")
        self.ui.menu_download.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_download_on.png)}")
        self.ui.menu_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_finish.png)}")
        # btn
        self.ui.btn_left.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_06/btn_left.png)}")
        self.ui.btn_right.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_06/btn_right.png)}")
        self.ui.btn_download.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_06/btn_download.png)}")
        self.ui.btn_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_06/btn_finish.png)}")

        # 更改樂器選擇enable
        global mod
        if mod == 'onestep':
            self.ui.menu_selection.setEnabled(False)

        # 取得所選樂器編號
        global inst_select
        for i in range(len(inst_select)):
            if inst_select[i] == True:
                self.inst.append(i)
        # 顯示第一順位被選擇的樂器
        self.ui.icon_instrument.setPixmap(
            QtGui.QPixmap("pic/frame_06/inst_" + str(self.inst[0]) + ".png"))
        self.inst_num = 0
        # 左方向鍵預設不顯示
        self.lr_visible_set()

        # 按鍵連接
        self.ui.menu_main.clicked.connect(self.menu_main_click)
        self.ui.menu_import.clicked.connect(self.menu_import_click)
        self.ui.menu_selection.clicked.connect(self.menu_selection_click)
        self.ui.btn_left.clicked.connect(
            lambda: self.icon_change(lr='l'))
        self.ui.btn_right.clicked.connect(
            lambda: self.icon_change(lr='r'))
        self.ui.btn_finish.clicked.connect(self.finish_click)
        self.ui.btn_download.clicked.connect(self.download_midifile)

    def icon_change(self, lr):
        global inst_select
        if lr == 'l':
            self.inst_num -= 1
            self.ui.icon_instrument.setPixmap(
                QtGui.QPixmap("pic/frame_06/inst_" + str(self.inst[self.inst_num]) + ".png"))
        elif lr == 'r':
            self.inst_num += 1
            self.ui.icon_instrument.setPixmap(
                QtGui.QPixmap("pic/frame_06/inst_" + str(self.inst[self.inst_num]) + ".png"))
        self.ui.btn_left.setVisible(True)
        self.ui.btn_right.setVisible(True)
        self.lr_visible_set()

        print(inst_select)
        print(self.inst)
        print(self.inst_num)

    def lr_visible_set(self):
        if self.inst_num == 0:
            self.ui.btn_left.setVisible(False)
        if self.inst_num == len(self.inst) - 1:
            self.ui.btn_right.setVisible(False)

    def download_midifile(self):
        if self.inst[self.inst_num] == 0:
            midifile = 'music/midi_output/vocals.mid'
        elif self.inst[self.inst_num] == 1:
            midifile = 'music/midi_output/piano.mid'
        elif self.inst[self.inst_num] == 2:
            midifile = 'music/midi_output/drums.mid'
        path, temp = QtWidgets.QFileDialog.getSaveFileName(
            self, '儲存檔案', './', 'All Files(*.mid)')
        print(midifile + '/' + path)
        if path != '':
            shutil.copyfile(midifile, path)

    def menu_main_click(self):
        self.hide()
        self.ui1 = ui_1()
        self.ui1.show()

    def menu_import_click(self):
        self.hide()
        self.ui2 = ui_2()
        self.ui2.show()

    def menu_selection_click(self):
        self.hide()
        self.ui4 = ui_4()
        self.ui4.show()

    def finish_click(self):
        self.hide()
        self.ui7 = ui_7()
        self.ui7.show()


# Frame7(finish)
class ui_7(QtWidgets.QMainWindow):
    inst = []
    inst_num = 0

    def __init__(self):
        super(ui_7, self).__init__()
        self.ui = Ui_Frame7()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('音之萃_MusicE')

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon('pic/icon.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load('pic/frame_07/BG_07.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # 物件樣式
        # menu
        self.ui.menu_main.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_main.png)}")
        self.ui.menu_import.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_import.png)}")
        self.ui.menu_selection.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_selection.png)}")
        self.ui.menu_download.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_download.png)}")
        self.ui.menu_finish.setStyleSheet(
            "QPushButton{border-image: url(pic/menu/menu_finish_on.png)}")
        # btn
        self.ui.btn_restart.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_07/btn_restart.png)}")
        self.ui.btn_exit.setStyleSheet(
            "QPushButton{border-image: url(pic/frame_07/btn_exit.png)}")

        # 更改樂器選擇enable
        global mod
        if mod == 'onestep':
            self.ui.menu_selection.setEnabled(False)

        # 按鍵連接
        self.ui.menu_main.clicked.connect(self.menu_main_click)
        self.ui.menu_import.clicked.connect(self.menu_import_click)
        self.ui.menu_selection.clicked.connect(self.menu_selection_click)
        self.ui.menu_download.clicked.connect(self.menu_download_click)
        self.ui.btn_restart.clicked.connect(self.menu_main_click)
        self.ui.btn_exit.clicked.connect(QtWidgets.qApp.quit)

    def menu_main_click(self):
        self.hide()
        self.ui1 = ui_1()
        self.ui1.show()

    def menu_import_click(self):
        self.hide()
        self.ui2 = ui_2()
        self.ui2.show()

    def menu_selection_click(self):
        self.hide()
        self.ui4 = ui_4()
        self.ui4.show()

    def menu_download_click(self):
        self.hide()
        self.ui6 = ui_6()
        self.ui6.show()


def main():
    app = QtWidgets.QApplication([])
    window = ui_1()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
