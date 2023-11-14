from UIs.FormPesquisa import *
from UIs.Genero.CadastroGenero import *
from conexao import *


class PesquisaGenero(QWidget):
    def __init__(self, parent=None):
        super(PesquisaGenero, self).__init__(parent)

        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Gênero - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro_genero)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

        self.cadastro = CadastroGenero()
        self.genero = None

    def exibir_cadastro_genero(self):
        self.cadastro = CadastroGenero()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()

        genero = Genero()

        genero.id = (table.item(linha, 0)).text()
        genero.nome = (table.item(linha, 1)).text()

        self.genero = genero

        self.cadastro.ui.lineEditNome.setText(genero.nome)
        self.cadastro.genero.id = int(genero.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Genero).filter(Genero.nome.contains(valor_pesquisa)).all()
        else:
            resultados = session.query(Genero).all()

        total = len(resultados)

        colunas = ['ID', 'Nome']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                genero = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{genero.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{genero.nome}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
