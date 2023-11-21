from UIs.Evento.CadastroEventoDialog_ui import *
from helpers import *
from PySide6.QtCore import Slot


class CadastroEvento(QDialog):
    def __init__(self, parent=None):
        super(CadastroEvento, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.sair)

        self.evento = Evento()
        self.evento.id = 0

        self.form_pesquisa = None

        tipo_eventos = session.query(TipoEvento).all()
        cidades = session.query(Cidade).all()

        for tipo_evento in tipo_eventos:
            self.ui.comboBoxTipoEvento.addItem(tipo_evento.nome)

        for cidade in cidades:
            self.ui.comboBoxCidade.addItem(cidade.nome)

        # Definições Padrão
        self.ui.lineEditLocalizacao.setMaxLength(100)

        if self.evento.id == 0:
            self.ui.dateEditData.setDate(QDate.currentDate())

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def clear_all(self):
        self.ui.dateEditData.clear()
        self.ui.lineEditLocalizacao.setText("")

    @Slot()
    def salvar(self):
        try:
            self.evento.data = format_date_to_sql(self.ui.dateEditData.text())
            self.evento.localizacao = self.ui.lineEditLocalizacao.text()
            self.evento.tipo_evento_id = get_tipo_evento_by_name(self.ui.comboBoxTipoEvento.currentText())
            self.evento.cidade_id = get_cidade_by_name(self.ui.comboBoxCidade.currentText())

            if self.evento.id <= 0:
                session.add(self.evento)
            else:
                session.merge(self.evento)

            session.commit()

            self.clear_all()

            self.evento = Evento()
            self.evento.id = 0

            self.close()

        except Exception as ex:
            print(ex)

    @Slot()
    def sair(self):
        self.clear_all()
        self.close()
