from UIs.Genero.CadastroGeneroDialog_ui import *
from conexao import *
from entity import Estado
from PySide6.QtCore import Slot


class CadastroGenero(QDialog):
    def __init__(self, parent=None):
        super(CadastroGenero, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)

        self.genero = Genero()
        self.genero.id = 0

        self.form_pesquisa = None

        # Definições Padrão
        self.ui.lineEditNome.setMaxLength(100)

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    @Slot()
    def salvar(self):
        try:
            self.genero.nome = self.ui.lineEditNome.text()

            if self.genero.id <= 0:
                session.add(self.genero)
            else:
                session.merge(self.genero)

            session.commit()

            self.ui.lineEditNome.setText("")

            self.genero = Genero()
            self.genero.id = 0

            self.close()

        except Exception as ex:
            print(ex)
