# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastroArtistaDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

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
        self.formLayoutWidget.setGeometry(QRect(10, 40, 381, 136))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelNome = QLabel(self.formLayoutWidget)
        self.labelNome.setObjectName(u"labelNome")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelNome)

        self.lineEditNome = QLineEdit(self.formLayoutWidget)
        self.lineEditNome.setObjectName(u"lineEditNome")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditNome)

        self.labelGenero = QLabel(self.formLayoutWidget)
        self.labelGenero.setObjectName(u"labelGenero")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelGenero)

        self.comboBoxGenero = QComboBox(self.formLayoutWidget)
        self.comboBoxGenero.setObjectName(u"comboBoxGenero")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBoxGenero)

        self.labelPagina = QLabel(self.formLayoutWidget)
        self.labelPagina.setObjectName(u"labelPagina")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelPagina)

        self.lineEditPagina = QLineEdit(self.formLayoutWidget)
        self.lineEditPagina.setObjectName(u"lineEditPagina")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditPagina)

        self.labelEmail = QLabel(self.formLayoutWidget)
        self.labelEmail.setObjectName(u"labelEmail")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelEmail)

        self.lineEditEmail = QLineEdit(self.formLayoutWidget)
        self.lineEditEmail.setObjectName(u"lineEditEmail")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditEmail)

        self.labelTelefone = QLabel(self.formLayoutWidget)
        self.labelTelefone.setObjectName(u"labelTelefone")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelTelefone)

        self.lineEditTelefone = QLineEdit(self.formLayoutWidget)
        self.lineEditTelefone.setObjectName(u"lineEditTelefone")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditTelefone)

        QWidget.setTabOrder(self.lineEditNome, self.lineEditTelefone)
        QWidget.setTabOrder(self.lineEditTelefone, self.lineEditEmail)
        QWidget.setTabOrder(self.lineEditEmail, self.lineEditPagina)
        QWidget.setTabOrder(self.lineEditPagina, self.comboBoxGenero)
        QWidget.setTabOrder(self.comboBoxGenero, self.pushButtonSalvar)
        QWidget.setTabOrder(self.pushButtonSalvar, self.pushButtonCancelar)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cadastro de Artistas - Eventos", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.labelNome.setText(QCoreApplication.translate("Dialog", u"Nome:", None))
        self.labelGenero.setText(QCoreApplication.translate("Dialog", u"G\u00eanero:", None))
        self.labelPagina.setText(QCoreApplication.translate("Dialog", u"P\u00e1gina:", None))
        self.labelEmail.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.labelTelefone.setText(QCoreApplication.translate("Dialog", u"Telefone:", None))
    # retranslateUi

