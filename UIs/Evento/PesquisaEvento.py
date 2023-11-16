from UIs.FormPesquisa import *
from UIs.Evento.CadastroEvento import *
from helpers import *


class PesquisaEvento(QWidget):
    def __init__(self, parent=None):
        super(PesquisaEvento, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Evento - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleciona_linha)

    def exibir_cadastro(self):
        self.cadastro = CadastroEvento()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleciona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroEvento()

        evento = Evento()

        evento.id = (table.item(linha, 0)).text()
        evento.data = format_date_to_sql((table.item(linha, 1)).text())
        evento.localizacao = (table.item(linha, 2)).text()

        tipo_evento = (table.item(linha, 3)).text()
        evento.tipo_evento_id = get_tipo_evento_by_name(tipo_evento)

        cidade = (table.item(linha, 4)).text()
        evento.cidade_id = get_cidade_by_name(cidade)

        self.evento = evento

        self.cadastro.ui.dateEditData.dateTimeFromText(evento.data)
        self.cadastro.ui.lineEditLocalizacao.setText(evento.localizacao)

        index = self.cadastro.ui.comboBoxTipoEvento.findText(tipo_evento)
        self.cadastro.ui.comboBoxTipoEvento.setCurrentIndex(index)

        index = self.cadastro.ui.comboBoxCidade.findText(cidade)
        self.cadastro.ui.comboBoxCidade.setCurrentIndex(index)

        self.cadastro.evento.id = int(evento.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Evento).filter(
                Evento.data.contains(valor_pesquisa) | Evento.localizacao.contains(valor_pesquisa)
            ).all()
        else:
            resultados = session.query(Evento).all()

        total = len(resultados)

        colunas = ['ID', 'Data', 'Localização', 'Tipo de Evento', 'Cidade']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                evento = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{evento.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{unformat_sql_date(evento.data)}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{evento.localizacao}")
                if coluna == 3:
                    valor = QTableWidgetItem(f"{get_tipo_evento_by_id(evento.tipo_evento_id)}")
                if coluna == 4:
                    valor = QTableWidgetItem(f"{get_cidade_by_id(evento.cidade_id)}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
