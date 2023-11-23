from UIs.FormPesquisa import *
from UIs.TipoDespesa.CadastroTipoDespesa import *
from conexao import *


class PesquisaTipoDespesa(QWidget):
    def __init__(self, parent=None):
        super(PesquisaTipoDespesa, self).__init__(parent)

        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Tipo de Despesa - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

        self.cadastro = CadastroTipoDespesa()
        self.tipo_evento = None

    def exibir_cadastro(self):
        self.cadastro = CadastroTipoDespesa()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()

        tipo_despesa = TipoDespesa()

        tipo_despesa.id = (table.item(linha, 0)).text()
        tipo_despesa.nome = (table.item(linha, 1)).text()

        self.tipo_despesa = tipo_despesa

        self.cadastro.ui.lineEditNome.setText(tipo_despesa.nome)
        self.cadastro.tipo_despesa.id = int(tipo_despesa.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(TipoDespesa).filter(TipoDespesa.nome.contains(valor_pesquisa)).all()
        else:
            resultados = session.query(TipoDespesa).all()

        total = len(resultados)

        colunas = ['ID', 'Nome']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)
        self.ui.tableResultado.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                tipo_despesa = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{tipo_despesa.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{tipo_despesa.nome}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
