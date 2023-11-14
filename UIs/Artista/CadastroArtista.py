from UIs.Artista.CadastroArtistaDialog_ui import *
from conexao import *
from entity import Artista
from entity import Genero
from PySide6.QtCore import Slot


class CadastroArtista(QDialog):
    def __init__(self, parent=None):
        super(CadastroArtista, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)

        self.artista = Artista()
        self.artista.id = 0

        self.form_pesquisa = None

        generos = session.query(Genero).all()

        for genero in generos:
            self.ui.comboBoxGenero.addItem(genero.nome)

        # Definições Padrão
        self.ui.lineEditNome.setMaxLength(100)

        self.ui.lineEditTelefone.setMaxLength(16)
        self.ui.lineEditTelefone.setInputMask('(00) 0 0000-0000')

        self.ui.lineEditEmail.setMaxLength(100)
        self.ui.lineEditPagina.setMaxLength(100)

    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    def get_genero_id(self):
        genero = session.query(Genero).filter(Genero.nome.contains(self.ui.comboBoxGenero.currentText())).first()
        return genero.id

    @Slot()
    def salvar(self):
        try:
            self.artista.nome = self.ui.lineEditNome.text()
            self.artista.telefone = self.ui.lineEditTelefone.text()
            self.artista.email = self.ui.lineEditEmail.text()
            self.artista.pagina_web = self.ui.lineEditPagina.text()
            self.artista.genero_id = self.get_genero_id()

            if self.artista.pagina_web == "":
                self.artista.pagina_web = None

            if self.artista.id <= 0:
                session.add(self.artista)
            else:
                session.merge(self.artista)

            session.commit()

            self.artista = Artista()
            self.artista.id = 0

            self.ui.lineEditNome.setText("")
            self.ui.lineEditTelefone.setText("")
            self.ui.lineEditEmail.setText("")
            self.ui.lineEditPagina.setText("")

            self.close()

        except Exception as ex:
            print(ex)
