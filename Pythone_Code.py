import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hız Problemi")
        self.resize(500, 250)

        self.labelYol = QLabel("Toplam Yolu Giriniz:(Km)", self)
        self.labelYol.move(50, 30)

        self.lineEditYol = QLineEdit(self)
        self.lineEditYol.setValidator(QIntValidator())
        self.lineEditYol.setMaxLength(5)
        self.lineEditYol.move(350, 25)
        self.lineEditYol.resize(100, 40)

        self.labelSure = QLabel("Toplam Süreyi Giriniz:(Saat)", self)
        self.labelSure.move(50, 100)

        self.lineEditSure = QLineEdit(self)
        self.lineEditSure.setValidator(QIntValidator())
        self.lineEditSure.setMaxLength(5)
        self.lineEditSure.move(350, 95)
        self.lineEditSure.resize(100, 40)

        self.ButtonHesap = QPushButton("Hesapla", self)
        self.ButtonHesap.resize(350, 50)
        self.ButtonHesap.move(75, 165)

        self.ButtonHesap.clicked.connect(self.Sonuc)

    def Sonuc(self):
        hız = int(self.lineEditYol.text()) / int(self.lineEditSure.text())
        ButtonHesap = QMessageBox.information(self, 'Hız',str(hız))

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

main()
