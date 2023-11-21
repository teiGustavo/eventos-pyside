from UIs.Despesa.CadastroDespesaDialog_ui import *
from PySide6.QtCore import Slot
from helpers import *


class CadastroDespesa(QDialog):
    def __init__(self, parent=None):
        super(CadastroDespesa, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.sair)

        self.despesa = Despesa()
        self.despesa.id = 0

        self.form_pesquisa = None

        tipo_despesas = session.query(TipoDespesa).all()
        eventos = session.query(Evento).all()

        for tipo_despesa in tipo_despesas:
            self.ui.comboBoxTipoDespesa.addItem(tipo_despesa.nome)

        for evento in eventos:
            self.ui.comboBoxEvento.addItem(format_evento(evento))

        # Definições Padrão
        if self.despesa.id == 0:
            self.ui.dateEditData.setDate(QDate.currentDate())

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def clear_all(self):
        self.ui.lineEditDescricao.setText("")
        self.ui.doubleSpinBoxValor.setValue(0)
        self.ui.dateEditData.clear()

    @Slot()
    def salvar(self):
        try:
            self.despesa.descricao = self.ui.lineEditDescricao.text()
            self.despesa.valor = self.ui.doubleSpinBoxValor.value()
            self.despesa.data = format_date_to_sql(self.ui.dateEditData.text())
            self.despesa.tipo_despesa_id = get_tipo_despesa_by_name(self.ui.comboBoxTipoDespesa.currentText())
            self.despesa.evento_id = get_evento_by_format(self.ui.comboBoxEvento.currentText())

            if self.despesa.id <= 0:
                session.add(self.despesa)
            else:
                session.merge(self.despesa)

            session.commit()

            self.clear_all()

            self.despesa = Despesa()
            self.despesa.id = 0

            self.close()

        except Exception as ex:
            print(ex)

    @Slot()
    def sair(self):
        self.clear_all()
        self.close()
