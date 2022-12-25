# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_object_creation_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 202)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frameCollectable_2 = QFrame(Form)
        self.frameCollectable_2.setObjectName(u"frameCollectable_2")
        self.frameCollectable_2.setFrameShape(QFrame.Panel)
        self.frameCollectable_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frameCollectable_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_ObstacleImage = QLabel(self.frameCollectable_2)
        self.label_ObstacleImage.setObjectName(u"label_ObstacleImage")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ObstacleImage.sizePolicy().hasHeightForWidth())
        self.label_ObstacleImage.setSizePolicy(sizePolicy)
        self.label_ObstacleImage.setMinimumSize(QSize(128, 128))
        self.label_ObstacleImage.setAutoFillBackground(True)
        self.label_ObstacleImage.setFrameShape(QFrame.Panel)
        self.label_ObstacleImage.setFrameShadow(QFrame.Sunken)
        self.label_ObstacleImage.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_ObstacleImage)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_DeleteObstacle = QPushButton(self.frameCollectable_2)
        self.pushButton_DeleteObstacle.setObjectName(u"pushButton_DeleteObstacle")
        sizePolicy.setHeightForWidth(self.pushButton_DeleteObstacle.sizePolicy().hasHeightForWidth())
        self.pushButton_DeleteObstacle.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.pushButton_DeleteObstacle)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_13.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_SelectCollectableImage = QLabel(self.frameCollectable_2)
        self.label_SelectCollectableImage.setObjectName(u"label_SelectCollectableImage")
        self.label_SelectCollectableImage.setSizeIncrement(QSize(0, 0))
        self.label_SelectCollectableImage.setIndent(5)

        self.horizontalLayout_21.addWidget(self.label_SelectCollectableImage)

        self.pushButton_SelectCollectableImage = QPushButton(self.frameCollectable_2)
        self.pushButton_SelectCollectableImage.setObjectName(u"pushButton_SelectCollectableImage")
        sizePolicy.setHeightForWidth(self.pushButton_SelectCollectableImage.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectCollectableImage.setSizePolicy(sizePolicy)

        self.horizontalLayout_21.addWidget(self.pushButton_SelectCollectableImage)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.checkBox_ObstacleKeepAspectRatio = QCheckBox(self.frameCollectable_2)
        self.checkBox_ObstacleKeepAspectRatio.setObjectName(u"checkBox_ObstacleKeepAspectRatio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_ObstacleKeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_ObstacleKeepAspectRatio.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.checkBox_ObstacleKeepAspectRatio, 0, 4, 1, 1)

        self.label_ObstacleWidth = QLabel(self.frameCollectable_2)
        self.label_ObstacleWidth.setObjectName(u"label_ObstacleWidth")
        self.label_ObstacleWidth.setMinimumSize(QSize(50, 0))
        self.label_ObstacleWidth.setIndent(5)

        self.gridLayout_8.addWidget(self.label_ObstacleWidth, 0, 0, 1, 1)

        self.spinBox_ObstacleHeight = QSpinBox(self.frameCollectable_2)
        self.spinBox_ObstacleHeight.setObjectName(u"spinBox_ObstacleHeight")
        self.spinBox_ObstacleHeight.setMinimumSize(QSize(60, 0))

        self.gridLayout_8.addWidget(self.spinBox_ObstacleHeight, 0, 3, 1, 1)

        self.spinBox_ObstacleWidth = QSpinBox(self.frameCollectable_2)
        self.spinBox_ObstacleWidth.setObjectName(u"spinBox_ObstacleWidth")
        self.spinBox_ObstacleWidth.setMinimumSize(QSize(60, 0))

        self.gridLayout_8.addWidget(self.spinBox_ObstacleWidth, 0, 1, 1, 1)

        self.label_ObstacleHeight = QLabel(self.frameCollectable_2)
        self.label_ObstacleHeight.setObjectName(u"label_ObstacleHeight")
        self.label_ObstacleHeight.setIndent(5)

        self.gridLayout_8.addWidget(self.label_ObstacleHeight, 0, 2, 1, 1)

        self.spinBox_ObstaclePoints = QSpinBox(self.frameCollectable_2)
        self.spinBox_ObstaclePoints.setObjectName(u"spinBox_ObstaclePoints")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox_ObstaclePoints.sizePolicy().hasHeightForWidth())
        self.spinBox_ObstaclePoints.setSizePolicy(sizePolicy2)
        self.spinBox_ObstaclePoints.setMinimumSize(QSize(60, 0))
        self.spinBox_ObstaclePoints.setBaseSize(QSize(37, 0))

        self.gridLayout_8.addWidget(self.spinBox_ObstaclePoints, 1, 1, 1, 1)

        self.label_ObstaclePoints = QLabel(self.frameCollectable_2)
        self.label_ObstaclePoints.setObjectName(u"label_ObstaclePoints")
        self.label_ObstaclePoints.setIndent(5)

        self.gridLayout_8.addWidget(self.label_ObstaclePoints, 1, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_8)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_ObstacleSound = QLabel(self.frameCollectable_2)
        self.label_ObstacleSound.setObjectName(u"label_ObstacleSound")
        self.label_ObstacleSound.setIndent(5)

        self.horizontalLayout_18.addWidget(self.label_ObstacleSound)

        self.pushButton_ObstacleSoundSelect = QPushButton(self.frameCollectable_2)
        self.pushButton_ObstacleSoundSelect.setObjectName(u"pushButton_ObstacleSoundSelect")

        self.horizontalLayout_18.addWidget(self.pushButton_ObstacleSoundSelect)

        self.pushButton_ObstacleSoundRemove = QPushButton(self.frameCollectable_2)
        self.pushButton_ObstacleSoundRemove.setObjectName(u"pushButton_ObstacleSoundRemove")

        self.horizontalLayout_18.addWidget(self.pushButton_ObstacleSoundRemove)

        self.pushButton_ObstacleSoundPlay = QPushButton(self.frameCollectable_2)
        self.pushButton_ObstacleSoundPlay.setObjectName(u"pushButton_ObstacleSoundPlay")

        self.horizontalLayout_18.addWidget(self.pushButton_ObstacleSoundPlay)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_24)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.frameCollectable_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_ObstacleImage.setText("")
        self.pushButton_DeleteObstacle.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label_SelectCollectableImage.setText(QCoreApplication.translate("Form", u"Image", None))
        self.pushButton_SelectCollectableImage.setText(QCoreApplication.translate("Form", u"Select", None))
        self.checkBox_ObstacleKeepAspectRatio.setText(QCoreApplication.translate("Form", u"Keep aspect ratio", None))
        self.label_ObstacleWidth.setText(QCoreApplication.translate("Form", u"Width", None))
        self.label_ObstacleHeight.setText(QCoreApplication.translate("Form", u"Height", None))
        self.label_ObstaclePoints.setText(QCoreApplication.translate("Form", u"Points", None))
        self.label_ObstacleSound.setText(QCoreApplication.translate("Form", u"Sound", None))
        self.pushButton_ObstacleSoundSelect.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_ObstacleSoundRemove.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.pushButton_ObstacleSoundPlay.setText(QCoreApplication.translate("Form", u"Play", None))
    # retranslateUi

