# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_object_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_ObjectWidget(object):
    def setupUi(self, ObjectWidget):
        if not ObjectWidget.objectName():
            ObjectWidget.setObjectName(u"ObjectWidget")
        ObjectWidget.resize(936, 210)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ObjectWidget.sizePolicy().hasHeightForWidth())
        ObjectWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(ObjectWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frameObject = QFrame(ObjectWidget)
        self.frameObject.setObjectName(u"frameObject")
        sizePolicy.setHeightForWidth(self.frameObject.sizePolicy().hasHeightForWidth())
        self.frameObject.setSizePolicy(sizePolicy)
        self.frameObject.setFrameShape(QFrame.Panel)
        self.frameObject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frameObject)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_Image = QLabel(self.frameObject)
        self.label_Image.setObjectName(u"label_Image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_Image.sizePolicy().hasHeightForWidth())
        self.label_Image.setSizePolicy(sizePolicy1)
        self.label_Image.setMinimumSize(QSize(128, 128))
        self.label_Image.setMaximumSize(QSize(128, 128))
#if QT_CONFIG(accessibility)
        self.label_Image.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_Image.setAutoFillBackground(True)
        self.label_Image.setFrameShape(QFrame.Panel)
        self.label_Image.setFrameShadow(QFrame.Sunken)
        self.label_Image.setScaledContents(False)
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setMargin(2)
        self.label_Image.setIndent(0)

        self.horizontalLayout_13.addWidget(self.label_Image)

        self.verticalLayout_Buttons = QVBoxLayout()
        self.verticalLayout_Buttons.setObjectName(u"verticalLayout_Buttons")
        self.horizontalLayout_SelectImage = QHBoxLayout()
        self.horizontalLayout_SelectImage.setObjectName(u"horizontalLayout_SelectImage")
        self.pushButton_SelectImage = QPushButton(self.frameObject)
        self.pushButton_SelectImage.setObjectName(u"pushButton_SelectImage")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectImage.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectImage.setSizePolicy(sizePolicy1)
        self.pushButton_SelectImage.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_SelectImage.addWidget(self.pushButton_SelectImage)

        self.label_Size = QLabel(self.frameObject)
        self.label_Size.setObjectName(u"label_Size")
        sizePolicy.setHeightForWidth(self.label_Size.sizePolicy().hasHeightForWidth())
        self.label_Size.setSizePolicy(sizePolicy)
        self.label_Size.setMinimumSize(QSize(60, 0))
        self.label_Size.setIndent(5)

        self.horizontalLayout_SelectImage.addWidget(self.label_Size)

        self.spinBox_Width = QSpinBox(self.frameObject)
        self.spinBox_Width.setObjectName(u"spinBox_Width")
        self.spinBox_Width.setMinimumSize(QSize(60, 0))
        self.spinBox_Width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_Width.setMinimum(1)
        self.spinBox_Width.setMaximum(1920)
        self.spinBox_Width.setValue(100)

        self.horizontalLayout_SelectImage.addWidget(self.spinBox_Width)

        self.spinBox_Height = QSpinBox(self.frameObject)
        self.spinBox_Height.setObjectName(u"spinBox_Height")
        self.spinBox_Height.setEnabled(False)
        self.spinBox_Height.setMinimumSize(QSize(60, 0))
        self.spinBox_Height.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_Height.setMinimum(1)
        self.spinBox_Height.setMaximum(1920)

        self.horizontalLayout_SelectImage.addWidget(self.spinBox_Height)

        self.checkBox_KeepAspectRatio = QCheckBox(self.frameObject)
        self.checkBox_KeepAspectRatio.setObjectName(u"checkBox_KeepAspectRatio")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_KeepAspectRatio.sizePolicy().hasHeightForWidth())
        self.checkBox_KeepAspectRatio.setSizePolicy(sizePolicy2)
        self.checkBox_KeepAspectRatio.setChecked(True)

        self.horizontalLayout_SelectImage.addWidget(self.checkBox_KeepAspectRatio)

        self.horizontalSpacer_SelectImage = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_SelectImage.addItem(self.horizontalSpacer_SelectImage)


        self.verticalLayout_Buttons.addLayout(self.horizontalLayout_SelectImage)

        self.horizontalLayout_Points = QHBoxLayout()
        self.horizontalLayout_Points.setObjectName(u"horizontalLayout_Points")
        self.label_Points = QLabel(self.frameObject)
        self.label_Points.setObjectName(u"label_Points")
        sizePolicy.setHeightForWidth(self.label_Points.sizePolicy().hasHeightForWidth())
        self.label_Points.setSizePolicy(sizePolicy)
        self.label_Points.setMinimumSize(QSize(60, 0))
        self.label_Points.setIndent(5)

        self.horizontalLayout_Points.addWidget(self.label_Points)

        self.doubleSpinBox_Points = QDoubleSpinBox(self.frameObject)
        self.doubleSpinBox_Points.setObjectName(u"doubleSpinBox_Points")
        self.doubleSpinBox_Points.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_Points.setDecimals(4)
        self.doubleSpinBox_Points.setMinimum(-1000000.000000000000000)
        self.doubleSpinBox_Points.setMaximum(1000000.000000000000000)

        self.horizontalLayout_Points.addWidget(self.doubleSpinBox_Points)

        self.horizontalSpacer_Points = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_Points.addItem(self.horizontalSpacer_Points)


        self.verticalLayout_Buttons.addLayout(self.horizontalLayout_Points)

        self.horizontalLayout_Sound = QHBoxLayout()
        self.horizontalLayout_Sound.setObjectName(u"horizontalLayout_Sound")
        self.label_Sound = QLabel(self.frameObject)
        self.label_Sound.setObjectName(u"label_Sound")
        sizePolicy.setHeightForWidth(self.label_Sound.sizePolicy().hasHeightForWidth())
        self.label_Sound.setSizePolicy(sizePolicy)
        self.label_Sound.setMinimumSize(QSize(120, 0))
        self.label_Sound.setIndent(5)

        self.horizontalLayout_Sound.addWidget(self.label_Sound)

        self.pushButton_SoundSelect = QPushButton(self.frameObject)
        self.pushButton_SoundSelect.setObjectName(u"pushButton_SoundSelect")
        sizePolicy1.setHeightForWidth(self.pushButton_SoundSelect.sizePolicy().hasHeightForWidth())
        self.pushButton_SoundSelect.setSizePolicy(sizePolicy1)

        self.horizontalLayout_Sound.addWidget(self.pushButton_SoundSelect)

        self.pushButton_SoundRemove = QPushButton(self.frameObject)
        self.pushButton_SoundRemove.setObjectName(u"pushButton_SoundRemove")
        self.pushButton_SoundRemove.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pushButton_SoundRemove.sizePolicy().hasHeightForWidth())
        self.pushButton_SoundRemove.setSizePolicy(sizePolicy1)

        self.horizontalLayout_Sound.addWidget(self.pushButton_SoundRemove)

        self.pushButton_SoundPlay = QPushButton(self.frameObject)
        self.pushButton_SoundPlay.setObjectName(u"pushButton_SoundPlay")
        self.pushButton_SoundPlay.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pushButton_SoundPlay.sizePolicy().hasHeightForWidth())
        self.pushButton_SoundPlay.setSizePolicy(sizePolicy1)

        self.horizontalLayout_Sound.addWidget(self.pushButton_SoundPlay)

        self.label_Volume = QLabel(self.frameObject)
        self.label_Volume.setObjectName(u"label_Volume")
        self.label_Volume.setIndent(2)

        self.horizontalLayout_Sound.addWidget(self.label_Volume)

        self.doubleSpinBox_Volume = QDoubleSpinBox(self.frameObject)
        self.doubleSpinBox_Volume.setObjectName(u"doubleSpinBox_Volume")
        self.doubleSpinBox_Volume.setEnabled(False)
        self.doubleSpinBox_Volume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_Volume.setMaximum(1.000000000000000)
        self.doubleSpinBox_Volume.setSingleStep(0.100000000000000)
        self.doubleSpinBox_Volume.setValue(1.000000000000000)

        self.horizontalLayout_Sound.addWidget(self.doubleSpinBox_Volume)

        self.horizontalSpacer_Sound = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_Sound.addItem(self.horizontalSpacer_Sound)


        self.verticalLayout_Buttons.addLayout(self.horizontalLayout_Sound)

        self.horizontalLayout_Size = QHBoxLayout()
        self.horizontalLayout_Size.setObjectName(u"horizontalLayout_Size")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_Size.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frameObject)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_Size.addWidget(self.pushButton)

        self.pushButton_Delete = QPushButton(self.frameObject)
        self.pushButton_Delete.setObjectName(u"pushButton_Delete")
        sizePolicy1.setHeightForWidth(self.pushButton_Delete.sizePolicy().hasHeightForWidth())
        self.pushButton_Delete.setSizePolicy(sizePolicy1)
        self.pushButton_Delete.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_Size.addWidget(self.pushButton_Delete)


        self.verticalLayout_Buttons.addLayout(self.horizontalLayout_Size)


        self.horizontalLayout_13.addLayout(self.verticalLayout_Buttons)


        self.gridLayout.addWidget(self.frameObject, 0, 0, 1, 1)


        self.retranslateUi(ObjectWidget)

        QMetaObject.connectSlotsByName(ObjectWidget)
    # setupUi

    def retranslateUi(self, ObjectWidget):
        ObjectWidget.setWindowTitle(QCoreApplication.translate("ObjectWidget", u"Form", None))
        self.label_Image.setText("")
        self.pushButton_SelectImage.setText(QCoreApplication.translate("ObjectWidget", u"Edit Image", None))
        self.label_Size.setText(QCoreApplication.translate("ObjectWidget", u"Size", None))
        self.checkBox_KeepAspectRatio.setText(QCoreApplication.translate("ObjectWidget", u"Keep aspect ratio", None))
        self.label_Points.setText(QCoreApplication.translate("ObjectWidget", u"Points", None))
        self.label_Sound.setText(QCoreApplication.translate("ObjectWidget", u"Contact sound", None))
        self.pushButton_SoundSelect.setText(QCoreApplication.translate("ObjectWidget", u"Select", None))
        self.pushButton_SoundRemove.setText(QCoreApplication.translate("ObjectWidget", u"Remove", None))
        self.pushButton_SoundPlay.setText(QCoreApplication.translate("ObjectWidget", u"Play", None))
        self.label_Volume.setText(QCoreApplication.translate("ObjectWidget", u"Volume", None))
        self.pushButton.setText(QCoreApplication.translate("ObjectWidget", u"Duplicate Object", None))
        self.pushButton_Delete.setText(QCoreApplication.translate("ObjectWidget", u"Delete Object", None))
    # retranslateUi

