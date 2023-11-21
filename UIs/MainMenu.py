from UIs.Estado.PesquisaEstado import *
from UIs.Cidade.PesquisaCidade import *
from UIs.Genero.PesquisaGenero import *
from UIs.Artista.PesquisaArtista import *
from UIs.TipoEvento.PesquisaTipoEvento import *
from UIs.Evento.PesquisaEvento import *
from UIs.Preco.PesquisaPreco import *
from UIs.Apresentacao.PesquisaApresentacao import *
from UIs.TipoDespesa.PesquisaTipoDespesa import *
from UIs.Despesa.PesquisaDespesa import *
from UIs.Receita.PesquisaReceita import *
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
        self.ui.actionArtista.triggered.connect(self.exibe_pesquisa_artista)
        self.ui.actionTipoEvento.triggered.connect(self.exibe_pesquisa_tipo_evento)
        self.ui.actionEvento.triggered.connect(self.exibe_pesquisa_evento)
        self.ui.actionPreco.triggered.connect(self.exibe_pesquisa_preco)
        self.ui.actionApresentacao.triggered.connect(self.exibe_pesquisa_apresentacao)
        self.ui.actionTipoDespesa.triggered.connect(self.exibe_pesquisa_tipo_despesa)
        self.ui.actionDespesa.triggered.connect(self.exibe_pesquisa_despesa)
        self.ui.actionReceita.triggered.connect(self.exibe_pesquisa_receita)

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

    @Slot()
    def exibe_pesquisa_tipo_evento(self):
        self.pesquisa_tipo_evento = PesquisaTipoEvento(parent=None)
        self.pesquisa_tipo_evento.show()

    @Slot()
    def exibe_pesquisa_evento(self):
        self.pesquisa_evento = PesquisaEvento(parent=None)
        self.pesquisa_evento.show()

    @Slot()
    def exibe_pesquisa_preco(self):
        self.pesquisa_preco = PesquisaPreco(parent=None)
        self.pesquisa_preco.show()

    @Slot()
    def exibe_pesquisa_apresentacao(self):
        self.pesquisa_apresentacao = PesquisaApresentacao(parent=None)
        self.pesquisa_apresentacao.show()

    @Slot()
    def exibe_pesquisa_tipo_despesa(self):
        self.pesquisa_tipo_despesa = PesquisaTipoDespesa(parent=None)
        self.pesquisa_tipo_despesa.show()

    @Slot()
    def exibe_pesquisa_despesa(self):
        self.pesquisa_despesa = PesquisaDespesa(parent=None)
        self.pesquisa_despesa.show()

    @Slot()
    def exibe_pesquisa_receita(self):
        self.pesquisa_receita = PesquisaReceita(parent=None)
        self.pesquisa_receita.show()
