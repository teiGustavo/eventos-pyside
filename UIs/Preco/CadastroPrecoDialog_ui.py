# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastroPrecoDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QPushButton,
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
        self.formLayoutWidget.setGeometry(QRect(10, 40, 381, 80))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCache = QLabel(self.formLayoutWidget)
        self.labelCache.setObjectName(u"labelCache")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelCache)

        self.labelArtista = QLabel(self.formLayoutWidget)
        self.labelArtista.setObjectName(u"labelArtista")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelArtista)

        self.comboBoxArtista = QComboBox(self.formLayoutWidget)
        self.comboBoxArtista.setObjectName(u"comboBoxArtista")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxArtista)

        self.labelEvento = QLabel(self.formLayoutWidget)
        self.labelEvento.setObjectName(u"labelEvento")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelEvento)

        self.comboBoxEvento = QComboBox(self.formLayoutWidget)
        self.comboBoxEvento.setObjectName(u"comboBoxEvento")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxEvento)

        self.doubleSpinBoxCache = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBoxCache.setObjectName(u"doubleSpinBoxCache")
        self.doubleSpinBoxCache.setMaximum(1000000000000.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBoxCache)

        QWidget.setTabOrder(self.doubleSpinBoxCache, self.comboBoxArtista)
        QWidget.setTabOrder(self.comboBoxArtista, self.comboBoxEvento)
        QWidget.setTabOrder(self.comboBoxEvento, self.pushButtonSalvar)
        QWidget.setTabOrder(self.pushButtonSalvar, self.pushButtonCancelar)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cadastro de Preco - Eventos", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.labelCache.setText(QCoreApplication.translate("Dialog", u"Cach\u00ea:", None))
        self.labelArtista.setText(QCoreApplication.translate("Dialog", u"Artista:", None))
        self.labelEvento.setText(QCoreApplication.translate("Dialog", u"Evento:", None))
    # retranslateUi

