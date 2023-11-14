from UIs.FormPesquisa import *
from UIs.Cidade.CadastroCidade import *
from conexao import *
from entity import Estado


def get_estado_by_id(estado_id):
    estado = session.query(Estado).filter(Estado.id == estado_id).first()
    return estado.nome


def get_estado_by_name(nome_estado):
    estado = session.query(Estado).filter(Estado.nome.contains(nome_estado)).first()
    return estado.id


class PesquisaCidade(QWidget):
    def __init__(self, parent=None):
        super(PesquisaCidade, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Cidade - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

        self.cadastro = CadastroCidade()
        self.cidade = None

    def exibir_cadastro(self):
        self.cadastro = CadastroCidade()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroCidade()

        cidade = Cidade()

        cidade.id = (table.item(linha, 0)).text()
        cidade.nome = (table.item(linha, 1)).text()
        nome_estado = (table.item(linha, 2)).text()
        cidade.estado_id = get_estado_by_name(nome_estado)

        self.cidade = cidade

        self.cadastro.ui.lineEditNome.setText(cidade.nome)

        index = self.cadastro.ui.comboBoxEstado.findText(nome_estado)
        self.cadastro.ui.comboBoxEstado.setCurrentIndex(index)

        self.cadastro.cidade.id = int(cidade.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Cidade).filter(Cidade.nome.contains(valor_pesquisa)).all()
        else:
            resultados = session.query(Cidade).join(Estado).all()

        total = len(resultados)

        colunas = ['ID', 'Nome', 'Estado']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                cidade = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{cidade.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{cidade.nome}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{get_estado_by_id(cidade.estado_id)}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
