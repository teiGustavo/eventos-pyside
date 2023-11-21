from UIs.FormPesquisa import *
from UIs.Despesa.CadastroDespesa import *
from helpers import *


class PesquisaDespesa(QWidget):
    def __init__(self, parent=None):
        super(PesquisaDespesa, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Despesa - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

        self.cadastro = CadastroDespesa()
        self.despesa = None

    def exibir_cadastro(self):
        self.cadastro = CadastroDespesa()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroDespesa()

        despesa = Despesa()

        despesa.id = (table.item(linha, 0)).text()
        despesa.descricao = (table.item(linha, 2)).text()
        despesa.valor = unformat_monetary((table.item(linha, 3)).text())
        despesa.data = format_date_to_sql((table.item(linha, 1)).text())

        nome_tipo_despesa = (table.item(linha, 4)).text()
        despesa.tipo_despesa_id = get_tipo_despesa_by_name(nome_tipo_despesa)

        evento_formatado = (table.item(linha, 5)).text()
        despesa.evento_id = get_evento_by_format(evento_formatado)

        self.despesa = despesa

        self.cadastro.ui.lineEditDescricao.setText(despesa.descricao)
        self.cadastro.ui.doubleSpinBoxValor.setValue(float(despesa.valor))
        self.cadastro.ui.dateEditData.setDate(QDate.fromString(despesa.data, "yyyy-MM-dd"))

        index = self.cadastro.ui.comboBoxTipoDespesa.findText(nome_tipo_despesa)
        self.cadastro.ui.comboBoxTipoDespesa.setCurrentIndex(index)

        index = self.cadastro.ui.comboBoxEvento.findText(evento_formatado)
        self.cadastro.ui.comboBoxEvento.setCurrentIndex(index)

        self.cadastro.despesa.id = int(despesa.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Despesa).filter(Despesa.valor.contains(valor_pesquisa)).all()
        else:
            resultados = session.query(Despesa).join(Evento).all()

        total = len(resultados)

        colunas = ['ID', 'Data', 'Descrição', 'Valor', 'Tipo de Despesa', 'Evento']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                despesa = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{despesa.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{unformat_sql_date(despesa.data)}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{despesa.descricao}")
                    self.ui.tableResultado.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
                if coluna == 3:
                    valor = QTableWidgetItem(f"{format_monetary(despesa.valor)}")
                if coluna == 4:
                    valor = QTableWidgetItem(f"{get_tipo_despesa_by_id(despesa.tipo_despesa_id)}")
                if coluna == 5:
                    valor = QTableWidgetItem(f"{get_evento_by_id(despesa.evento_id)}")
                    self.ui.tableResultado.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

                self.ui.tableResultado.setItem(linha, coluna, valor)
