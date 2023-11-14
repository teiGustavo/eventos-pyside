from UIs.FormPesquisa import *
from UIs.Artista.CadastroArtista import *
from conexao import *
from entity import Artista
from entity import Genero


def get_genero_by_id(genero_id):
    genero = session.query(Genero).filter(Genero.id == genero_id).first()
    return genero.nome


def get_genero_by_name(nome_genero):
    genero = session.query(Genero).filter(Genero.nome.contains(nome_genero)).first()
    return genero.id


class PesquisaArtista(QWidget):
    def __init__(self, parent=None):
        super(PesquisaArtista, self).__init__(parent)
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)
        self.setWindowTitle("Artista - Eventos")

        self.preencher_tabela()

        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)
        self.ui.EditValorPesquisa.textChanged.connect(self.pesquisar)
        self.ui.BtnPesquisar.clicked.connect(self.pesquisar)
        self.ui.tableResultado.cellDoubleClicked.connect(self.seleiona_linha)

        self.cadastro = CadastroArtista()
        self.artista = None

    def exibir_cadastro(self):
        self.cadastro = CadastroArtista()
        self.cadastro.form_pesquisa = self
        self.cadastro.show()

    def pesquisar(self):
        self.preencher_tabela()

    def seleiona_linha(self):
        table = self.ui.tableResultado
        linha = table.currentIndex().row()
        self.cadastro = CadastroArtista()

        artista = Artista()

        artista.id = (table.item(linha, 0)).text()
        artista.nome = (table.item(linha, 1)).text()
        artista.telefone = (table.item(linha, 2)).text()
        artista.email = (table.item(linha, 3)).text()
        artista.pagina_web = (table.item(linha, 4)).text()

        nome_genero = (table.item(linha, 5)).text()
        artista.genero_id = get_genero_by_name(nome_genero)

        self.artista = artista

        self.cadastro.ui.lineEditNome.setText(artista.nome)
        self.cadastro.ui.lineEditTelefone.setText(artista.telefone)
        self.cadastro.ui.lineEditEmail.setText(artista.email)
        self.cadastro.ui.lineEditPagina.setText(artista.pagina_web)

        index = self.cadastro.ui.comboBoxGenero.findText(nome_genero)
        self.cadastro.ui.comboBoxGenero.setCurrentIndex(index)

        self.cadastro.artista.id = int(artista.id)

        self.cadastro.form_pesquisa = self

        self.cadastro.show()

    def preencher_tabela(self):
        valor_pesquisa = self.ui.EditValorPesquisa.text()

        if valor_pesquisa != "":
            resultados = session.query(Artista).filter(Artista.nome.contains(valor_pesquisa)).all()
        else:
            resultados = session.query(Artista).join(Genero).all()

        total = len(resultados)

        colunas = ['ID', 'Nome', 'Telefone', 'Email', 'Pagina Web', 'Gênero']

        self.ui.tableResultado.setRowCount(0)

        self.ui.tableResultado.setRowCount(total)

        total_colunas = len(colunas)

        self.ui.tableResultado.setColumnCount(total_colunas)
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        for linha in range(total):
            for coluna in range(total_colunas):
                valor = None
                artista = resultados[linha]
                if coluna == 0:
                    valor = QTableWidgetItem(f"{artista.id}")
                if coluna == 1:
                    valor = QTableWidgetItem(f"{artista.nome}")
                if coluna == 2:
                    valor = QTableWidgetItem(f"{artista.telefone}")
                if coluna == 3:
                    valor = QTableWidgetItem(f"{artista.email}")
                if coluna == 4:
                    valor = QTableWidgetItem(f"{artista.pagina_web}")
                if coluna == 5:
                    valor = QTableWidgetItem(f"{get_genero_by_id(artista.genero_id)}")

                self.ui.tableResultado.setItem(linha, coluna, valor)
