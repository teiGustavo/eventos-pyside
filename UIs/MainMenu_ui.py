# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionEstado = QAction(MainWindow)
        self.actionEstado.setObjectName(u"actionEstado")
        self.actionPesquisaEstado = QAction(MainWindow)
        self.actionPesquisaEstado.setObjectName(u"actionPesquisaEstado")
        self.actionCidade = QAction(MainWindow)
        self.actionCidade.setObjectName(u"actionCidade")
        self.actionGenero = QAction(MainWindow)
        self.actionGenero.setObjectName(u"actionGenero")
        self.actionArtista = QAction(MainWindow)
        self.actionArtista.setObjectName(u"actionArtista")
        self.actionTipoEvento = QAction(MainWindow)
        self.actionTipoEvento.setObjectName(u"actionTipoEvento")
        self.actionEvento = QAction(MainWindow)
        self.actionEvento.setObjectName(u"actionEvento")
        self.actionTipoDespesa = QAction(MainWindow)
        self.actionTipoDespesa.setObjectName(u"actionTipoDespesa")
        self.actionDespesa = QAction(MainWindow)
        self.actionDespesa.setObjectName(u"actionDespesa")
        self.actionReceita = QAction(MainWindow)
        self.actionReceita.setObjectName(u"actionReceita")
        self.actionPreco = QAction(MainWindow)
        self.actionPreco.setObjectName(u"actionPreco")
        self.actionApresentacao = QAction(MainWindow)
        self.actionApresentacao.setObjectName(u"actionApresentacao")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menuCadastro.addAction(self.actionEstado)
        self.menuCadastro.addAction(self.actionCidade)
        self.menuCadastro.addAction(self.actionGenero)
        self.menuCadastro.addAction(self.actionArtista)
        self.menuCadastro.addAction(self.actionTipoEvento)
        self.menuCadastro.addAction(self.actionEvento)
        self.menuCadastro.addAction(self.actionPreco)
        self.menuCadastro.addAction(self.actionApresentacao)
        self.menuCadastro.addAction(self.actionReceita)
        self.menuCadastro.addAction(self.actionTipoDespesa)
        self.menuCadastro.addAction(self.actionDespesa)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Janela Principal - Eventos", None))
        self.actionEstado.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.actionPesquisaEstado.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.actionCidade.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.actionGenero.setText(QCoreApplication.translate("MainWindow", u"G\u00eanero", None))
        self.actionArtista.setText(QCoreApplication.translate("MainWindow", u"Artista", None))
        self.actionTipoEvento.setText(QCoreApplication.translate("MainWindow", u"Tipo de Evento", None))
        self.actionEvento.setText(QCoreApplication.translate("MainWindow", u"Evento", None))
        self.actionTipoDespesa.setText(QCoreApplication.translate("MainWindow", u"Tipo de Despesa", None))
        self.actionDespesa.setText(QCoreApplication.translate("MainWindow", u"Despesa", None))
        self.actionReceita.setText(QCoreApplication.translate("MainWindow", u"Receita", None))
        self.actionPreco.setText(QCoreApplication.translate("MainWindow", u"Preco", None))
        self.actionApresentacao.setText(QCoreApplication.translate("MainWindow", u"Apresenta\u00e7\u00e3o", None))
        self.menuCadastro.setTitle(QCoreApplication.translate("MainWindow", u"Casdastro", None))
    # retranslateUi

