from UIs.FormPesquisa import *
from UIs.Receita.CadastroReceita import *
from helpers import *


class PesquisaReceita(QWidget):
    def __init__(self, parent=None):
        super(PesquisaReceita, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Receita - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

        self.cadastro = CadastroReceita()
        self.receita = None

    def exibir_cadastro(self):
        self.cadastro = CadastroReceita()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroReceita()

        receita = Receita()

        receita.id = (table.item(linha, 0)).text()
        receita.valor = unformat_monetary((table.item(linha, 1)).text())

        evento_formatado = (table.item(linha, 2)).text()
        receita.evento_id = get_evento_by_format(evento_formatado)

        self.receita = receita

        self.cadastro.ui.doubleSpinBoxValor.setValue(float(receita.valor))

        index = self.cadastro.ui.comboBoxEvento.findText(evento_formatado)
        self.cadastro.ui.comboBoxEvento.setCurrentIndex(index)

        self.cadastro.receita.id = int(receita.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Receita).filter(Receita.valor.contains(valor_pesquisa)).all()
        else:
            resultados = session.query(Receita).join(Evento).all()

        total = len(resultados)

        colunas = ['ID', 'Valor', 'Evento']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)
        self.ui.tableResultado.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                receita = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{receita.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{format_monetary(receita.valor)}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{get_evento_by_id(receita.evento_id)}")
                    self.ui.tableResultado.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

                self.ui.tableResultado.setItem(linha, coluna, valor)
