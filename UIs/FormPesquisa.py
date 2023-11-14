# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormPesquisa.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_FormPesquisa(object):
    def setupUi(self, FormPesquisa):
        if not FormPesquisa.objectName():
            FormPesquisa.setObjectName(u"FormPesquisa")
        FormPesquisa.setWindowModality(Qt.NonModal)
        FormPesquisa.resize(618, 372)
        self.gridLayout = QGridLayout(FormPesquisa)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LblPesquisar = QLabel(FormPesquisa)
        self.LblPesquisar.setObjectName(u"LblPesquisar")

        self.horizontalLayout.addWidget(self.LblPesquisar)

        self.EditValorPesquisa = QLineEdit(FormPesquisa)
        self.EditValorPesquisa.setObjectName(u"EditValorPesquisa")

        self.horizontalLayout.addWidget(self.EditValorPesquisa)

        self.BtnPesquisar = QPushButton(FormPesquisa)
        self.BtnPesquisar.setObjectName(u"BtnPesquisar")

        self.horizontalLayout.addWidget(self.BtnPesquisar)

        self.BtnIncluir = QPushButton(FormPesquisa)
        self.BtnIncluir.setObjectName(u"BtnIncluir")

        self.horizontalLayout.addWidget(self.BtnIncluir)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(FormPesquisa)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableResultado = QTableWidget(self.tab)
        self.tableResultado.setObjectName(u"tableResultado")

        self.gridLayout_2.addWidget(self.tableResultado, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.retranslateUi(FormPesquisa)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormPesquisa)
    # setupUi

    def retranslateUi(self, FormPesquisa):
        FormPesquisa.setWindowTitle(QCoreApplication.translate("FormPesquisa", u"Form", None))
        self.LblPesquisar.setText(QCoreApplication.translate("FormPesquisa", u"Pesquisar", None))
        self.EditValorPesquisa.setText("")
        self.BtnPesquisar.setText(QCoreApplication.translate("FormPesquisa", u"Pesquisar...", None))
        self.BtnIncluir.setText(QCoreApplication.translate("FormPesquisa", u"Incluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("FormPesquisa", u"Dados", None))
    # retranslateUi

