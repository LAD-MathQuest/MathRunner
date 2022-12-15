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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(636, 899)
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
        icon2 = QIcon()
        iconThemeName = u"help-about"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_About.setIcon(icon2)
        self.action_Contents = QAction(MainWindow)
        self.action_Contents.setObjectName(u"action_Contents")
        icon3 = QIcon()
        iconThemeName = u"help-contents"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Contents.setIcon(icon3)
        self.action_Undo = QAction(MainWindow)
        self.action_Undo.setObjectName(u"action_Undo")
        icon4 = QIcon()
        iconThemeName = u"edit-undo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Undo.setIcon(icon4)
        self.action_Redo = QAction(MainWindow)
        self.action_Redo.setObjectName(u"action_Redo")
        icon5 = QIcon()
        iconThemeName = u"edit-redo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Redo.setIcon(icon5)
        self.action_Reset = QAction(MainWindow)
        self.action_Reset.setObjectName(u"action_Reset")
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
        icon9 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon9 = QIcon.fromTheme(iconThemeName)
        else:
            icon9.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Save.setIcon(icon9)
        self.action_Build = QAction(MainWindow)
        self.action_Build.setObjectName(u"action_Build")
        icon10 = QIcon()
        iconThemeName = u"application-x-executable"
        if QIcon.hasThemeIcon(iconThemeName):
            icon10 = QIcon.fromTheme(iconThemeName)
        else:
            icon10.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Build.setIcon(icon10)
        self.action_Save_as = QAction(MainWindow)
        self.action_Save_as.setObjectName(u"action_Save_as")
        icon11 = QIcon()
        iconThemeName = u"document-save-as"
        if QIcon.hasThemeIcon(iconThemeName):
            icon11 = QIcon.fromTheme(iconThemeName)
        else:
            icon11.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Save_as.setIcon(icon11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(True)
        self.tabGame = QWidget()
        self.tabGame.setObjectName(u"tabGame")
        self.gridLayout_2 = QGridLayout(self.tabGame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.lineEdit_Author = QLineEdit(self.tabGame)
        self.lineEdit_Author.setObjectName(u"lineEdit_Author")

        self.gridLayout_2.addWidget(self.lineEdit_Author, 3, 1, 1, 1)

        self.plainTextEdit_GameDescription = QPlainTextEdit(self.tabGame)
        self.plainTextEdit_GameDescription.setObjectName(u"plainTextEdit_GameDescription")

        self.gridLayout_2.addWidget(self.plainTextEdit_GameDescription, 2, 1, 1, 1)

        self.label_Author = QLabel(self.tabGame)
        self.label_Author.setObjectName(u"label_Author")

        self.gridLayout_2.addWidget(self.label_Author, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_GameIcon = QLabel(self.tabGame)
        self.label_GameIcon.setObjectName(u"label_GameIcon")
        self.label_GameIcon.setMinimumSize(QSize(64, 64))
        self.label_GameIcon.setBaseSize(QSize(64, 64))
        self.label_GameIcon.setAutoFillBackground(True)
        self.label_GameIcon.setFrameShape(QFrame.Panel)
        self.label_GameIcon.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.label_GameIcon)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_12)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.label_GameName = QLabel(self.tabGame)
        self.label_GameName.setObjectName(u"label_GameName")

        self.gridLayout_2.addWidget(self.label_GameName, 0, 0, 1, 1)

        self.label_GameDescription = QLabel(self.tabGame)
        self.label_GameDescription.setObjectName(u"label_GameDescription")

        self.gridLayout_2.addWidget(self.label_GameDescription, 2, 0, 1, 1)

        self.lineEdit_GameName = QLineEdit(self.tabGame)
        self.lineEdit_GameName.setObjectName(u"lineEdit_GameName")

        self.gridLayout_2.addWidget(self.lineEdit_GameName, 0, 1, 1, 1)

        self.pushButton_IconSelect = QPushButton(self.tabGame)
        self.pushButton_IconSelect.setObjectName(u"pushButton_IconSelect")

        self.gridLayout_2.addWidget(self.pushButton_IconSelect, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tabGame, "")
        self.tabDynamics = QWidget()
        self.tabDynamics.setObjectName(u"tabDynamics")
        self.gridLayout_3 = QGridLayout(self.tabDynamics)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 268, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 11, 0, 1, 1)

        self.groupBox_PlayerMovement = QGroupBox(self.tabDynamics)
        self.groupBox_PlayerMovement.setObjectName(u"groupBox_PlayerMovement")
        self.gridLayout_20 = QGridLayout(self.groupBox_PlayerMovement)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_PlayerSpeed = QLabel(self.groupBox_PlayerMovement)
        self.label_PlayerSpeed.setObjectName(u"label_PlayerSpeed")

        self.gridLayout_20.addWidget(self.label_PlayerSpeed, 1, 0, 1, 1)

        self.label_ScrollDirection = QLabel(self.groupBox_PlayerMovement)
        self.label_ScrollDirection.setObjectName(u"label_ScrollDirection")

        self.gridLayout_20.addWidget(self.label_ScrollDirection, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_ScrollVertical = QRadioButton(self.groupBox_PlayerMovement)
        self.radioButton_ScrollVertical.setObjectName(u"radioButton_ScrollVertical")

        self.verticalLayout.addWidget(self.radioButton_ScrollVertical)

        self.radioButton_ScrollHorizntal = QRadioButton(self.groupBox_PlayerMovement)
        self.radioButton_ScrollHorizntal.setObjectName(u"radioButton_ScrollHorizntal")

        self.verticalLayout.addWidget(self.radioButton_ScrollHorizntal)


        self.gridLayout_20.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBox_PlayerSpeed = QSpinBox(self.groupBox_PlayerMovement)
        self.spinBox_PlayerSpeed.setObjectName(u"spinBox_PlayerSpeed")

        self.horizontalLayout_3.addWidget(self.spinBox_PlayerSpeed)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_20.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_PlayerMovement, 0, 0, 1, 1)

        self.groupBox_Frequencies = QGroupBox(self.tabDynamics)
        self.groupBox_Frequencies.setObjectName(u"groupBox_Frequencies")
        self.gridLayout_21 = QGridLayout(self.groupBox_Frequencies)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.doubleSpinBox_ObstacleFrequency = QDoubleSpinBox(self.groupBox_Frequencies)
        self.doubleSpinBox_ObstacleFrequency.setObjectName(u"doubleSpinBox_ObstacleFrequency")

        self.gridLayout_21.addWidget(self.doubleSpinBox_ObstacleFrequency, 0, 1, 1, 1)

        self.doubleSpinBox_TreasureFrequency = QDoubleSpinBox(self.groupBox_Frequencies)
        self.doubleSpinBox_TreasureFrequency.setObjectName(u"doubleSpinBox_TreasureFrequency")

        self.gridLayout_21.addWidget(self.doubleSpinBox_TreasureFrequency, 1, 1, 1, 1)

        self.label_TreasureFrequency = QLabel(self.groupBox_Frequencies)
        self.label_TreasureFrequency.setObjectName(u"label_TreasureFrequency")

        self.gridLayout_21.addWidget(self.label_TreasureFrequency, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.label_ObstacleFrequency = QLabel(self.groupBox_Frequencies)
        self.label_ObstacleFrequency.setObjectName(u"label_ObstacleFrequency")

        self.gridLayout_21.addWidget(self.label_ObstacleFrequency, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_Frequencies, 2, 0, 1, 1)

        self.groupBox_ScoreComputing = QGroupBox(self.tabDynamics)
        self.groupBox_ScoreComputing.setObjectName(u"groupBox_ScoreComputing")
        self.gridLayout_22 = QGridLayout(self.groupBox_ScoreComputing)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_ScoreObstacle = QLabel(self.groupBox_ScoreComputing)
        self.label_ScoreObstacle.setObjectName(u"label_ScoreObstacle")

        self.gridLayout_22.addWidget(self.label_ScoreObstacle, 1, 0, 1, 1)

        self.label_ScoreTreasure = QLabel(self.groupBox_ScoreComputing)
        self.label_ScoreTreasure.setObjectName(u"label_ScoreTreasure")

        self.gridLayout_22.addWidget(self.label_ScoreTreasure, 2, 0, 1, 1)

        self.doubleSpinBox_ScoreObstacle = QDoubleSpinBox(self.groupBox_ScoreComputing)
        self.doubleSpinBox_ScoreObstacle.setObjectName(u"doubleSpinBox_ScoreObstacle")

        self.gridLayout_22.addWidget(self.doubleSpinBox_ScoreObstacle, 1, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_13, 2, 2, 1, 1)

        self.label_ScoreTimeBonus = QLabel(self.groupBox_ScoreComputing)
        self.label_ScoreTimeBonus.setObjectName(u"label_ScoreTimeBonus")

        self.gridLayout_22.addWidget(self.label_ScoreTimeBonus, 0, 0, 1, 1)

        self.doubleSpinBox_ScoreTreasure = QDoubleSpinBox(self.groupBox_ScoreComputing)
        self.doubleSpinBox_ScoreTreasure.setObjectName(u"doubleSpinBox_ScoreTreasure")

        self.gridLayout_22.addWidget(self.doubleSpinBox_ScoreTreasure, 2, 1, 1, 1)

        self.doubleSpinBox_ScoreTimeBonus = QDoubleSpinBox(self.groupBox_ScoreComputing)
        self.doubleSpinBox_ScoreTimeBonus.setObjectName(u"doubleSpinBox_ScoreTimeBonus")

        self.gridLayout_22.addWidget(self.doubleSpinBox_ScoreTimeBonus, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_ScoreComputing, 7, 0, 1, 1)

        self.tabWidget.addTab(self.tabDynamics, "")
        self.tabAppearence = QWidget()
        self.tabAppearence.setObjectName(u"tabAppearence")
        self.gridLayout_4 = QGridLayout(self.tabAppearence)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = QScrollArea(self.tabAppearence)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -267, 580, 1013))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_Scoreboard = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Scoreboard.setObjectName(u"groupBox_Scoreboard")
        self.gridLayout_18 = QGridLayout(self.groupBox_Scoreboard)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_ScoreboardImage = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardImage.setObjectName(u"label_ScoreboardImage")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ScoreboardImage.sizePolicy().hasHeightForWidth())
        self.label_ScoreboardImage.setSizePolicy(sizePolicy)
        self.label_ScoreboardImage.setMinimumSize(QSize(64, 64))
        self.label_ScoreboardImage.setFrameShape(QFrame.Panel)
        self.label_ScoreboardImage.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.label_ScoreboardImage)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_18)


        self.gridLayout_18.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.spinBox_ScoreboardPositionX = QSpinBox(self.groupBox_Scoreboard)
        self.spinBox_ScoreboardPositionX.setObjectName(u"spinBox_ScoreboardPositionX")
        self.spinBox_ScoreboardPositionX.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_23.addWidget(self.spinBox_ScoreboardPositionX)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_18)

        self.spinBox_ScoreboardPositionY = QSpinBox(self.groupBox_Scoreboard)
        self.spinBox_ScoreboardPositionY.setObjectName(u"spinBox_ScoreboardPositionY")
        self.spinBox_ScoreboardPositionY.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_23.addWidget(self.spinBox_ScoreboardPositionY)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_16)


        self.gridLayout_25.addLayout(self.horizontalLayout_23, 3, 1, 1, 1)

        self.label_ScoreboardBgColor_2 = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardBgColor_2.setObjectName(u"label_ScoreboardBgColor_2")
        self.label_ScoreboardBgColor_2.setIndent(5)

        self.gridLayout_25.addWidget(self.label_ScoreboardBgColor_2, 6, 0, 1, 1)

        self.label_ChoseScoreboardFgColor = QLabel(self.groupBox_Scoreboard)
        self.label_ChoseScoreboardFgColor.setObjectName(u"label_ChoseScoreboardFgColor")
        self.label_ChoseScoreboardFgColor.setIndent(5)

        self.gridLayout_25.addWidget(self.label_ChoseScoreboardFgColor, 7, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.spinBox_ScoreboardHeight = QSpinBox(self.groupBox_Scoreboard)
        self.spinBox_ScoreboardHeight.setObjectName(u"spinBox_ScoreboardHeight")
        self.spinBox_ScoreboardHeight.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_8.addWidget(self.spinBox_ScoreboardHeight)

        self.checkBox_ScoreboardKeepAspectRatio = QCheckBox(self.groupBox_Scoreboard)
        self.checkBox_ScoreboardKeepAspectRatio.setObjectName(u"checkBox_ScoreboardKeepAspectRatio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_ScoreboardKeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_ScoreboardKeepAspectRatio.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.checkBox_ScoreboardKeepAspectRatio)


        self.gridLayout_25.addLayout(self.horizontalLayout_8, 5, 1, 1, 1)

        self.label_ScoreboardWidth = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardWidth.setObjectName(u"label_ScoreboardWidth")
        self.label_ScoreboardWidth.setIndent(5)

        self.gridLayout_25.addWidget(self.label_ScoreboardWidth, 4, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_ScoreboardBgColor = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardBgColor.setObjectName(u"label_ScoreboardBgColor")
        sizePolicy.setHeightForWidth(self.label_ScoreboardBgColor.sizePolicy().hasHeightForWidth())
        self.label_ScoreboardBgColor.setSizePolicy(sizePolicy)
        self.label_ScoreboardBgColor.setMinimumSize(QSize(26, 26))
        self.label_ScoreboardBgColor.setBaseSize(QSize(26, 26))
        self.label_ScoreboardBgColor.setAutoFillBackground(True)
        self.label_ScoreboardBgColor.setFrameShape(QFrame.Panel)
        self.label_ScoreboardBgColor.setFrameShadow(QFrame.Sunken)
        self.label_ScoreboardBgColor.setMargin(0)

        self.horizontalLayout_22.addWidget(self.label_ScoreboardBgColor)

        self.pushButton_ChoseScoreboardBgColor = QPushButton(self.groupBox_Scoreboard)
        self.pushButton_ChoseScoreboardBgColor.setObjectName(u"pushButton_ChoseScoreboardBgColor")
        sizePolicy.setHeightForWidth(self.pushButton_ChoseScoreboardBgColor.sizePolicy().hasHeightForWidth())
        self.pushButton_ChoseScoreboardBgColor.setSizePolicy(sizePolicy)

        self.horizontalLayout_22.addWidget(self.pushButton_ChoseScoreboardBgColor)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_15)


        self.gridLayout_25.addLayout(self.horizontalLayout_22, 6, 1, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_ScoreboardFgColor = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardFgColor.setObjectName(u"label_ScoreboardFgColor")
        sizePolicy.setHeightForWidth(self.label_ScoreboardFgColor.sizePolicy().hasHeightForWidth())
        self.label_ScoreboardFgColor.setSizePolicy(sizePolicy)
        self.label_ScoreboardFgColor.setMinimumSize(QSize(26, 26))
        self.label_ScoreboardFgColor.setBaseSize(QSize(26, 26))
        self.label_ScoreboardFgColor.setAutoFillBackground(True)
        self.label_ScoreboardFgColor.setFrameShape(QFrame.Panel)
        self.label_ScoreboardFgColor.setFrameShadow(QFrame.Sunken)
        self.label_ScoreboardFgColor.setMargin(0)

        self.horizontalLayout_24.addWidget(self.label_ScoreboardFgColor)

        self.pushButton_ChoseScoreboardFgColor = QPushButton(self.groupBox_Scoreboard)
        self.pushButton_ChoseScoreboardFgColor.setObjectName(u"pushButton_ChoseScoreboardFgColor")
        sizePolicy.setHeightForWidth(self.pushButton_ChoseScoreboardFgColor.sizePolicy().hasHeightForWidth())
        self.pushButton_ChoseScoreboardFgColor.setSizePolicy(sizePolicy)

        self.horizontalLayout_24.addWidget(self.pushButton_ChoseScoreboardFgColor)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)


        self.gridLayout_25.addLayout(self.horizontalLayout_24, 7, 1, 1, 1)

        self.label_ScoreboardHeight = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardHeight.setObjectName(u"label_ScoreboardHeight")
        self.label_ScoreboardHeight.setIndent(5)

        self.gridLayout_25.addWidget(self.label_ScoreboardHeight, 5, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spinBox_ScoreboardWidth = QSpinBox(self.groupBox_Scoreboard)
        self.spinBox_ScoreboardWidth.setObjectName(u"spinBox_ScoreboardWidth")
        self.spinBox_ScoreboardWidth.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_7.addWidget(self.spinBox_ScoreboardWidth)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_22)


        self.gridLayout_25.addLayout(self.horizontalLayout_7, 4, 1, 1, 1)

        self.label_ScoreboardPosition = QLabel(self.groupBox_Scoreboard)
        self.label_ScoreboardPosition.setObjectName(u"label_ScoreboardPosition")
        self.label_ScoreboardPosition.setIndent(5)

        self.gridLayout_25.addWidget(self.label_ScoreboardPosition, 3, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_SelectScoreboard = QPushButton(self.groupBox_Scoreboard)
        self.pushButton_SelectScoreboard.setObjectName(u"pushButton_SelectScoreboard")
        sizePolicy.setHeightForWidth(self.pushButton_SelectScoreboard.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectScoreboard.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.pushButton_SelectScoreboard)

        self.horizontalSpacer_25 = QSpacerItem(1, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_25)


        self.gridLayout_25.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_25, 0, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_3, 5, 2, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_Scoreboard, 7, 0, 1, 1)

        self.groupBox_Treasure = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Treasure.setObjectName(u"groupBox_Treasure")
        self.gridLayout_17 = QGridLayout(self.groupBox_Treasure)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_TreasureImage = QLabel(self.groupBox_Treasure)
        self.label_TreasureImage.setObjectName(u"label_TreasureImage")
        sizePolicy.setHeightForWidth(self.label_TreasureImage.sizePolicy().hasHeightForWidth())
        self.label_TreasureImage.setSizePolicy(sizePolicy)
        self.label_TreasureImage.setMinimumSize(QSize(64, 64))
        self.label_TreasureImage.setAutoFillBackground(True)
        self.label_TreasureImage.setFrameShape(QFrame.Panel)
        self.label_TreasureImage.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.label_TreasureImage)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_12)


        self.gridLayout_17.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_SelectTreasure = QPushButton(self.groupBox_Treasure)
        self.pushButton_SelectTreasure.setObjectName(u"pushButton_SelectTreasure")
        sizePolicy.setHeightForWidth(self.pushButton_SelectTreasure.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectTreasure.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.pushButton_SelectTreasure)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.spinBox_TreasureWidth = QSpinBox(self.groupBox_Treasure)
        self.spinBox_TreasureWidth.setObjectName(u"spinBox_TreasureWidth")
        self.spinBox_TreasureWidth.setMinimumSize(QSize(60, 0))

        self.gridLayout_23.addWidget(self.spinBox_TreasureWidth, 1, 1, 1, 1)

        self.label_TreasureWidth = QLabel(self.groupBox_Treasure)
        self.label_TreasureWidth.setObjectName(u"label_TreasureWidth")
        self.label_TreasureWidth.setMinimumSize(QSize(50, 0))
        self.label_TreasureWidth.setIndent(5)

        self.gridLayout_23.addWidget(self.label_TreasureWidth, 1, 0, 1, 1)

        self.label_TreasureHeight = QLabel(self.groupBox_Treasure)
        self.label_TreasureHeight.setObjectName(u"label_TreasureHeight")
        self.label_TreasureHeight.setIndent(5)

        self.gridLayout_23.addWidget(self.label_TreasureHeight, 2, 0, 1, 1)

        self.spinBox_TreasureHeight = QSpinBox(self.groupBox_Treasure)
        self.spinBox_TreasureHeight.setObjectName(u"spinBox_TreasureHeight")

        self.gridLayout_23.addWidget(self.spinBox_TreasureHeight, 2, 1, 1, 1)

        self.checkBox_TreasureKeepAspectRatio = QCheckBox(self.groupBox_Treasure)
        self.checkBox_TreasureKeepAspectRatio.setObjectName(u"checkBox_TreasureKeepAspectRatio")
        sizePolicy1.setHeightForWidth(self.checkBox_TreasureKeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_TreasureKeepAspectRatio.setSizePolicy(sizePolicy1)

        self.gridLayout_23.addWidget(self.checkBox_TreasureKeepAspectRatio, 2, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_23)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_15)


        self.gridLayout_17.addLayout(self.verticalLayout_7, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_Treasure, 2, 0, 1, 1)

        self.groupBox_Track = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Track.setObjectName(u"groupBox_Track")
        self.gridLayout_16 = QGridLayout(self.groupBox_Track)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_TrackImage = QLabel(self.groupBox_Track)
        self.label_TrackImage.setObjectName(u"label_TrackImage")
        sizePolicy.setHeightForWidth(self.label_TrackImage.sizePolicy().hasHeightForWidth())
        self.label_TrackImage.setSizePolicy(sizePolicy)
        self.label_TrackImage.setMinimumSize(QSize(64, 64))
        self.label_TrackImage.setAutoFillBackground(True)
        self.label_TrackImage.setFrameShape(QFrame.Panel)
        self.label_TrackImage.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.label_TrackImage)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_16)


        self.gridLayout_16.addLayout(self.verticalLayout_11, 1, 0, 1, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.pushButton_SelectTrack = QPushButton(self.groupBox_Track)
        self.pushButton_SelectTrack.setObjectName(u"pushButton_SelectTrack")
        sizePolicy.setHeightForWidth(self.pushButton_SelectTrack.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectTrack.setSizePolicy(sizePolicy)

        self.gridLayout_27.addWidget(self.pushButton_SelectTrack, 0, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_19, 1, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_27, 1, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_Track, 4, 0, 1, 1)

        self.groupBox_Player = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Player.setObjectName(u"groupBox_Player")
        self.gridLayout_13 = QGridLayout(self.groupBox_Player)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_SelectPlayer = QPushButton(self.groupBox_Player)
        self.pushButton_SelectPlayer.setObjectName(u"pushButton_SelectPlayer")

        self.horizontalLayout_15.addWidget(self.pushButton_SelectPlayer)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.spinBox_PlayerWidth = QSpinBox(self.groupBox_Player)
        self.spinBox_PlayerWidth.setObjectName(u"spinBox_PlayerWidth")
        self.spinBox_PlayerWidth.setMinimumSize(QSize(60, 0))

        self.gridLayout_12.addWidget(self.spinBox_PlayerWidth, 0, 1, 1, 1)

        self.label_PlayerWidth = QLabel(self.groupBox_Player)
        self.label_PlayerWidth.setObjectName(u"label_PlayerWidth")
        self.label_PlayerWidth.setMinimumSize(QSize(50, 0))
        self.label_PlayerWidth.setIndent(5)

        self.gridLayout_12.addWidget(self.label_PlayerWidth, 0, 0, 1, 1)

        self.spinBox_PlayerHeight = QSpinBox(self.groupBox_Player)
        self.spinBox_PlayerHeight.setObjectName(u"spinBox_PlayerHeight")

        self.gridLayout_12.addWidget(self.spinBox_PlayerHeight, 1, 1, 1, 1)

        self.label_PlayerHeight = QLabel(self.groupBox_Player)
        self.label_PlayerHeight.setObjectName(u"label_PlayerHeight")
        self.label_PlayerHeight.setIndent(5)

        self.gridLayout_12.addWidget(self.label_PlayerHeight, 1, 0, 1, 1)

        self.checkBox_PlayerKeepAspectRatio = QCheckBox(self.groupBox_Player)
        self.checkBox_PlayerKeepAspectRatio.setObjectName(u"checkBox_PlayerKeepAspectRatio")
        sizePolicy1.setHeightForWidth(self.checkBox_PlayerKeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_PlayerKeepAspectRatio.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.checkBox_PlayerKeepAspectRatio, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.gridLayout_13.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_PlayerImage = QLabel(self.groupBox_Player)
        self.label_PlayerImage.setObjectName(u"label_PlayerImage")
        sizePolicy.setHeightForWidth(self.label_PlayerImage.sizePolicy().hasHeightForWidth())
        self.label_PlayerImage.setSizePolicy(sizePolicy)
        self.label_PlayerImage.setMinimumSize(QSize(64, 64))
        self.label_PlayerImage.setAutoFillBackground(True)
        self.label_PlayerImage.setFrameShape(QFrame.Panel)
        self.label_PlayerImage.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.label_PlayerImage)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)


        self.gridLayout_13.addLayout(self.verticalLayout_8, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_Player, 0, 0, 1, 1)

        self.groupBox_Obstacle = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Obstacle.setObjectName(u"groupBox_Obstacle")
        self.gridLayout_8 = QGridLayout(self.groupBox_Obstacle)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_SelectObstacle = QPushButton(self.groupBox_Obstacle)
        self.pushButton_SelectObstacle.setObjectName(u"pushButton_SelectObstacle")
        sizePolicy.setHeightForWidth(self.pushButton_SelectObstacle.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectObstacle.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.pushButton_SelectObstacle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_ObstacleWidth = QLabel(self.groupBox_Obstacle)
        self.label_ObstacleWidth.setObjectName(u"label_ObstacleWidth")
        self.label_ObstacleWidth.setMinimumSize(QSize(50, 0))
        self.label_ObstacleWidth.setIndent(5)

        self.gridLayout_14.addWidget(self.label_ObstacleWidth, 0, 0, 1, 1)

        self.spinBox_ObstacleWidth = QSpinBox(self.groupBox_Obstacle)
        self.spinBox_ObstacleWidth.setObjectName(u"spinBox_ObstacleWidth")
        self.spinBox_ObstacleWidth.setMinimumSize(QSize(60, 0))

        self.gridLayout_14.addWidget(self.spinBox_ObstacleWidth, 0, 1, 1, 1)

        self.spinBox_ObstacleHeight = QSpinBox(self.groupBox_Obstacle)
        self.spinBox_ObstacleHeight.setObjectName(u"spinBox_ObstacleHeight")

        self.gridLayout_14.addWidget(self.spinBox_ObstacleHeight, 1, 1, 1, 1)

        self.label_ObstacleHeight = QLabel(self.groupBox_Obstacle)
        self.label_ObstacleHeight.setObjectName(u"label_ObstacleHeight")
        self.label_ObstacleHeight.setIndent(5)

        self.gridLayout_14.addWidget(self.label_ObstacleHeight, 1, 0, 1, 1)

        self.checkBox_ObstacleKeepAspectRatio = QCheckBox(self.groupBox_Obstacle)
        self.checkBox_ObstacleKeepAspectRatio.setObjectName(u"checkBox_ObstacleKeepAspectRatio")
        sizePolicy1.setHeightForWidth(self.checkBox_ObstacleKeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_ObstacleKeepAspectRatio.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.checkBox_ObstacleKeepAspectRatio, 1, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_14)

        self.verticalSpacer_14 = QSpacerItem(20, 85, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_14)


        self.gridLayout_8.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_ObstacleImage = QLabel(self.groupBox_Obstacle)
        self.label_ObstacleImage.setObjectName(u"label_ObstacleImage")
        sizePolicy.setHeightForWidth(self.label_ObstacleImage.sizePolicy().hasHeightForWidth())
        self.label_ObstacleImage.setSizePolicy(sizePolicy)
        self.label_ObstacleImage.setMinimumSize(QSize(64, 64))
        self.label_ObstacleImage.setAutoFillBackground(True)
        self.label_ObstacleImage.setFrameShape(QFrame.Panel)
        self.label_ObstacleImage.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.label_ObstacleImage)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_11)


        self.gridLayout_8.addLayout(self.verticalLayout_6, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_Obstacle, 1, 0, 1, 1)

        self.groupBox_Background = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Background.setObjectName(u"groupBox_Background")
        self.gridLayout_15 = QGridLayout(self.groupBox_Background)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_BackgroundImage = QLabel(self.groupBox_Background)
        self.label_BackgroundImage.setObjectName(u"label_BackgroundImage")
        sizePolicy.setHeightForWidth(self.label_BackgroundImage.sizePolicy().hasHeightForWidth())
        self.label_BackgroundImage.setSizePolicy(sizePolicy)
        self.label_BackgroundImage.setMinimumSize(QSize(64, 64))
        self.label_BackgroundImage.setAutoFillBackground(True)
        self.label_BackgroundImage.setFrameShape(QFrame.Panel)
        self.label_BackgroundImage.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.label_BackgroundImage)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_13)


        self.gridLayout_15.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_17, 3, 0, 1, 1)

        self.radioButton_BackgroundFixed = QRadioButton(self.groupBox_Background)
        self.radioButton_BackgroundFixed.setObjectName(u"radioButton_BackgroundFixed")

        self.gridLayout_24.addWidget(self.radioButton_BackgroundFixed, 1, 0, 1, 1)

        self.radioButton_BackgroundScrolls = QRadioButton(self.groupBox_Background)
        self.radioButton_BackgroundScrolls.setObjectName(u"radioButton_BackgroundScrolls")

        self.gridLayout_24.addWidget(self.radioButton_BackgroundScrolls, 2, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_SelectBackground = QPushButton(self.groupBox_Background)
        self.pushButton_SelectBackground.setObjectName(u"pushButton_SelectBackground")
        sizePolicy.setHeightForWidth(self.pushButton_SelectBackground.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectBackground.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.pushButton_SelectBackground)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)


        self.gridLayout_24.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_24, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_Background, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tabAppearence, "")
        self.tabSounds = QWidget()
        self.tabSounds.setObjectName(u"tabSounds")
        self.gridLayout_5 = QGridLayout(self.tabSounds)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_SoundCatch = QLabel(self.tabSounds)
        self.label_SoundCatch.setObjectName(u"label_SoundCatch")

        self.gridLayout_5.addWidget(self.label_SoundCatch, 2, 0, 1, 1)

        self.label_SoundCrash = QLabel(self.tabSounds)
        self.label_SoundCrash.setObjectName(u"label_SoundCrash")

        self.gridLayout_5.addWidget(self.label_SoundCrash, 1, 0, 1, 1)

        self.pushButton_PlayCatch = QPushButton(self.tabSounds)
        self.pushButton_PlayCatch.setObjectName(u"pushButton_PlayCatch")

        self.gridLayout_5.addWidget(self.pushButton_PlayCatch, 2, 2, 1, 1)

        self.label_SoundAmbience = QLabel(self.tabSounds)
        self.label_SoundAmbience.setObjectName(u"label_SoundAmbience")

        self.gridLayout_5.addWidget(self.label_SoundAmbience, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 311, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.pushButton_PlayAmbience = QPushButton(self.tabSounds)
        self.pushButton_PlayAmbience.setObjectName(u"pushButton_PlayAmbience")

        self.gridLayout_5.addWidget(self.pushButton_PlayAmbience, 0, 2, 1, 1)

        self.pushButton_SelectAmbience = QPushButton(self.tabSounds)
        self.pushButton_SelectAmbience.setObjectName(u"pushButton_SelectAmbience")

        self.gridLayout_5.addWidget(self.pushButton_SelectAmbience, 0, 1, 1, 1)

        self.pushButton_SelectCatch = QPushButton(self.tabSounds)
        self.pushButton_SelectCatch.setObjectName(u"pushButton_SelectCatch")

        self.gridLayout_5.addWidget(self.pushButton_SelectCatch, 2, 1, 1, 1)

        self.pushButton_SelectCrash = QPushButton(self.tabSounds)
        self.pushButton_SelectCrash.setObjectName(u"pushButton_SelectCrash")

        self.gridLayout_5.addWidget(self.pushButton_SelectCrash, 1, 1, 1, 1)

        self.pushButton_PlayCrash = QPushButton(self.tabSounds)
        self.pushButton_PlayCrash.setObjectName(u"pushButton_PlayCrash")

        self.gridLayout_5.addWidget(self.pushButton_PlayCrash, 1, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_20, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tabSounds, "")
        self.tabVelocity = QWidget()
        self.tabVelocity.setObjectName(u"tabVelocity")
        self.gridLayout_6 = QGridLayout(self.tabVelocity)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_VelocityPlot = QLabel(self.tabVelocity)
        self.label_VelocityPlot.setObjectName(u"label_VelocityPlot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_VelocityPlot.sizePolicy().hasHeightForWidth())
        self.label_VelocityPlot.setSizePolicy(sizePolicy2)
        self.label_VelocityPlot.setMinimumSize(QSize(0, 264))
        self.label_VelocityPlot.setAutoFillBackground(True)
        self.label_VelocityPlot.setFrameShape(QFrame.Panel)
        self.label_VelocityPlot.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.label_VelocityPlot, 0, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_VelocityA = QLabel(self.tabVelocity)
        self.label_VelocityA.setObjectName(u"label_VelocityA")
        self.label_VelocityA.setMinimumSize(QSize(30, 0))
        self.label_VelocityA.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_VelocityA, 0, 0, 1, 1)

        self.label_VelocityB = QLabel(self.tabVelocity)
        self.label_VelocityB.setObjectName(u"label_VelocityB")
        self.label_VelocityB.setMinimumSize(QSize(30, 0))
        self.label_VelocityB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_VelocityB, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 2, 0, 1, 1)

        self.doubleSpinBox_VelocityA = QDoubleSpinBox(self.tabVelocity)
        self.doubleSpinBox_VelocityA.setObjectName(u"doubleSpinBox_VelocityA")

        self.gridLayout_7.addWidget(self.doubleSpinBox_VelocityA, 0, 1, 1, 1)

        self.doubleSpinBox_VelocityB = QDoubleSpinBox(self.tabVelocity)
        self.doubleSpinBox_VelocityB.setObjectName(u"doubleSpinBox_VelocityB")

        self.gridLayout_7.addWidget(self.doubleSpinBox_VelocityB, 1, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabVelocity, "")
        self.tabMargins = QWidget()
        self.tabMargins.setObjectName(u"tabMargins")
        self.tabMargins.setEnabled(False)
        self.gridLayout_9 = QGridLayout(self.tabMargins)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_MarginsPlot = QLabel(self.tabMargins)
        self.label_MarginsPlot.setObjectName(u"label_MarginsPlot")
        sizePolicy2.setHeightForWidth(self.label_MarginsPlot.sizePolicy().hasHeightForWidth())
        self.label_MarginsPlot.setSizePolicy(sizePolicy2)
        self.label_MarginsPlot.setMinimumSize(QSize(0, 264))
        self.label_MarginsPlot.setAutoFillBackground(True)
        self.label_MarginsPlot.setFrameShape(QFrame.Panel)
        self.label_MarginsPlot.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.label_MarginsPlot, 0, 3, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.tabMargins)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.groupBox = QGroupBox(self.tabMargins)
        self.groupBox.setObjectName(u"groupBox")
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


        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabMargins, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 636, 23))
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

        self.tabWidget.setCurrentIndex(0)


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
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.tabGame.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabGame.setStatusTip(QCoreApplication.translate("MainWindow", u"Define game properties", None))
#endif // QT_CONFIG(statustip)
        self.label_Author.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.label_GameIcon.setText("")
        self.label_GameName.setText(QCoreApplication.translate("MainWindow", u"Game name", None))
        self.label_GameDescription.setText(QCoreApplication.translate("MainWindow", u"Game description", None))
        self.pushButton_IconSelect.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGame), QCoreApplication.translate("MainWindow", u"Game", None))
#if QT_CONFIG(statustip)
        self.tabDynamics.setStatusTip(QCoreApplication.translate("MainWindow", u"Define game dynamics", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_PlayerMovement.setTitle(QCoreApplication.translate("MainWindow", u"Player movement", None))
        self.label_PlayerSpeed.setText(QCoreApplication.translate("MainWindow", u"Player speed", None))
        self.label_ScrollDirection.setText(QCoreApplication.translate("MainWindow", u"Scroll direction", None))
        self.radioButton_ScrollVertical.setText(QCoreApplication.translate("MainWindow", u"Vertical", None))
        self.radioButton_ScrollHorizntal.setText(QCoreApplication.translate("MainWindow", u"Horizontal", None))
        self.groupBox_Frequencies.setTitle(QCoreApplication.translate("MainWindow", u"Frequencies", None))
        self.label_TreasureFrequency.setText(QCoreApplication.translate("MainWindow", u"Treasure frequency", None))
        self.label_ObstacleFrequency.setText(QCoreApplication.translate("MainWindow", u"Obstacle frequency", None))
        self.groupBox_ScoreComputing.setTitle(QCoreApplication.translate("MainWindow", u"Score computing", None))
        self.label_ScoreObstacle.setText(QCoreApplication.translate("MainWindow", u"Score dodge obstacle", None))
        self.label_ScoreTreasure.setText(QCoreApplication.translate("MainWindow", u"Score catch treasure", None))
        self.label_ScoreTimeBonus.setText(QCoreApplication.translate("MainWindow", u"Score time bonus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDynamics), QCoreApplication.translate("MainWindow", u"Dynamics", None))
#if QT_CONFIG(statustip)
        self.tabAppearence.setStatusTip(QCoreApplication.translate("MainWindow", u"Define visual elements", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_Scoreboard.setTitle(QCoreApplication.translate("MainWindow", u"Scoreboard", None))
        self.label_ScoreboardImage.setText("")
        self.label_ScoreboardBgColor_2.setText(QCoreApplication.translate("MainWindow", u"Background color", None))
        self.label_ChoseScoreboardFgColor.setText(QCoreApplication.translate("MainWindow", u"Foreground color", None))
        self.checkBox_ScoreboardKeepAspectRatio.setText(QCoreApplication.translate("MainWindow", u"Keep aspect ratio", None))
        self.label_ScoreboardWidth.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_ScoreboardBgColor.setText("")
        self.pushButton_ChoseScoreboardBgColor.setText(QCoreApplication.translate("MainWindow", u"Choose color", None))
        self.label_ScoreboardFgColor.setText("")
        self.pushButton_ChoseScoreboardFgColor.setText(QCoreApplication.translate("MainWindow", u"Choose color", None))
        self.label_ScoreboardHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_ScoreboardPosition.setText(QCoreApplication.translate("MainWindow", u"Position (x,y)", None))
        self.pushButton_SelectScoreboard.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.groupBox_Treasure.setTitle(QCoreApplication.translate("MainWindow", u"Treasure", None))
        self.label_TreasureImage.setText("")
        self.pushButton_SelectTreasure.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_TreasureWidth.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_TreasureHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.checkBox_TreasureKeepAspectRatio.setText(QCoreApplication.translate("MainWindow", u"Keep aspect ratio", None))
        self.groupBox_Track.setTitle(QCoreApplication.translate("MainWindow", u"Track background", None))
        self.label_TrackImage.setText("")
        self.pushButton_SelectTrack.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.groupBox_Player.setTitle(QCoreApplication.translate("MainWindow", u"Player", None))
        self.pushButton_SelectPlayer.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_PlayerWidth.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_PlayerHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.checkBox_PlayerKeepAspectRatio.setText(QCoreApplication.translate("MainWindow", u"Keep aspect ratio", None))
        self.label_PlayerImage.setText("")
        self.groupBox_Obstacle.setTitle(QCoreApplication.translate("MainWindow", u"Obstacle", None))
        self.pushButton_SelectObstacle.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_ObstacleWidth.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_ObstacleHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.checkBox_ObstacleKeepAspectRatio.setText(QCoreApplication.translate("MainWindow", u"Keep aspect ratio", None))
        self.label_ObstacleImage.setText("")
        self.groupBox_Background.setTitle(QCoreApplication.translate("MainWindow", u"Game background", None))
        self.label_BackgroundImage.setText("")
        self.radioButton_BackgroundFixed.setText(QCoreApplication.translate("MainWindow", u"Background is fixed", None))
        self.radioButton_BackgroundScrolls.setText(QCoreApplication.translate("MainWindow", u"Background scrolls", None))
        self.pushButton_SelectBackground.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAppearence), QCoreApplication.translate("MainWindow", u"Appearance", None))
#if QT_CONFIG(tooltip)
        self.tabSounds.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabSounds.setStatusTip(QCoreApplication.translate("MainWindow", u"Define game sounds", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.tabSounds.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_SoundCatch.setText(QCoreApplication.translate("MainWindow", u"Catch the treasure", None))
        self.label_SoundCrash.setText(QCoreApplication.translate("MainWindow", u"Crash with obstacle", None))
        self.pushButton_PlayCatch.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_SoundAmbience.setText(QCoreApplication.translate("MainWindow", u"Ambience", None))
        self.pushButton_PlayAmbience.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pushButton_SelectAmbience.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_SelectCatch.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_SelectCrash.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_PlayCrash.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSounds), QCoreApplication.translate("MainWindow", u"Sounds", None))
#if QT_CONFIG(statustip)
        self.tabVelocity.setStatusTip(QCoreApplication.translate("MainWindow", u"Define scrolling velocity", None))
#endif // QT_CONFIG(statustip)
        self.label_VelocityPlot.setText("")
        self.label_VelocityA.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_VelocityB.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVelocity), QCoreApplication.translate("MainWindow", u"Velocity", None))
#if QT_CONFIG(statustip)
        self.tabMargins.setStatusTip(QCoreApplication.translate("MainWindow", u"Define track margins", None))
#endif // QT_CONFIG(statustip)
        self.label_MarginsPlot.setText("")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMargins), QCoreApplication.translate("MainWindow", u"Margins", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

