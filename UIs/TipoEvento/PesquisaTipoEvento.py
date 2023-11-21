from UIs.FormPesquisa import *
from UIs.TipoEvento.CadastroTipoEvento import *
from conexao import *


class PesquisaTipoEvento(QWidget):
    def __init__(self, parent=None):
        super(PesquisaTipoEvento, self).__init__(parent)

        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Tipo Evento - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

        self.cadastro = CadastroTipoEvento()
        self.tipo_evento = None

    def exibir_cadastro(self):
        self.cadastro = CadastroTipoEvento()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()

        tipo_evento = TipoEvento()

        tipo_evento.id = (table.item(linha, 0)).text()
        tipo_evento.nome = (table.item(linha, 1)).text()

        self.tipo_evento = tipo_evento

        self.cadastro.ui.lineEditNome.setText(tipo_evento.nome)
        self.cadastro.tipo_evento.id = int(tipo_evento.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(TipoEvento).filter(TipoEvento.nome.contains(valor_pesquisa)).all()
        else:
            resultados = session.query(TipoEvento).all()

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
                tipo_evento = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{tipo_evento.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{tipo_evento.nome}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
