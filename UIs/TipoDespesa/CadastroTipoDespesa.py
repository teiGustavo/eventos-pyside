from UIs.TipoDespesa.CadastroTipoDespesaDialog_ui import *
from conexao import *
from entity import TipoDespesa
from PySide6.QtCore import Slot


class CadastroTipoDespesa(QDialog):
    def __init__(self, parent=None):
        super(CadastroTipoDespesa, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.sair)

        self.tipo_despesa = TipoDespesa()
        self.tipo_despesa.id = 0

        self.form_pesquisa = None

        # Definições Padrão
        self.ui.lineEditNome.setMaxLength(100)

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def clear_all(self):
        self.ui.lineEditNome.setText("")

    @Slot()
    def salvar(self):
        try:
            self.tipo_despesa.nome = self.ui.lineEditNome.text()

            if self.tipo_despesa.id <= 0:
                session.add(self.tipo_despesa)
            else:
                session.merge(self.tipo_despesa)

            session.commit()

            self.clear_all()

            self.tipo_despesa = TipoDespesa()
            self.tipo_despesa.id = 0

            self.close()

        except Exception as ex:
            print(ex)

    @Slot()
    def sair(self):
        self.clear_all()
        self.close()
