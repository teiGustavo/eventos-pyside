# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastroApresentacaoDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFormLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 325)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 161, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonSalvar = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonSalvar.setObjectName(u"pushButtonSalvar")

        self.horizontalLayout.addWidget(self.pushButtonSalvar)

        self.pushButtonCancelar = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonCancelar.setObjectName(u"pushButtonCancelar")

        self.horizontalLayout.addWidget(self.pushButtonCancelar)

        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 40, 381, 164))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelData = QLabel(self.formLayoutWidget)
        self.labelData.setObjectName(u"labelData")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelData)

        self.dateEditData = QDateEdit(self.formLayoutWidget)
        self.dateEditData.setObjectName(u"dateEditData")
        self.dateEditData.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEditData)

        self.labelValorIngresso = QLabel(self.formLayoutWidget)
        self.labelValorIngresso.setObjectName(u"labelValorIngresso")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelValorIngresso)

        self.spinBoxValorIngresso = QSpinBox(self.formLayoutWidget)
        self.spinBoxValorIngresso.setObjectName(u"spinBoxValorIngresso")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBoxValorIngresso)

        self.labelPublicoPresente = QLabel(self.formLayoutWidget)
        self.labelPublicoPresente.setObjectName(u"labelPublicoPresente")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelPublicoPresente)

        self.spinBoxPublicoPresente = QSpinBox(self.formLayoutWidget)
        self.spinBoxPublicoPresente.setObjectName(u"spinBoxPublicoPresente")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBoxPublicoPresente)

        self.labelPublicoMaximo = QLabel(self.formLayoutWidget)
        self.labelPublicoMaximo.setObjectName(u"labelPublicoMaximo")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelPublicoMaximo)

        self.spinBoxPublicoMaximo = QSpinBox(self.formLayoutWidget)
        self.spinBoxPublicoMaximo.setObjectName(u"spinBoxPublicoMaximo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBoxPublicoMaximo)

        self.labelArtista = QLabel(self.formLayoutWidget)
        self.labelArtista.setObjectName(u"labelArtista")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelArtista)

        self.comboBoxArtista = QComboBox(self.formLayoutWidget)
        self.comboBoxArtista.setObjectName(u"comboBoxArtista")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBoxArtista)

        self.labelEvento = QLabel(self.formLayoutWidget)
        self.labelEvento.setObjectName(u"labelEvento")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelEvento)

        self.comboBoxEvento = QComboBox(self.formLayoutWidget)
        self.comboBoxEvento.setObjectName(u"comboBoxEvento")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.comboBoxEvento)

        QWidget.setTabOrder(self.dateEditData, self.spinBoxValorIngresso)
        QWidget.setTabOrder(self.spinBoxValorIngresso, self.spinBoxPublicoMaximo)
        QWidget.setTabOrder(self.spinBoxPublicoMaximo, self.spinBoxPublicoPresente)
        QWidget.setTabOrder(self.spinBoxPublicoPresente, self.comboBoxArtista)
        QWidget.setTabOrder(self.comboBoxArtista, self.comboBoxEvento)
        QWidget.setTabOrder(self.comboBoxEvento, self.pushButtonSalvar)
        QWidget.setTabOrder(self.pushButtonSalvar, self.pushButtonCancelar)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cadastro de Apresentacao - Eventos", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.labelData.setText(QCoreApplication.translate("Dialog", u"Data:", None))
        self.labelValorIngresso.setText(QCoreApplication.translate("Dialog", u"Valor do Ingresso:", None))
        self.labelPublicoPresente.setText(QCoreApplication.translate("Dialog", u"P\u00fablico Presente:", None))
        self.labelPublicoMaximo.setText(QCoreApplication.translate("Dialog", u"P\u00fablico M\u00e1ximo:", None))
        self.labelArtista.setText(QCoreApplication.translate("Dialog", u"Artista:", None))
        self.labelEvento.setText(QCoreApplication.translate("Dialog", u"Evento:", None))
    # retranslateUi

