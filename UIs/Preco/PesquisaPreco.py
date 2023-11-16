from UIs.FormPesquisa import *
from UIs.Preco.CadastroPreco import *
from helpers import *


class PesquisaPreco(QWidget):
    def __init__(self, parent=None):
        super(PesquisaPreco, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Preço - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleciona_linha)

    def exibir_cadastro(self):
        self.cadastro = CadastroPreco()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleciona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroPreco()

        preco = Preco()

        preco.id = (table.item(linha, 0)).text()
        preco.cache = (table.item(linha, 1)).text()

        artista = (table.item(linha, 2)).text()
        preco.artista_id = get_artista_by_name(artista)

        evento = (table.item(linha, 3)).text()
        preco.evento_id = get_evento_by_format(evento)

        self.preco = preco

        self.cadastro.ui.doubleSpinBoxCache.setValue(float(preco.cache))

        index = self.cadastro.ui.comboBoxArtista.findText(artista)
        self.cadastro.ui.comboBoxArtista.setCurrentIndex(index)

        index = self.cadastro.ui.comboBoxEvento.findText(evento)
        self.cadastro.ui.comboBoxEvento.setCurrentIndex(index)

        self.cadastro.preco.id = int(preco.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Preco).filter(
                Preco.cache.contains(valor_pesquisa)
            ).all()
        else:
            resultados = session.query(Preco).all()

        total = len(resultados)

        colunas = ['ID', 'Cachê', 'Artista', 'Evento']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                preco = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{preco.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{preco.cache}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{get_artista_by_id(preco.artista_id)}")
                if coluna == 3:
                    valor = QTableWidgetItem(f"{get_evento_by_id(preco.evento_id)}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
