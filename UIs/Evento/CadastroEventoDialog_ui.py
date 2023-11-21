# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastroEventoDialog.ui'
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
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

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
        self.formLayoutWidget.setGeometry(QRect(10, 40, 381, 108))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelData = QLabel(self.formLayoutWidget)
        self.labelData.setObjectName(u"labelData")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelData)

        self.labelLocalizacao = QLabel(self.formLayoutWidget)
        self.labelLocalizacao.setObjectName(u"labelLocalizacao")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelLocalizacao)

        self.lineEditLocalizacao = QLineEdit(self.formLayoutWidget)
        self.lineEditLocalizacao.setObjectName(u"lineEditLocalizacao")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditLocalizacao)

        self.labelTipoEvento = QLabel(self.formLayoutWidget)
        self.labelTipoEvento.setObjectName(u"labelTipoEvento")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelTipoEvento)

        self.labelCidade = QLabel(self.formLayoutWidget)
        self.labelCidade.setObjectName(u"labelCidade")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelCidade)

        self.comboBoxTipoEvento = QComboBox(self.formLayoutWidget)
        self.comboBoxTipoEvento.setObjectName(u"comboBoxTipoEvento")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxTipoEvento)

        self.comboBoxCidade = QComboBox(self.formLayoutWidget)
        self.comboBoxCidade.setObjectName(u"comboBoxCidade")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBoxCidade)

        self.dateEditData = QDateEdit(self.formLayoutWidget)
        self.dateEditData.setObjectName(u"dateEditData")
        self.dateEditData.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEditData)

        QWidget.setTabOrder(self.dateEditData, self.lineEditLocalizacao)
        QWidget.setTabOrder(self.lineEditLocalizacao, self.comboBoxTipoEvento)
        QWidget.setTabOrder(self.comboBoxTipoEvento, self.comboBoxCidade)
        QWidget.setTabOrder(self.comboBoxCidade, self.pushButtonSalvar)
        QWidget.setTabOrder(self.pushButtonSalvar, self.pushButtonCancelar)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cadastro de Evento - Eventos", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.labelData.setText(QCoreApplication.translate("Dialog", u"Data:", None))
        self.labelLocalizacao.setText(QCoreApplication.translate("Dialog", u"Localiza\u00e7\u00e3o:", None))
        self.labelTipoEvento.setText(QCoreApplication.translate("Dialog", u"Tipo de Evento:", None))
        self.labelCidade.setText(QCoreApplication.translate("Dialog", u"Cidade:", None))
    # retranslateUi

