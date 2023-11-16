from UIs.Cidade.CadastroCidadeDialog_ui import *
from conexao import *
from entity import Estado
from entity import Cidade
from PySide6.QtCore import Slot
from helpers import *


class CadastroCidade(QDialog):
    def __init__(self, parent=None):
        super(CadastroCidade, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)

        self.cidade = Cidade()
        self.cidade.id = 0

        self.form_pesquisa = None

        estados = session.query(Estado).all()

        for estado in estados:
            self.ui.comboBoxEstado.addItem(estado.nome)

        # Definições Padrão
        self.ui.lineEditNome.setMaxLength(100)

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    @Slot()
    def salvar(self):
        try:
            self.cidade.nome = self.ui.lineEditNome.text()
            self.cidade.estado_id = get_estado_by_name(self.ui.comboBoxEstado.currentText())

            if self.cidade.id <= 0:
                session.add(self.cidade)
            else:
                session.merge(self.cidade)

            session.commit()

            self.ui.lineEditNome.setText("")

            self.cidade = Cidade()
            self.cidade.id = 0

            self.close()

        except Exception as ex:
            print(ex)
