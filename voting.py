import sys
from PyQt6.QtWidgets import *
from vote import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = VotingAppWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('School Voting')
    MainWindow.show()
    sys.exit(app.exec())
