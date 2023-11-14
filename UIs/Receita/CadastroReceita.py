from UIs.Receita.CadastroReceitaDialog_ui import *
from conexao import *
from entity import Receita
from entity import Evento
from PySide6.QtCore import Slot


class CadastroReceita(QDialog):
    def __init__(self, parent=None):
        super(CadastroReceita, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)

        self.receita = Receita()
        self.receita.id = 0

        self.form_pesquisa = None

        eventos = session.query(Evento).all()

        for evento in eventos:
            self.ui.comboBoxEvento.addItem(f"{evento.data} - {evento.localizacao}")

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def get_evento_id(self):
        combobox_evento_text = (self.ui.comboBoxEvento.currentText()).split(' - ')
        data = combobox_evento_text[0]
        localizacao = combobox_evento_text[1]

        evento = session.query(Evento).filter(
            Evento.data.contains(data), Evento.localizacao.contains(localizacao)
        ).first()

        return evento.id

    @Slot()
    def salvar(self):
        try:
            self.receita.valor = self.ui.doubleSpinBoxValor.text()
            self.receita.evento_id = self.get_evento_id()

            if self.receita.id <= 0:
                session.add(self.receita)
            else:
                session.merge(self.receita)

            session.commit()

            self.ui.doubleSpinBoxValor.setValue(0)

            self.receita = Receita()
            self.receita.id = 0

            self.close()

        except Exception as ex:
            print(ex)
