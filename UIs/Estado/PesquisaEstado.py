from UIs.FormPesquisa import *
from UIs.Estado.CadastroEstado import *
from conexao import *


class PesquisaEstado(QWidget):
    def __init__(self, parent=None):
        super(PesquisaEstado, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Estado - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro_estado)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

    def exibir_cadastro_estado(self):
        self.cadastro = CadastroEstado()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroEstado()

        estado = Estado()

        estado.id = (table.item(linha, 0)).text()
        estado.nome = (table.item(linha, 1)).text()
        estado.abreviacao = (table.item(linha, 2)).text()

        self.cadastro = CadastroEstado()
        self.estado = estado

        self.cadastro.ui.lineEditNome.setText(estado.nome)
        self.cadastro.ui.lineEditSigla.setText(estado.abreviacao)
        self.cadastro.estado.id = int(estado.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Estado).filter(
                Estado.nome.contains(valor_pesquisa) | Estado.abreviacao.contains(valor_pesquisa)
            ).all()
        else:
            resultados = session.query(Estado).all()

        total = len(resultados)

        colunas = ['ID', 'Nome', 'Abreviação']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                estado = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{estado.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{estado.nome}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{estado.abreviacao}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
