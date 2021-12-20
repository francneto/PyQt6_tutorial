from PyQt6.QtGui import QIcon,QPixmap
from PyQt6.QtWidgets import QApplication, QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1200,300,400,400)
        self.setWindowTitle("FADEC")
        # self.setFixedSize(500,300)
        # self.setFixedWidth(1000)
        # self.setFixedHeight(300)
        self.setStyleSheet("background-color:blue")
        self.setWindowOpacity(.4)

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("Section_1/Icons/py_logo.png"))

window = Window()

window.show()

sys.exit(app.exec())