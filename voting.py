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


#References:
#https://www.w3schools.com/python/
#https://www.youtube.com/watch?v=SelawmXHtPg&list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB
#https://www.youtube.com/watch?v=Lx-kfm5jCUw&t=191s