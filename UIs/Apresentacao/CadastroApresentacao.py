from UIs.Apresentacao.CadastroApresentacaoDialog_ui import *
from PySide6.QtCore import Slot
from helpers import *


class CadastroApresentacao(QDialog):
    def __init__(self, parent=None):
        super(CadastroApresentacao, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.sair)

        self.apresentacao = Apresentacao()
        self.apresentacao.id = 0

        self.form_pesquisa = None

        artistas = session.query(Artista).all()
        eventos = session.query(Evento).all()

        for artista in artistas:
            self.ui.comboBoxArtista.addItem(artista.nome)

        for evento in eventos:
            self.ui.comboBoxEvento.addItem(format_evento(evento))

        # Definições Padrão
        if self.apresentacao.id == 0:
            self.ui.dateEditData.setDate(QDate.currentDate())

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def clear_all(self):
        self.ui.dateEditData.clear()
        self.ui.doubleSpinBoxValorIngresso.setValue(0)
        self.ui.spinBoxPublicoMaximo.setValue(0)
        self.ui.spinBoxPublicoPresente.setValue(0)

    @Slot()
    def salvar(self):
        try:
            self.apresentacao.data = format_date_to_sql(self.ui.dateEditData.text())
            self.apresentacao.valor_ingresso = self.ui.doubleSpinBoxValorIngresso.value()
            self.apresentacao.publico_maximo = self.ui.spinBoxPublicoMaximo.value()
            self.apresentacao.publico_presente = self.ui.spinBoxPublicoPresente.value()
            self.apresentacao.artista_id = get_artista_by_name(self.ui.comboBoxArtista.currentText())
            self.apresentacao.evento_id = get_evento_by_format(self.ui.comboBoxEvento.currentText())

            if self.apresentacao.id <= 0:
                session.add(self.apresentacao)
            else:
                session.merge(self.apresentacao)

            session.commit()

            self.clear_all()

            self.apresentacao = Apresentacao()
            self.apresentacao.id = 0

            self.close()

        except Exception as ex:
            print(ex)

    @Slot()
    def sair(self):
        self.clear_all()
        self.close()
