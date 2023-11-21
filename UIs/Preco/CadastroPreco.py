from UIs.Preco.CadastroPrecoDialog_ui import *
from PySide6.QtCore import Slot
from helpers import *


class CadastroPreco(QDialog):
    def __init__(self, parent=None):
        super(CadastroPreco, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.sair)

        self.preco = Preco()
        self.preco.id = 0

        self.form_pesquisa = None

        artistas = session.query(Artista).all()
        eventos = session.query(Evento).all()

        for artista in artistas:
            self.ui.comboBoxArtista.addItem(artista.nome)

        for evento in eventos:
            self.ui.comboBoxEvento.addItem(format_evento(evento))

        # Definições Padrão
        # self.ui.lineEditLocalizacao.setMaxLength(100)

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def clear_all(self):
        self.ui.doubleSpinBoxCache.clear()

    @Slot()
    def salvar(self):
        try:
            self.preco.cache = self.ui.doubleSpinBoxCache.value()
            self.preco.artista_id = get_artista_by_name(self.ui.comboBoxArtista.currentText())
            self.preco.evento_id = get_evento_by_format(self.ui.comboBoxEvento.currentText())

            if self.preco.id <= 0:
                session.add(self.preco)
            else:
                session.merge(self.preco)

            session.commit()

            self.clear_all()

            self.preco = Preco()
            self.preco.id = 0

            self.close()

        except Exception as ex:
            print(ex)

    @Slot()
    def sair(self):
        self.clear_all()
        self.close()
