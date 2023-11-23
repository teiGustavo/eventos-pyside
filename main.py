import sys
from UIs.MainMenu import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainMenu()
    window.showMaximized()
    sys.exit(app.exec())
