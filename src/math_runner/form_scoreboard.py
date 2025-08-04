# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_scoreboard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFontComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(637, 435)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fontComboBox = QFontComboBox(self.groupBox_3)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.fontComboBox, 2, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_2.addWidget(self.radioButton_3, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 2, 1, 1)

        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 2, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_2, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setIndent(5)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(50, 0))
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.spinBox)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setIndent(7)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.spinBox_2 = QSpinBox(self.groupBox_3)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(50, 0))
        self.spinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.spinBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_4)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_5)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAutoFillBackground(True)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 25))

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(250, 25))

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(80, 25))
        self.label_4.setMargin(2)
        self.label_4.setIndent(0)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(80, 25))
        self.label_5.setMargin(2)
        self.label_5.setIndent(0)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(80, 25))
        self.label.setMargin(2)
        self.label.setIndent(0)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6.setMargin(2)
        self.label_6.setIndent(0)

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7.setMargin(2)
        self.label_7.setIndent(0)

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8.setMargin(2)
        self.label_8.setIndent(0)

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Di\u00e1logo", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Fonte", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Carregar do arquivo", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Selecionar", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Fonte do sistema", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Fonte de recurso", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Tamanho da fonte", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Espa\u00e7amento entre linhas", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cor da fonte", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cor de fundo", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Conte\u00fados", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Nome do jogo", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Texto", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"Texto", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Pontos", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Velocidade", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Tempo decorrido", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Pr\u00e9 visualiza\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"MathRunner", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Texto", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Pontos:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Tempo:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Velocidade: ", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"0 123 456 789", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"0 123 456 789", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"0 123 456 789", None))
    # retranslateUi

