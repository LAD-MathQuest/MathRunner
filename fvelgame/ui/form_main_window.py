# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QToolBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 946)
        self.action_Run = QAction(MainWindow)
        self.action_Run.setObjectName(u"action_Run")
        icon = QIcon()
        iconThemeName = u"media-playback-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Run.setIcon(icon)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        icon1 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Exit.setIcon(icon1)
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_About.setEnabled(False)
        icon2 = QIcon()
        iconThemeName = u"help-about"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_About.setIcon(icon2)
        self.action_Contents = QAction(MainWindow)
        self.action_Contents.setObjectName(u"action_Contents")
        self.action_Contents.setEnabled(False)
        icon3 = QIcon()
        iconThemeName = u"help-contents"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Contents.setIcon(icon3)
        self.action_Undo = QAction(MainWindow)
        self.action_Undo.setObjectName(u"action_Undo")
        self.action_Undo.setEnabled(False)
        icon4 = QIcon()
        iconThemeName = u"edit-undo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Undo.setIcon(icon4)
        self.action_Redo = QAction(MainWindow)
        self.action_Redo.setObjectName(u"action_Redo")
        self.action_Redo.setEnabled(False)
        icon5 = QIcon()
        iconThemeName = u"edit-redo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Redo.setIcon(icon5)
        self.action_Reset = QAction(MainWindow)
        self.action_Reset.setObjectName(u"action_Reset")
        self.action_Reset.setEnabled(False)
        icon6 = QIcon()
        iconThemeName = u"document-revert"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Reset.setIcon(icon6)
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        icon7 = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_New.setIcon(icon7)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        icon8 = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Open.setIcon(icon8)
        self.action_Save = QAction(MainWindow)
        self.action_Save.setObjectName(u"action_Save")
        self.action_Save.setEnabled(False)
        icon9 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon9 = QIcon.fromTheme(iconThemeName)
        else:
            icon9.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Save.setIcon(icon9)
        self.action_Build = QAction(MainWindow)
        self.action_Build.setObjectName(u"action_Build")
        self.action_Build.setEnabled(False)
        icon10 = QIcon()
        iconThemeName = u"application-x-executable"
        if QIcon.hasThemeIcon(iconThemeName):
            icon10 = QIcon.fromTheme(iconThemeName)
        else:
            icon10.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Build.setIcon(icon10)
        self.action_Save_as = QAction(MainWindow)
        self.action_Save_as.setObjectName(u"action_Save_as")
        self.action_Save_as.setEnabled(False)
        icon11 = QIcon()
        iconThemeName = u"document-save-as"
        if QIcon.hasThemeIcon(iconThemeName):
            icon11 = QIcon.fromTheme(iconThemeName)
        else:
            icon11.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Save_as.setIcon(icon11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget_Game = QTabWidget(self.centralwidget)
        self.tabWidget_Game.setObjectName(u"tabWidget_Game")
        self.tabWidget_Game.setEnabled(True)
        self.tabWidget_Game.setAutoFillBackground(True)
        self.tabGame = QWidget()
        self.tabGame.setObjectName(u"tabGame")
        self.tabGame.setEnabled(True)
        self.verticalLayout_10 = QVBoxLayout(self.tabGame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_Software = QGroupBox(self.tabGame)
        self.groupBox_Software.setObjectName(u"groupBox_Software")
        self.gridLayout_17 = QGridLayout(self.groupBox_Software)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_Author = QLabel(self.groupBox_Software)
        self.label_Author.setObjectName(u"label_Author")

        self.gridLayout_17.addWidget(self.label_Author, 1, 0, 1, 1)

        self.pushButton_IconSelect = QPushButton(self.groupBox_Software)
        self.pushButton_IconSelect.setObjectName(u"pushButton_IconSelect")

        self.gridLayout_17.addWidget(self.pushButton_IconSelect, 2, 0, 1, 1)

        self.lineEdit_GameName = QLineEdit(self.groupBox_Software)
        self.lineEdit_GameName.setObjectName(u"lineEdit_GameName")

        self.gridLayout_17.addWidget(self.lineEdit_GameName, 0, 1, 1, 1)

        self.label_GameName = QLabel(self.groupBox_Software)
        self.label_GameName.setObjectName(u"label_GameName")

        self.gridLayout_17.addWidget(self.label_GameName, 0, 0, 1, 1)

        self.label_GameDescription = QLabel(self.groupBox_Software)
        self.label_GameDescription.setObjectName(u"label_GameDescription")

        self.gridLayout_17.addWidget(self.label_GameDescription, 3, 0, 1, 1)

        self.lineEdit_Author = QLineEdit(self.groupBox_Software)
        self.lineEdit_Author.setObjectName(u"lineEdit_Author")

        self.gridLayout_17.addWidget(self.lineEdit_Author, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_GameIcon = QLabel(self.groupBox_Software)
        self.label_GameIcon.setObjectName(u"label_GameIcon")
        self.label_GameIcon.setMinimumSize(QSize(64, 64))
        self.label_GameIcon.setBaseSize(QSize(64, 64))
        self.label_GameIcon.setAutoFillBackground(True)
        self.label_GameIcon.setFrameShape(QFrame.Panel)
        self.label_GameIcon.setFrameShadow(QFrame.Sunken)
        self.label_GameIcon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_GameIcon)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_12)


        self.gridLayout_17.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.plainTextEdit_GameDescription = QPlainTextEdit(self.groupBox_Software)
        self.plainTextEdit_GameDescription.setObjectName(u"plainTextEdit_GameDescription")

        self.gridLayout_17.addWidget(self.plainTextEdit_GameDescription, 3, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_Software)

        self.groupBox_Game = QGroupBox(self.tabGame)
        self.groupBox_Game.setObjectName(u"groupBox_Game")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_Game)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_ScrollDirection = QLabel(self.groupBox_Game)
        self.label_ScrollDirection.setObjectName(u"label_ScrollDirection")

        self.horizontalLayout_7.addWidget(self.label_ScrollDirection)

        self.radioButton_VertialScrolling = QRadioButton(self.groupBox_Game)
        self.radioButton_VertialScrolling.setObjectName(u"radioButton_VertialScrolling")

        self.horizontalLayout_7.addWidget(self.radioButton_VertialScrolling)

        self.radioButton_HorizontalScrolling = QRadioButton(self.groupBox_Game)
        self.radioButton_HorizontalScrolling.setObjectName(u"radioButton_HorizontalScrolling")

        self.horizontalLayout_7.addWidget(self.radioButton_HorizontalScrolling)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_TrackKills = QCheckBox(self.groupBox_Game)
        self.checkBox_TrackKills.setObjectName(u"checkBox_TrackKills")

        self.horizontalLayout_8.addWidget(self.checkBox_TrackKills)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_ScoreTimeBonus = QLabel(self.groupBox_Game)
        self.label_ScoreTimeBonus.setObjectName(u"label_ScoreTimeBonus")

        self.horizontalLayout_15.addWidget(self.label_ScoreTimeBonus)

        self.doubleSpinBox_ScoreTimeBonus = QDoubleSpinBox(self.groupBox_Game)
        self.doubleSpinBox_ScoreTimeBonus.setObjectName(u"doubleSpinBox_ScoreTimeBonus")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_ScoreTimeBonus.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_ScoreTimeBonus.setSizePolicy(sizePolicy)
        self.doubleSpinBox_ScoreTimeBonus.setMinimumSize(QSize(60, 0))
        self.doubleSpinBox_ScoreTimeBonus.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_ScoreTimeBonus.setDecimals(6)
        self.doubleSpinBox_ScoreTimeBonus.setMinimum(-999999.999998999992386)
        self.doubleSpinBox_ScoreTimeBonus.setMaximum(999999.999998999992386)

        self.horizontalLayout_15.addWidget(self.doubleSpinBox_ScoreTimeBonus)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_AmbienceSound = QLabel(self.groupBox_Game)
        self.label_AmbienceSound.setObjectName(u"label_AmbienceSound")

        self.horizontalLayout_17.addWidget(self.label_AmbienceSound)

        self.pushButton_AmbienceSoundSelect = QPushButton(self.groupBox_Game)
        self.pushButton_AmbienceSoundSelect.setObjectName(u"pushButton_AmbienceSoundSelect")

        self.horizontalLayout_17.addWidget(self.pushButton_AmbienceSoundSelect)

        self.pushButton_AmbienceSoundRemove = QPushButton(self.groupBox_Game)
        self.pushButton_AmbienceSoundRemove.setObjectName(u"pushButton_AmbienceSoundRemove")
        self.pushButton_AmbienceSoundRemove.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.pushButton_AmbienceSoundRemove)

        self.pushButton_AmbienceSoundPlay = QPushButton(self.groupBox_Game)
        self.pushButton_AmbienceSoundPlay.setObjectName(u"pushButton_AmbienceSoundPlay")
        self.pushButton_AmbienceSoundPlay.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.pushButton_AmbienceSoundPlay)

        self.label_AmbienceSoundVolume = QLabel(self.groupBox_Game)
        self.label_AmbienceSoundVolume.setObjectName(u"label_AmbienceSoundVolume")
        self.label_AmbienceSoundVolume.setIndent(2)

        self.horizontalLayout_17.addWidget(self.label_AmbienceSoundVolume)

        self.doubleSpinBox_AmbienceSoundVolume = QDoubleSpinBox(self.groupBox_Game)
        self.doubleSpinBox_AmbienceSoundVolume.setObjectName(u"doubleSpinBox_AmbienceSoundVolume")
        self.doubleSpinBox_AmbienceSoundVolume.setEnabled(False)
        self.doubleSpinBox_AmbienceSoundVolume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_AmbienceSoundVolume.setMaximum(1.000000000000000)
        self.doubleSpinBox_AmbienceSoundVolume.setSingleStep(0.100000000000000)
        self.doubleSpinBox_AmbienceSoundVolume.setValue(1.000000000000000)

        self.horizontalLayout_17.addWidget(self.doubleSpinBox_AmbienceSoundVolume)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)


        self.verticalLayout_10.addWidget(self.groupBox_Game)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.tabWidget_Game.addTab(self.tabGame, "")
        self.tabAppearance = QWidget()
        self.tabAppearance.setObjectName(u"tabAppearance")
        self.verticalLayout_9 = QVBoxLayout(self.tabAppearance)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_Appearance = QScrollArea(self.tabAppearance)
        self.scrollArea_Appearance.setObjectName(u"scrollArea_Appearance")
        self.scrollArea_Appearance.setFrameShape(QFrame.NoFrame)
        self.scrollArea_Appearance.setFrameShadow(QFrame.Plain)
        self.scrollArea_Appearance.setWidgetResizable(True)
        self.scrollAreaWidgetContents_Appearance = QWidget()
        self.scrollAreaWidgetContents_Appearance.setObjectName(u"scrollAreaWidgetContents_Appearance")
        self.scrollAreaWidgetContents_Appearance.setGeometry(QRect(0, 0, 904, 795))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_Appearance)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_Background = QGroupBox(self.scrollAreaWidgetContents_Appearance)
        self.groupBox_Background.setObjectName(u"groupBox_Background")
        self.groupBox_Background.setFlat(False)
        self.gridLayout_15 = QGridLayout(self.groupBox_Background)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_SelectBackgroundImage = QPushButton(self.groupBox_Background)
        self.pushButton_SelectBackgroundImage.setObjectName(u"pushButton_SelectBackgroundImage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_SelectBackgroundImage.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectBackgroundImage.setSizePolicy(sizePolicy1)
        self.pushButton_SelectBackgroundImage.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_20.addWidget(self.pushButton_SelectBackgroundImage)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)


        self.verticalLayout_18.addLayout(self.horizontalLayout_20)

        self.checkBox_BackgroundImageScrolls = QCheckBox(self.groupBox_Background)
        self.checkBox_BackgroundImageScrolls.setObjectName(u"checkBox_BackgroundImageScrolls")

        self.verticalLayout_18.addWidget(self.checkBox_BackgroundImageScrolls)

        self.verticalSpacer_17 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_17)


        self.gridLayout_15.addLayout(self.verticalLayout_18, 0, 1, 1, 1)

        self.label_BackgroundImage = QLabel(self.groupBox_Background)
        self.label_BackgroundImage.setObjectName(u"label_BackgroundImage")
        sizePolicy1.setHeightForWidth(self.label_BackgroundImage.sizePolicy().hasHeightForWidth())
        self.label_BackgroundImage.setSizePolicy(sizePolicy1)
        self.label_BackgroundImage.setMinimumSize(QSize(228, 128))
        self.label_BackgroundImage.setMaximumSize(QSize(228, 128))
#if QT_CONFIG(accessibility)
        self.label_BackgroundImage.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_BackgroundImage.setAutoFillBackground(True)
        self.label_BackgroundImage.setFrameShape(QFrame.Panel)
        self.label_BackgroundImage.setFrameShadow(QFrame.Sunken)
        self.label_BackgroundImage.setScaledContents(False)
        self.label_BackgroundImage.setAlignment(Qt.AlignCenter)
        self.label_BackgroundImage.setMargin(2)
        self.label_BackgroundImage.setIndent(0)

        self.gridLayout_15.addWidget(self.label_BackgroundImage, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.groupBox_Background)

        self.groupBox_Track = QGroupBox(self.scrollAreaWidgetContents_Appearance)
        self.groupBox_Track.setObjectName(u"groupBox_Track")
        self.gridLayout_16 = QGridLayout(self.groupBox_Track)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.checkBox_DrawTrack = QCheckBox(self.groupBox_Track)
        self.checkBox_DrawTrack.setObjectName(u"checkBox_DrawTrack")

        self.verticalLayout_19.addWidget(self.checkBox_DrawTrack)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_SelectTrackImage = QPushButton(self.groupBox_Track)
        self.pushButton_SelectTrackImage.setObjectName(u"pushButton_SelectTrackImage")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectTrackImage.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectTrackImage.setSizePolicy(sizePolicy1)
        self.pushButton_SelectTrackImage.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_SelectTrackImage)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)


        self.verticalLayout_19.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_19 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_19)


        self.gridLayout_16.addLayout(self.verticalLayout_19, 1, 1, 1, 1)

        self.label_TrackImage = QLabel(self.groupBox_Track)
        self.label_TrackImage.setObjectName(u"label_TrackImage")
        sizePolicy1.setHeightForWidth(self.label_TrackImage.sizePolicy().hasHeightForWidth())
        self.label_TrackImage.setSizePolicy(sizePolicy1)
        self.label_TrackImage.setMinimumSize(QSize(228, 128))
        self.label_TrackImage.setMaximumSize(QSize(228, 128))
#if QT_CONFIG(accessibility)
        self.label_TrackImage.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_TrackImage.setAutoFillBackground(True)
        self.label_TrackImage.setFrameShape(QFrame.Panel)
        self.label_TrackImage.setFrameShadow(QFrame.Sunken)
        self.label_TrackImage.setScaledContents(False)
        self.label_TrackImage.setAlignment(Qt.AlignCenter)
        self.label_TrackImage.setMargin(2)
        self.label_TrackImage.setIndent(0)

        self.gridLayout_16.addWidget(self.label_TrackImage, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.groupBox_Track)

        self.groupBox_Scoreboard = QGroupBox(self.scrollAreaWidgetContents_Appearance)
        self.groupBox_Scoreboard.setObjectName(u"groupBox_Scoreboard")
        self.gridLayout_18 = QGridLayout(self.groupBox_Scoreboard)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_ScoreboardImage = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardImage.setObjectName(u"label_ScoreboardImage")
        sizePolicy1.setHeightForWidth(self.label_ScoreboardImage.sizePolicy().hasHeightForWidth())
        self.label_ScoreboardImage.setSizePolicy(sizePolicy1)
        self.label_ScoreboardImage.setMinimumSize(QSize(228, 128))
        self.label_ScoreboardImage.setMaximumSize(QSize(228, 128))
        self.label_ScoreboardImage.setAutoFillBackground(True)
        self.label_ScoreboardImage.setFrameShape(QFrame.Panel)
        self.label_ScoreboardImage.setFrameShadow(QFrame.Sunken)
        self.label_ScoreboardImage.setScaledContents(False)
        self.label_ScoreboardImage.setAlignment(Qt.AlignCenter)
        self.label_ScoreboardImage.setMargin(2)
        self.label_ScoreboardImage.setIndent(0)

        self.verticalLayout_12.addWidget(self.label_ScoreboardImage)

        self.label_ScoreboardExample = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardExample.setObjectName(u"label_ScoreboardExample")
        sizePolicy1.setHeightForWidth(self.label_ScoreboardExample.sizePolicy().hasHeightForWidth())
        self.label_ScoreboardExample.setSizePolicy(sizePolicy1)
        self.label_ScoreboardExample.setMinimumSize(QSize(228, 26))
        self.label_ScoreboardExample.setBaseSize(QSize(26, 26))
        self.label_ScoreboardExample.setAutoFillBackground(True)
        self.label_ScoreboardExample.setFrameShape(QFrame.Panel)
        self.label_ScoreboardExample.setFrameShadow(QFrame.Sunken)
        self.label_ScoreboardExample.setAlignment(Qt.AlignCenter)
        self.label_ScoreboardExample.setMargin(0)
        self.label_ScoreboardExample.setIndent(0)

        self.verticalLayout_12.addWidget(self.label_ScoreboardExample)

        self.verticalSpacer_18 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_18)


        self.gridLayout_18.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.groupBox_ScoreboardImage = QGroupBox(self.groupBox_Scoreboard)
        self.groupBox_ScoreboardImage.setObjectName(u"groupBox_ScoreboardImage")
        self.verticalLayout = QVBoxLayout(self.groupBox_ScoreboardImage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_SelectScoreboardImage = QPushButton(self.groupBox_ScoreboardImage)
        self.pushButton_SelectScoreboardImage.setObjectName(u"pushButton_SelectScoreboardImage")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectScoreboardImage.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectScoreboardImage.setSizePolicy(sizePolicy1)
        self.pushButton_SelectScoreboardImage.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_9.addWidget(self.pushButton_SelectScoreboardImage)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_25)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.spinBox_ScoreboardImageWidth = QSpinBox(self.groupBox_ScoreboardImage)
        self.spinBox_ScoreboardImageWidth.setObjectName(u"spinBox_ScoreboardImageWidth")
        self.spinBox_ScoreboardImageWidth.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardImageWidth.setMinimum(1)
        self.spinBox_ScoreboardImageWidth.setMaximum(1920)

        self.gridLayout_13.addWidget(self.spinBox_ScoreboardImageWidth, 1, 1, 1, 1)

        self.checkBox_ScoreboardImageKeepAspectRatio = QCheckBox(self.groupBox_ScoreboardImage)
        self.checkBox_ScoreboardImageKeepAspectRatio.setObjectName(u"checkBox_ScoreboardImageKeepAspectRatio")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_ScoreboardImageKeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_ScoreboardImageKeepAspectRatio.setSizePolicy(sizePolicy2)

        self.gridLayout_13.addWidget(self.checkBox_ScoreboardImageKeepAspectRatio, 1, 4, 1, 1)

        self.label_ScoreboardImageWidth = QLabel(self.groupBox_ScoreboardImage)
        self.label_ScoreboardImageWidth.setObjectName(u"label_ScoreboardImageWidth")
        self.label_ScoreboardImageWidth.setIndent(5)

        self.gridLayout_13.addWidget(self.label_ScoreboardImageWidth, 1, 0, 1, 1)

        self.label_ScoreboardImagePosition = QLabel(self.groupBox_ScoreboardImage)
        self.label_ScoreboardImagePosition.setObjectName(u"label_ScoreboardImagePosition")
        self.label_ScoreboardImagePosition.setIndent(5)

        self.gridLayout_13.addWidget(self.label_ScoreboardImagePosition, 0, 0, 1, 1)

        self.spinBox_ScoreboardImagePositionX = QSpinBox(self.groupBox_ScoreboardImage)
        self.spinBox_ScoreboardImagePositionX.setObjectName(u"spinBox_ScoreboardImagePositionX")
        self.spinBox_ScoreboardImagePositionX.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardImagePositionX.setMinimum(1)
        self.spinBox_ScoreboardImagePositionX.setMaximum(1920)

        self.gridLayout_13.addWidget(self.spinBox_ScoreboardImagePositionX, 0, 1, 1, 1)

        self.spinBox_ScoreboardImagePositionY = QSpinBox(self.groupBox_ScoreboardImage)
        self.spinBox_ScoreboardImagePositionY.setObjectName(u"spinBox_ScoreboardImagePositionY")
        self.spinBox_ScoreboardImagePositionY.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardImagePositionY.setMinimum(1)
        self.spinBox_ScoreboardImagePositionY.setMaximum(1080)

        self.gridLayout_13.addWidget(self.spinBox_ScoreboardImagePositionY, 0, 2, 1, 1)

        self.spinBox_ScoreboardImageHeight = QSpinBox(self.groupBox_ScoreboardImage)
        self.spinBox_ScoreboardImageHeight.setObjectName(u"spinBox_ScoreboardImageHeight")
        self.spinBox_ScoreboardImageHeight.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardImageHeight.setMinimum(1)
        self.spinBox_ScoreboardImageHeight.setMaximum(1080)

        self.gridLayout_13.addWidget(self.spinBox_ScoreboardImageHeight, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_13)


        self.verticalLayout_20.addWidget(self.groupBox_ScoreboardImage)

        self.groupBox_ScoreboardText = QGroupBox(self.groupBox_Scoreboard)
        self.groupBox_ScoreboardText.setObjectName(u"groupBox_ScoreboardText")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_ScoreboardText)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_ScoreboardTextWidth = QLabel(self.groupBox_ScoreboardText)
        self.label_ScoreboardTextWidth.setObjectName(u"label_ScoreboardTextWidth")
        self.label_ScoreboardTextWidth.setIndent(5)

        self.gridLayout_14.addWidget(self.label_ScoreboardTextWidth, 1, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_13, 0, 3, 1, 1)

        self.spinBox_ScoreboardTextWidth = QSpinBox(self.groupBox_ScoreboardText)
        self.spinBox_ScoreboardTextWidth.setObjectName(u"spinBox_ScoreboardTextWidth")
        self.spinBox_ScoreboardTextWidth.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardTextWidth.setMinimum(1)
        self.spinBox_ScoreboardTextWidth.setMaximum(1920)

        self.gridLayout_14.addWidget(self.spinBox_ScoreboardTextWidth, 1, 1, 1, 1)

        self.label_ScoreboardTextPosition = QLabel(self.groupBox_ScoreboardText)
        self.label_ScoreboardTextPosition.setObjectName(u"label_ScoreboardTextPosition")
        self.label_ScoreboardTextPosition.setIndent(5)

        self.gridLayout_14.addWidget(self.label_ScoreboardTextPosition, 0, 0, 1, 1)

        self.spinBox_ScoreboardTextPositionY = QSpinBox(self.groupBox_ScoreboardText)
        self.spinBox_ScoreboardTextPositionY.setObjectName(u"spinBox_ScoreboardTextPositionY")
        self.spinBox_ScoreboardTextPositionY.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardTextPositionY.setMinimum(1)
        self.spinBox_ScoreboardTextPositionY.setMaximum(1080)

        self.gridLayout_14.addWidget(self.spinBox_ScoreboardTextPositionY, 0, 2, 1, 1)

        self.spinBox_ScoreboardTextHeight = QSpinBox(self.groupBox_ScoreboardText)
        self.spinBox_ScoreboardTextHeight.setObjectName(u"spinBox_ScoreboardTextHeight")
        self.spinBox_ScoreboardTextHeight.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardTextHeight.setMinimum(1)
        self.spinBox_ScoreboardTextHeight.setMaximum(1080)

        self.gridLayout_14.addWidget(self.spinBox_ScoreboardTextHeight, 1, 2, 1, 1)

        self.spinBox_ScoreboardTextPositionX = QSpinBox(self.groupBox_ScoreboardText)
        self.spinBox_ScoreboardTextPositionX.setObjectName(u"spinBox_ScoreboardTextPositionX")
        self.spinBox_ScoreboardTextPositionX.setMinimumSize(QSize(60, 0))
        self.spinBox_ScoreboardTextPositionX.setMinimum(1)
        self.spinBox_ScoreboardTextPositionX.setMaximum(1920)

        self.gridLayout_14.addWidget(self.spinBox_ScoreboardTextPositionX, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_14)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.groupBox_ScoreboardText)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_ChoseScoreboardBgColor = QPushButton(self.groupBox_ScoreboardText)
        self.pushButton_ChoseScoreboardBgColor.setObjectName(u"pushButton_ChoseScoreboardBgColor")
        sizePolicy1.setHeightForWidth(self.pushButton_ChoseScoreboardBgColor.sizePolicy().hasHeightForWidth())
        self.pushButton_ChoseScoreboardBgColor.setSizePolicy(sizePolicy1)
        self.pushButton_ChoseScoreboardBgColor.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_ChoseScoreboardBgColor)

        self.pushButton_ChoseScoreboardFgColor = QPushButton(self.groupBox_ScoreboardText)
        self.pushButton_ChoseScoreboardFgColor.setObjectName(u"pushButton_ChoseScoreboardFgColor")
        sizePolicy1.setHeightForWidth(self.pushButton_ChoseScoreboardFgColor.sizePolicy().hasHeightForWidth())
        self.pushButton_ChoseScoreboardFgColor.setSizePolicy(sizePolicy1)
        self.pushButton_ChoseScoreboardFgColor.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_ChoseScoreboardFgColor)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_20.addWidget(self.groupBox_ScoreboardText)


        self.gridLayout_18.addLayout(self.verticalLayout_20, 0, 3, 1, 1)


        self.verticalLayout_13.addWidget(self.groupBox_Scoreboard)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.scrollArea_Appearance.setWidget(self.scrollAreaWidgetContents_Appearance)

        self.verticalLayout_9.addWidget(self.scrollArea_Appearance)

        self.tabWidget_Game.addTab(self.tabAppearance, "")
        self.tabObjects = QWidget()
        self.tabObjects.setObjectName(u"tabObjects")
        self.tabObjects.setEnabled(True)
        self.verticalLayout_11 = QVBoxLayout(self.tabObjects)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget_Objects = QTabWidget(self.tabObjects)
        self.tabWidget_Objects.setObjectName(u"tabWidget_Objects")
        self.tab_Player = QWidget()
        self.tab_Player.setObjectName(u"tab_Player")
        self.verticalLayout_21 = QVBoxLayout(self.tab_Player)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame = QFrame(self.tab_Player)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_PlayerImage = QLabel(self.frame)
        self.label_PlayerImage.setObjectName(u"label_PlayerImage")
        sizePolicy1.setHeightForWidth(self.label_PlayerImage.sizePolicy().hasHeightForWidth())
        self.label_PlayerImage.setSizePolicy(sizePolicy1)
        self.label_PlayerImage.setMinimumSize(QSize(128, 128))
        self.label_PlayerImage.setMaximumSize(QSize(128, 128))
        self.label_PlayerImage.setAutoFillBackground(True)
        self.label_PlayerImage.setFrameShape(QFrame.Panel)
        self.label_PlayerImage.setFrameShadow(QFrame.Sunken)
        self.label_PlayerImage.setScaledContents(False)
        self.label_PlayerImage.setAlignment(Qt.AlignCenter)
        self.label_PlayerImage.setIndent(0)

        self.horizontalLayout_12.addWidget(self.label_PlayerImage)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_SelectPlayerImage = QPushButton(self.frame)
        self.pushButton_SelectPlayerImage.setObjectName(u"pushButton_SelectPlayerImage")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectPlayerImage.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectPlayerImage.setSizePolicy(sizePolicy1)
        self.pushButton_SelectPlayerImage.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_16.addWidget(self.pushButton_SelectPlayerImage)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_14)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_PlayerSpeed = QLabel(self.frame)
        self.label_PlayerSpeed.setObjectName(u"label_PlayerSpeed")
        self.label_PlayerSpeed.setMargin(1)
        self.label_PlayerSpeed.setIndent(5)

        self.gridLayout_19.addWidget(self.label_PlayerSpeed, 1, 0, 1, 1)

        self.spinBox_PlayerSpeed = QSpinBox(self.frame)
        self.spinBox_PlayerSpeed.setObjectName(u"spinBox_PlayerSpeed")
        self.spinBox_PlayerSpeed.setMinimum(1)
        self.spinBox_PlayerSpeed.setMaximum(1920)

        self.gridLayout_19.addWidget(self.spinBox_PlayerSpeed, 1, 1, 1, 1)

        self.spinBox_PlayerHeight = QSpinBox(self.frame)
        self.spinBox_PlayerHeight.setObjectName(u"spinBox_PlayerHeight")
        self.spinBox_PlayerHeight.setMinimumSize(QSize(60, 0))
        self.spinBox_PlayerHeight.setMinimum(1)
        self.spinBox_PlayerHeight.setMaximum(1080)

        self.gridLayout_19.addWidget(self.spinBox_PlayerHeight, 0, 2, 1, 1)

        self.label_PlayerSize = QLabel(self.frame)
        self.label_PlayerSize.setObjectName(u"label_PlayerSize")
        self.label_PlayerSize.setMinimumSize(QSize(50, 0))
        self.label_PlayerSize.setMargin(1)
        self.label_PlayerSize.setIndent(5)

        self.gridLayout_19.addWidget(self.label_PlayerSize, 0, 0, 1, 1)

        self.checkBox_PlayerKeepAspectRatio = QCheckBox(self.frame)
        self.checkBox_PlayerKeepAspectRatio.setObjectName(u"checkBox_PlayerKeepAspectRatio")
        sizePolicy2.setHeightForWidth(self.checkBox_PlayerKeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_PlayerKeepAspectRatio.setSizePolicy(sizePolicy2)

        self.gridLayout_19.addWidget(self.checkBox_PlayerKeepAspectRatio, 0, 3, 1, 1)

        self.spinBox_PlayerWidth = QSpinBox(self.frame)
        self.spinBox_PlayerWidth.setObjectName(u"spinBox_PlayerWidth")
        self.spinBox_PlayerWidth.setMinimumSize(QSize(60, 0))
        self.spinBox_PlayerWidth.setMinimum(1)
        self.spinBox_PlayerWidth.setMaximum(1920)

        self.gridLayout_19.addWidget(self.spinBox_PlayerWidth, 0, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_19)

        self.verticalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_7)


        self.horizontalLayout_12.addLayout(self.verticalLayout_14)


        self.verticalLayout_21.addWidget(self.frame)

        self.verticalSpacer_25 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_25)

        self.verticalSpacer_26 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_26)

        self.verticalSpacer_24 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_24)

        self.verticalSpacer_15 = QSpacerItem(20, 128, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_15)

        self.tabWidget_Objects.addTab(self.tab_Player, "")
        self.tab_Obstacles = QWidget()
        self.tab_Obstacles.setObjectName(u"tab_Obstacles")
        self.verticalLayout_22 = QVBoxLayout(self.tab_Obstacles)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_ObstacleFrequency = QHBoxLayout()
        self.horizontalLayout_ObstacleFrequency.setObjectName(u"horizontalLayout_ObstacleFrequency")
        self.label_ObstacleFrequency = QLabel(self.tab_Obstacles)
        self.label_ObstacleFrequency.setObjectName(u"label_ObstacleFrequency")
        self.label_ObstacleFrequency.setMinimumSize(QSize(140, 0))
        self.label_ObstacleFrequency.setMargin(1)
        self.label_ObstacleFrequency.setIndent(2)

        self.horizontalLayout_ObstacleFrequency.addWidget(self.label_ObstacleFrequency)

        self.doubleSpinBox_ObstaclesFrequency = QDoubleSpinBox(self.tab_Obstacles)
        self.doubleSpinBox_ObstaclesFrequency.setObjectName(u"doubleSpinBox_ObstaclesFrequency")
        self.doubleSpinBox_ObstaclesFrequency.setMinimumSize(QSize(60, 0))
        self.doubleSpinBox_ObstaclesFrequency.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_ObstaclesFrequency.setMinimum(0.010000000000000)
        self.doubleSpinBox_ObstaclesFrequency.setValue(1.000000000000000)

        self.horizontalLayout_ObstacleFrequency.addWidget(self.doubleSpinBox_ObstaclesFrequency)

        self.horizontalSpacer_ObstacleFrequency = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_ObstacleFrequency.addItem(self.horizontalSpacer_ObstacleFrequency)


        self.verticalLayout_22.addLayout(self.horizontalLayout_ObstacleFrequency)

        self.scrollArea_Obstacles = QScrollArea(self.tab_Obstacles)
        self.scrollArea_Obstacles.setObjectName(u"scrollArea_Obstacles")
        self.scrollArea_Obstacles.setFrameShape(QFrame.NoFrame)
        self.scrollArea_Obstacles.setFrameShadow(QFrame.Plain)
        self.scrollArea_Obstacles.setWidgetResizable(True)
        self.scrollAreaWidgetContents_Obstacle = QWidget()
        self.scrollAreaWidgetContents_Obstacle.setObjectName(u"scrollAreaWidgetContents_Obstacle")
        self.scrollAreaWidgetContents_Obstacle.setGeometry(QRect(0, 0, 882, 676))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_Obstacle)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_ObstacleFrequency_1 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_ObstacleFrequency_1)

        self.verticalSpacer_ObstacleFrequency_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_ObstacleFrequency_2)

        self.verticalSpacer_ObstacleFrequency_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_ObstacleFrequency_3)

        self.verticalSpacer_ObstacleFrequency_4 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_ObstacleFrequency_4)

        self.scrollArea_Obstacles.setWidget(self.scrollAreaWidgetContents_Obstacle)

        self.verticalLayout_22.addWidget(self.scrollArea_Obstacles)

        self.horizontalLayout_ObstacleNew = QHBoxLayout()
        self.horizontalLayout_ObstacleNew.setObjectName(u"horizontalLayout_ObstacleNew")
        self.horizontalSpacer_ObstacleNew = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_ObstacleNew.addItem(self.horizontalSpacer_ObstacleNew)

        self.pushButton_NewObstacle = QPushButton(self.tab_Obstacles)
        self.pushButton_NewObstacle.setObjectName(u"pushButton_NewObstacle")

        self.horizontalLayout_ObstacleNew.addWidget(self.pushButton_NewObstacle)


        self.verticalLayout_22.addLayout(self.horizontalLayout_ObstacleNew)

        self.tabWidget_Objects.addTab(self.tab_Obstacles, "")
        self.tab_Collectibles = QWidget()
        self.tab_Collectibles.setObjectName(u"tab_Collectibles")
        self.verticalLayout_23 = QVBoxLayout(self.tab_Collectibles)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_CollectiblesFrequency = QLabel(self.tab_Collectibles)
        self.label_CollectiblesFrequency.setObjectName(u"label_CollectiblesFrequency")
        self.label_CollectiblesFrequency.setMinimumSize(QSize(140, 0))
        self.label_CollectiblesFrequency.setMargin(1)
        self.label_CollectiblesFrequency.setIndent(2)

        self.horizontalLayout_4.addWidget(self.label_CollectiblesFrequency)

        self.doubleSpinBox_CollectiblesFrequency = QDoubleSpinBox(self.tab_Collectibles)
        self.doubleSpinBox_CollectiblesFrequency.setObjectName(u"doubleSpinBox_CollectiblesFrequency")
        self.doubleSpinBox_CollectiblesFrequency.setMinimumSize(QSize(60, 0))
        self.doubleSpinBox_CollectiblesFrequency.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_CollectiblesFrequency.setMinimum(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_CollectiblesFrequency)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_23.addLayout(self.horizontalLayout_4)

        self.scrollArea_Collectibles = QScrollArea(self.tab_Collectibles)
        self.scrollArea_Collectibles.setObjectName(u"scrollArea_Collectibles")
        self.scrollArea_Collectibles.setFrameShape(QFrame.NoFrame)
        self.scrollArea_Collectibles.setFrameShadow(QFrame.Plain)
        self.scrollArea_Collectibles.setWidgetResizable(True)
        self.scrollAreaWidgetContents_Collectibles = QWidget()
        self.scrollAreaWidgetContents_Collectibles.setObjectName(u"scrollAreaWidgetContents_Collectibles")
        self.scrollAreaWidgetContents_Collectibles.setGeometry(QRect(0, 0, 882, 676))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_Collectibles)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_13 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_13)

        self.verticalSpacer_14 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_14)

        self.verticalSpacer_12 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_12)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.scrollArea_Collectibles.setWidget(self.scrollAreaWidgetContents_Collectibles)

        self.verticalLayout_23.addWidget(self.scrollArea_Collectibles)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pushButton_NewCollectible = QPushButton(self.tab_Collectibles)
        self.pushButton_NewCollectible.setObjectName(u"pushButton_NewCollectible")

        self.horizontalLayout_5.addWidget(self.pushButton_NewCollectible)


        self.verticalLayout_23.addLayout(self.horizontalLayout_5)

        self.tabWidget_Objects.addTab(self.tab_Collectibles, "")

        self.verticalLayout_11.addWidget(self.tabWidget_Objects)

        self.tabWidget_Game.addTab(self.tabObjects, "")
        self.tabVelocity = QWidget()
        self.tabVelocity.setObjectName(u"tabVelocity")
        self.tabVelocity.setEnabled(True)
        self.layout_TabVelocity = QHBoxLayout(self.tabVelocity)
        self.layout_TabVelocity.setObjectName(u"layout_TabVelocity")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.doubleSpinBox_VelocityA = QDoubleSpinBox(self.tabVelocity)
        self.doubleSpinBox_VelocityA.setObjectName(u"doubleSpinBox_VelocityA")
        self.doubleSpinBox_VelocityA.setMinimumSize(QSize(90, 0))
        self.doubleSpinBox_VelocityA.setDecimals(3)

        self.gridLayout_7.addWidget(self.doubleSpinBox_VelocityA, 0, 1, 1, 1)

        self.label_VelocityA = QLabel(self.tabVelocity)
        self.label_VelocityA.setObjectName(u"label_VelocityA")
        self.label_VelocityA.setMinimumSize(QSize(40, 0))
        self.label_VelocityA.setAlignment(Qt.AlignCenter)
        self.label_VelocityA.setIndent(2)

        self.gridLayout_7.addWidget(self.label_VelocityA, 0, 0, 1, 1)

        self.label_VelocityB = QLabel(self.tabVelocity)
        self.label_VelocityB.setObjectName(u"label_VelocityB")
        self.label_VelocityB.setMinimumSize(QSize(40, 0))
        self.label_VelocityB.setAlignment(Qt.AlignCenter)
        self.label_VelocityB.setIndent(2)

        self.gridLayout_7.addWidget(self.label_VelocityB, 1, 0, 1, 1)

        self.doubleSpinBox_VelocityB = QDoubleSpinBox(self.tabVelocity)
        self.doubleSpinBox_VelocityB.setObjectName(u"doubleSpinBox_VelocityB")
        self.doubleSpinBox_VelocityB.setDecimals(6)

        self.gridLayout_7.addWidget(self.doubleSpinBox_VelocityB, 1, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 2, 0, 1, 1)


        self.layout_TabVelocity.addLayout(self.gridLayout_7)

        self.plotVelocity = PlotWidget(self.tabVelocity)
        self.plotVelocity.setObjectName(u"plotVelocity")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plotVelocity.sizePolicy().hasHeightForWidth())
        self.plotVelocity.setSizePolicy(sizePolicy3)

        self.layout_TabVelocity.addWidget(self.plotVelocity)

        self.tabWidget_Game.addTab(self.tabVelocity, "")
        self.tabMargins = QWidget()
        self.tabMargins.setObjectName(u"tabMargins")
        self.tabMargins.setEnabled(True)
        self.layout_TabMargins = QHBoxLayout(self.tabMargins)
        self.layout_TabMargins.setObjectName(u"layout_TabMargins")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.tabMargins)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 0))
        self.label_8.setIndent(2)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.doubleSpinBox_MarginRight = QDoubleSpinBox(self.tabMargins)
        self.doubleSpinBox_MarginRight.setObjectName(u"doubleSpinBox_MarginRight")
        self.doubleSpinBox_MarginRight.setDecimals(6)
        self.doubleSpinBox_MarginRight.setMaximum(1.000000000000000)
        self.doubleSpinBox_MarginRight.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_MarginRight, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tabMargins)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 0))
        self.label_5.setIndent(2)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.doubleSpinBox_MarginLeft = QDoubleSpinBox(self.tabMargins)
        self.doubleSpinBox_MarginLeft.setObjectName(u"doubleSpinBox_MarginLeft")
        self.doubleSpinBox_MarginLeft.setMinimumSize(QSize(90, 0))
        self.doubleSpinBox_MarginLeft.setDecimals(6)
        self.doubleSpinBox_MarginLeft.setMaximum(1.000000000000000)
        self.doubleSpinBox_MarginLeft.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_MarginLeft, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_5)

        self.checkBox = QCheckBox(self.tabMargins)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.groupBox = QGroupBox(self.tabMargins)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.gridLayout_10 = QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(30, 0))
        self.label_32.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_32, 0, 0, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout_10.addWidget(self.doubleSpinBox_7, 1, 1, 1, 1)

        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(30, 0))
        self.label_33.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_33, 1, 0, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout_10.addWidget(self.doubleSpinBox_6, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tabMargins)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.gridLayout_11 = QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(30, 0))
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_35, 0, 0, 1, 1)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.gridLayout_11.addWidget(self.doubleSpinBox_9, 0, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(30, 0))
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_34, 1, 0, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.gridLayout_11.addWidget(self.doubleSpinBox_8, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_6 = QGroupBox(self.tabMargins)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setEnabled(False)
        self.gridLayout_26 = QGridLayout(self.groupBox_6)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_24 = QLabel(self.groupBox_6)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_26.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_26.addWidget(self.label_25, 1, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox_6)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.gridLayout_26.addWidget(self.spinBox_7, 1, 1, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox_6)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.gridLayout_26.addWidget(self.spinBox_8, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)


        self.layout_TabMargins.addLayout(self.verticalLayout_3)

        self.plotMargins = PlotWidget(self.tabMargins)
        self.plotMargins.setObjectName(u"plotMargins")
        sizePolicy3.setHeightForWidth(self.plotMargins.sizePolicy().hasHeightForWidth())
        self.plotMargins.setSizePolicy(sizePolicy3)

        self.layout_TabMargins.addWidget(self.plotMargins)

        self.tabWidget_Game.addTab(self.tabMargins, "")

        self.gridLayout.addWidget(self.tabWidget_Game, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_New)
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.action_Save_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Exit)
        self.menuHelp.addAction(self.action_Contents)
        self.menuHelp.addAction(self.action_About)
        self.menuEdit.addAction(self.action_Undo)
        self.menuEdit.addAction(self.action_Redo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_Reset)
        self.menuGame.addAction(self.action_Run)
        self.menuGame.addAction(self.action_Build)
        self.toolBar.addAction(self.action_New)
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.action_Save_as)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Undo)
        self.toolBar.addAction(self.action_Redo)
        self.toolBar.addAction(self.action_Reset)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Run)
        self.toolBar.addAction(self.action_Build)

        self.retranslateUi(MainWindow)

        self.tabWidget_Game.setCurrentIndex(2)
        self.tabWidget_Objects.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Run.setText(QCoreApplication.translate("MainWindow", u"&Run Game", None))
#if QT_CONFIG(statustip)
        self.action_Run.setStatusTip(QCoreApplication.translate("MainWindow", u"Run game", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Run.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(statustip)
        self.action_Exit.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit game editor", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_Contents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
#if QT_CONFIG(statustip)
        self.action_Contents.setStatusTip(QCoreApplication.translate("MainWindow", u"Help contents", None))
#endif // QT_CONFIG(statustip)
        self.action_Undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(statustip)
        self.action_Undo.setStatusTip(QCoreApplication.translate("MainWindow", u"Undo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Undo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_Redo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(statustip)
        self.action_Redo.setStatusTip(QCoreApplication.translate("MainWindow", u"Redo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Redo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
#if QT_CONFIG(statustip)
        self.action_New.setStatusTip(QCoreApplication.translate("MainWindow", u"Create new game definition", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_New.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
#if QT_CONFIG(statustip)
        self.action_Open.setStatusTip(QCoreApplication.translate("MainWindow", u"Open game definition", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Save.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(statustip)
        self.action_Save.setStatusTip(QCoreApplication.translate("MainWindow", u"Save game definition", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_Build.setText(QCoreApplication.translate("MainWindow", u"Build", None))
#if QT_CONFIG(statustip)
        self.action_Build.setStatusTip(QCoreApplication.translate("MainWindow", u"Build game executable", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Build.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.action_Save_as.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
#if QT_CONFIG(statustip)
        self.tabWidget_Game.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.tabGame.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabGame.setStatusTip(QCoreApplication.translate("MainWindow", u"Define game properties", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_Software.setTitle(QCoreApplication.translate("MainWindow", u"Software", None))
        self.label_Author.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.pushButton_IconSelect.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_GameName.setText(QCoreApplication.translate("MainWindow", u"Game name", None))
        self.label_GameDescription.setText(QCoreApplication.translate("MainWindow", u"Game description", None))
        self.label_GameIcon.setText("")
        self.groupBox_Game.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.label_ScrollDirection.setText(QCoreApplication.translate("MainWindow", u"Scroll direction: ", None))
        self.radioButton_VertialScrolling.setText(QCoreApplication.translate("MainWindow", u"Vertical", None))
        self.radioButton_HorizontalScrolling.setText(QCoreApplication.translate("MainWindow", u"Horizontal", None))
        self.checkBox_TrackKills.setText(QCoreApplication.translate("MainWindow", u"Touching track boundaries kills the player", None))
        self.label_ScoreTimeBonus.setText(QCoreApplication.translate("MainWindow", u"Score time bonus", None))
        self.label_AmbienceSound.setText(QCoreApplication.translate("MainWindow", u"Ambience sound", None))
        self.pushButton_AmbienceSoundSelect.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_AmbienceSoundRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_AmbienceSoundPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_AmbienceSoundVolume.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.tabWidget_Game.setTabText(self.tabWidget_Game.indexOf(self.tabGame), QCoreApplication.translate("MainWindow", u"Game", None))
        self.groupBox_Background.setTitle(QCoreApplication.translate("MainWindow", u"Screen background", None))
        self.pushButton_SelectBackgroundImage.setText(QCoreApplication.translate("MainWindow", u"Edit Image", None))
        self.checkBox_BackgroundImageScrolls.setText(QCoreApplication.translate("MainWindow", u"Background image scrolls", None))
        self.label_BackgroundImage.setText("")
        self.groupBox_Track.setTitle(QCoreApplication.translate("MainWindow", u"Track background", None))
        self.checkBox_DrawTrack.setText(QCoreApplication.translate("MainWindow", u"Draw track image", None))
        self.pushButton_SelectTrackImage.setText(QCoreApplication.translate("MainWindow", u"Edit Image", None))
        self.label_TrackImage.setText("")
        self.groupBox_Scoreboard.setTitle(QCoreApplication.translate("MainWindow", u"Scoreboard", None))
        self.label_ScoreboardImage.setText("")
        self.label_ScoreboardExample.setText(QCoreApplication.translate("MainWindow", u"Text Example", None))
        self.groupBox_ScoreboardImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.pushButton_SelectScoreboardImage.setText(QCoreApplication.translate("MainWindow", u"Edit Image", None))
        self.checkBox_ScoreboardImageKeepAspectRatio.setText(QCoreApplication.translate("MainWindow", u"Keep aspect ratio", None))
        self.label_ScoreboardImageWidth.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_ScoreboardImagePosition.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.groupBox_ScoreboardText.setTitle(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_ScoreboardTextWidth.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_ScoreboardTextPosition.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select font", None))
        self.pushButton_ChoseScoreboardBgColor.setText(QCoreApplication.translate("MainWindow", u"Background color", None))
        self.pushButton_ChoseScoreboardFgColor.setText(QCoreApplication.translate("MainWindow", u"Foreground color", None))
        self.tabWidget_Game.setTabText(self.tabWidget_Game.indexOf(self.tabAppearance), QCoreApplication.translate("MainWindow", u"Appearance", None))
#if QT_CONFIG(statustip)
        self.tabObjects.setStatusTip(QCoreApplication.translate("MainWindow", u"Define visual elements", None))
#endif // QT_CONFIG(statustip)
        self.label_PlayerImage.setText("")
        self.pushButton_SelectPlayerImage.setText(QCoreApplication.translate("MainWindow", u"Edit Image", None))
        self.label_PlayerSpeed.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_PlayerSize.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.checkBox_PlayerKeepAspectRatio.setText(QCoreApplication.translate("MainWindow", u"Keep aspect ratio", None))
        self.tabWidget_Objects.setTabText(self.tabWidget_Objects.indexOf(self.tab_Player), QCoreApplication.translate("MainWindow", u"Player", None))
        self.label_ObstacleFrequency.setText(QCoreApplication.translate("MainWindow", u"Obstacles frequency", None))
        self.pushButton_NewObstacle.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.tabWidget_Objects.setTabText(self.tabWidget_Objects.indexOf(self.tab_Obstacles), QCoreApplication.translate("MainWindow", u"Obstacles", None))
        self.label_CollectiblesFrequency.setText(QCoreApplication.translate("MainWindow", u"Collectibles frequency", None))
        self.pushButton_NewCollectible.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.tabWidget_Objects.setTabText(self.tabWidget_Objects.indexOf(self.tab_Collectibles), QCoreApplication.translate("MainWindow", u"Collectibles", None))
        self.tabWidget_Game.setTabText(self.tabWidget_Game.indexOf(self.tabObjects), QCoreApplication.translate("MainWindow", u"Objects", None))
#if QT_CONFIG(statustip)
        self.tabVelocity.setStatusTip(QCoreApplication.translate("MainWindow", u"Define scrolling velocity", None))
#endif // QT_CONFIG(statustip)
        self.label_VelocityA.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_VelocityB.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.tabWidget_Game.setTabText(self.tabWidget_Game.indexOf(self.tabVelocity), QCoreApplication.translate("MainWindow", u"Velocity", None))
#if QT_CONFIG(statustip)
        self.tabMargins.setStatusTip(QCoreApplication.translate("MainWindow", u"Define track margins", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Symmetrical", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Rigth", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Symmetrical", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Radius", None))
        self.tabWidget_Game.setTabText(self.tabWidget_Game.indexOf(self.tabMargins), QCoreApplication.translate("MainWindow", u"Margins", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

