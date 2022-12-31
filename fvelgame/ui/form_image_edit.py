# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_image_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon(QIcon.fromTheme(u"document-new"))
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon(QIcon.fromTheme(u"document-open"))
        self.actionOpen.setIcon(icon1)
        self.actionSelect = QAction(MainWindow)
        self.actionSelect.setObjectName(u"actionSelect")
        icon2 = QIcon(QIcon.fromTheme(u"document-save"))
        self.actionSelect.setIcon(icon2)
        self.actionCancel = QAction(MainWindow)
        self.actionCancel.setObjectName(u"actionCancel")
        self.actionNew_shape = QAction(MainWindow)
        self.actionNew_shape.setObjectName(u"actionNew_shape")
        self.actionFill_color = QAction(MainWindow)
        self.actionFill_color.setObjectName(u"actionFill_color")
        self.actionFlip_left_right = QAction(MainWindow)
        self.actionFlip_left_right.setObjectName(u"actionFlip_left_right")
        self.actionFlip_up_down = QAction(MainWindow)
        self.actionFlip_up_down.setObjectName(u"actionFlip_up_down")
        self.actionRotate_90 = QAction(MainWindow)
        self.actionRotate_90.setObjectName(u"actionRotate_90")
        self.actionCrop = QAction(MainWindow)
        self.actionCrop.setObjectName(u"actionCrop")
        self.actionSet_transparence = QAction(MainWindow)
        self.actionSet_transparence.setObjectName(u"actionSet_transparence")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNew_shape)
        self.menuFile.addAction(self.actionSelect)
        self.menuFile.addAction(self.actionCancel)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFill_color)
        self.menuEdit.addAction(self.actionFlip_left_right)
        self.menuEdit.addAction(self.actionFlip_up_down)
        self.menuEdit.addAction(self.actionRotate_90)
        self.menuEdit.addAction(self.actionCrop)
        self.menuEdit.addAction(self.actionSet_transparence)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New from image", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSelect.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.actionCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.actionNew_shape.setText(QCoreApplication.translate("MainWindow", u"New shape", None))
        self.actionFill_color.setText(QCoreApplication.translate("MainWindow", u"Fill color", None))
        self.actionFlip_left_right.setText(QCoreApplication.translate("MainWindow", u"Flip left right", None))
        self.actionFlip_up_down.setText(QCoreApplication.translate("MainWindow", u"Flip up down", None))
        self.actionRotate_90.setText(QCoreApplication.translate("MainWindow", u"Rotate 90", None))
        self.actionCrop.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.actionSet_transparence.setText(QCoreApplication.translate("MainWindow", u"Set transparency", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Image Display", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

