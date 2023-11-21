from UIs.FormPesquisa import *
from UIs.Apresentacao.CadastroApresentacao import *
from helpers import *


class PesquisaApresentacao(QWidget):
    def __init__(self, parent=None):
        super(PesquisaApresentacao, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Apresentacao - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleciona_linha)

    def exibir_cadastro(self):
        self.cadastro = CadastroApresentacao()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleciona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroApresentacao()

        apresentacao = Apresentacao()

        apresentacao.id = (table.item(linha, 0)).text()
        apresentacao.data = format_date_to_sql((table.item(linha, 1)).text())
        apresentacao.valor_ingresso = unformat_monetary((table.item(linha, 2)).text())
        apresentacao.publico_maximo = unformat_integer((table.item(linha, 3)).text())
        apresentacao.publico_presente = unformat_integer((table.item(linha, 4)).text())

        artista = (table.item(linha, 5)).text()
        apresentacao.artista_id = get_artista_by_name(artista)

        evento = (table.item(linha, 6)).text()
        apresentacao.evento_id = get_evento_by_format(evento)

        self.apresentacao = apresentacao

        self.cadastro.ui.dateEditData.setDate(QDate.fromString(apresentacao.data, "yyyy-MM-dd"))
        self.cadastro.ui.doubleSpinBoxValorIngresso.setValue(float(apresentacao.valor_ingresso))
        self.cadastro.ui.spinBoxPublicoMaximo.setValue(int(apresentacao.publico_maximo))
        self.cadastro.ui.spinBoxPublicoPresente.setValue(int(apresentacao.publico_presente))

        index = self.cadastro.ui.comboBoxArtista.findText(artista)
        self.cadastro.ui.comboBoxArtista.setCurrentIndex(index)

        index = self.cadastro.ui.comboBoxEvento.findText(evento)
        self.cadastro.ui.comboBoxEvento.setCurrentIndex(index)

        self.cadastro.apresentacao.id = int(apresentacao.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Apresentacao).filter(
                Apresentacao.data.contains(valor_pesquisa) | Apresentacao.valor_ingresso.contains(valor_pesquisa) |
                Apresentacao.publico_maximo.contains(valor_pesquisa)
            ).all()
        else:
            resultados = session.query(Apresentacao).all()

        total = len(resultados)

        colunas = ['ID', 'Data', 'Valor do Ingresso', 'Público Máximo', 'Público Presente', 'Artista', 'Evento']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                apresentacao = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{apresentacao.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{unformat_sql_date(apresentacao.data)}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{format_monetary(apresentacao.valor_ingresso)}")
                if coluna == 3:
                    valor = QTableWidgetItem(f"{format_integer(apresentacao.publico_maximo)}")
                if coluna == 4:
                    valor = QTableWidgetItem(f"{format_integer(apresentacao.publico_presente)}")
                if coluna == 5:
                    valor = QTableWidgetItem(f"{get_artista_by_id(apresentacao.artista_id)}")
                    self.ui.tableResultado.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
                if coluna == 6:
                    valor = QTableWidgetItem(f"{get_evento_by_id(apresentacao.evento_id)}")
                    self.ui.tableResultado.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)

                self.ui.tableResultado.setItem(linha, coluna, valor)
