from UIs.Receita.CadastroReceitaDialog_ui import *
from PySide6.QtCore import Slot
from helpers import *


class CadastroReceita(QDialog):
    def __init__(self, parent=None):
        super(CadastroReceita, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.sair)

        self.receita = Receita()
        self.receita.id = 0

        self.form_pesquisa = None

        eventos = session.query(Evento).all()

        for evento in eventos:
            self.ui.comboBoxEvento.addItem(format_evento(evento))

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def clear_all(self):
        self.ui.doubleSpinBoxValor.setValue(0)

    @Slot()
    def salvar(self):
        try:
            self.receita.valor = self.ui.doubleSpinBoxValor.value()
            self.receita.evento_id = get_evento_by_format(self.ui.comboBoxEvento.currentText())

            if self.receita.id <= 0:
                session.add(self.receita)
            else:
                session.merge(self.receita)

            session.commit()

            self.clear_all()

            self.receita = Receita()
            self.receita.id = 0

            self.close()

        except Exception as ex:
            print(ex)

    @Slot()
    def sair(self):
        self.clear_all()
        self.close()
