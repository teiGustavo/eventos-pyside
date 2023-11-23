# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastroDespesaDialog.ui'
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
    QDoubleSpinBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

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
        self.formLayoutWidget.setGeometry(QRect(10, 40, 381, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelDescricao = QLabel(self.formLayoutWidget)
        self.labelDescricao.setObjectName(u"labelDescricao")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDescricao)

        self.labelValor = QLabel(self.formLayoutWidget)
        self.labelValor.setObjectName(u"labelValor")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelValor)

        self.lineEditDescricao = QLineEdit(self.formLayoutWidget)
        self.lineEditDescricao.setObjectName(u"lineEditDescricao")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditDescricao)

        self.doubleSpinBoxValor = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBoxValor.setObjectName(u"doubleSpinBoxValor")
        self.doubleSpinBoxValor.setMaximum(1000000000000.989990234375000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBoxValor)

        self.labelData = QLabel(self.formLayoutWidget)
        self.labelData.setObjectName(u"labelData")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelData)

        self.dateEditData = QDateEdit(self.formLayoutWidget)
        self.dateEditData.setObjectName(u"dateEditData")
        self.dateEditData.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEditData)

        self.comboBoxTipoDespesa = QComboBox(self.formLayoutWidget)
        self.comboBoxTipoDespesa.setObjectName(u"comboBoxTipoDespesa")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBoxTipoDespesa)

        self.labelTipoDespesa = QLabel(self.formLayoutWidget)
        self.labelTipoDespesa.setObjectName(u"labelTipoDespesa")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelTipoDespesa)

        self.labelEvento = QLabel(self.formLayoutWidget)
        self.labelEvento.setObjectName(u"labelEvento")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelEvento)

        self.comboBoxEvento = QComboBox(self.formLayoutWidget)
        self.comboBoxEvento.setObjectName(u"comboBoxEvento")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBoxEvento)

        QWidget.setTabOrder(self.dateEditData, self.lineEditDescricao)
        QWidget.setTabOrder(self.lineEditDescricao, self.doubleSpinBoxValor)
        QWidget.setTabOrder(self.doubleSpinBoxValor, self.comboBoxTipoDespesa)
        QWidget.setTabOrder(self.comboBoxTipoDespesa, self.comboBoxEvento)
        QWidget.setTabOrder(self.comboBoxEvento, self.pushButtonSalvar)
        QWidget.setTabOrder(self.pushButtonSalvar, self.pushButtonCancelar)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cadastro de Despesa - Eventos", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.labelDescricao.setText(QCoreApplication.translate("Dialog", u"Descri\u00e7\u00e3o:", None))
        self.labelValor.setText(QCoreApplication.translate("Dialog", u"Valor:", None))
        self.lineEditDescricao.setPlaceholderText(QCoreApplication.translate("Dialog", u"Descri\u00e7\u00e3o da Despesa", None))
        self.doubleSpinBoxValor.setPrefix(QCoreApplication.translate("Dialog", u"R$ ", None))
        self.labelData.setText(QCoreApplication.translate("Dialog", u"Data:", None))
        self.labelTipoDespesa.setText(QCoreApplication.translate("Dialog", u"Tipo de Despesa:", None))
        self.labelEvento.setText(QCoreApplication.translate("Dialog", u"Evento:", None))
    # retranslateUi

