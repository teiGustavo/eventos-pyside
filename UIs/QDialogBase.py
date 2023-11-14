import sys
from typing import Optional
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtWidgets import QPushButton, QLineEdit, QTableView, QTableWidget, QTableWidgetItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QObject, Slot


class QDialogBase(QDialog):
    def __init__(self, ui_file_name, parent):
        super().__init__(parent)
        loader = QUiLoader()

        ui_file = QFile(f'Uis/{ui_file_name}')

        if not ui_file.open(QIODevice.ReadOnly):
            msg = "Erro ao abrir o arquivo: "
            print(f"{msg} {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file, self)

        ui_file.close()

    def show(self):
        self.ui.show()

    def showMaximized(self):
        self.ui.showMaximized()
