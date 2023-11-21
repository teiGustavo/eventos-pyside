from UIs.Genero.CadastroGeneroDialog_ui import *
from conexao import *
from PySide6.QtCore import Slot


class CadastroGenero(QDialog):
    def __init__(self, parent=None):
        super(CadastroGenero, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.sair)

        self.genero = Genero()
        self.genero.id = 0

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
            self.genero.nome = self.ui.lineEditNome.text()

            if self.genero.id <= 0:
                session.add(self.genero)
            else:
                session.merge(self.genero)

            session.commit()

            self.clear_all()

            self.genero = Genero()
            self.genero.id = 0

            self.close()

        except Exception as ex:
            print(ex)

    @Slot()
    def sair(self):
        self.clear_all()
        self.close()
