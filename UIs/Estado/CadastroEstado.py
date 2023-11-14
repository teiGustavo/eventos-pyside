from UIs.Estado.CadastroEstadoDialog_ui import *
from conexao import *
from entity import Estado
from PySide6.QtCore import Slot


class CadastroEstado(QDialog):
    def __init__(self, parent=None):
        super(CadastroEstado, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)

        self.estado = Estado()
        self.estado.id = 0

        self.form_pesquisa = None

        # Definições Padrão
        self.ui.lineEditNome.setMaxLength(100)
        self.ui.lineEditSigla.setMaxLength(2)

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    @Slot()
    def salvar(self):
        try:
            self.estado.nome = self.ui.lineEditNome.text()
            self.estado.abreviacao = self.ui.lineEditSigla.text()

            if self.estado.id <= 0:
                session.add(self.estado)
            else:
                session.merge(self.estado)

            session.commit()

            self.ui.lineEditNome.setText("")
            self.ui.lineEditSigla.setText("")

            self.estado = Estado()
            self.estado.id = 0

            self.close()

        except Exception as ex:
            print(ex)
