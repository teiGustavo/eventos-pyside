from UIs.Estado.PesquisaEstado import *
from UIs.Cidade.PesquisaCidade import *
from UIs.Genero.PesquisaGenero import *
from UIs.Artista.PesquisaArtista import *
from UIs.MainMenu_ui import *
from PySide6.QtCore import Slot


class MainMenu(QMainWindow):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionEstado.triggered.connect(self.exibe_pesquisa_estado)
        self.ui.actionCidade.triggered.connect(self.exibe_pesquisa_cidade)
        self.ui.actionGenero.triggered.connect(self.exibe_pesquisa_genero)
        self.ui.actionGenero.triggered.connect(self.exibe_pesquisa_genero)
        self.ui.actionArtista.triggered.connect(self.exibe_pesquisa_artista)

    @Slot()
    def exibe_pesquisa_estado(self):
        self.pesquisa_estado = PesquisaEstado(parent=None)
        self.pesquisa_estado.show()

    @Slot()
    def exibe_pesquisa_cidade(self):
        self.pesquisa_cidade = PesquisaCidade(parent=None)
        self.pesquisa_cidade.show()

    @Slot()
    def exibe_pesquisa_genero(self):
        self.pesquisa_genero = PesquisaGenero(parent=None)
        self.pesquisa_genero.show()

    @Slot()
    def exibe_pesquisa_artista(self):
        self.pesquisa_artista = PesquisaArtista(parent=None)
        self.pesquisa_artista.show()
