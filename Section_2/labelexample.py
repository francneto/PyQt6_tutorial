from PyQt6.QtGui import QIcon,QPixmap,QFont,QMovie
from PyQt6.QtWidgets import QApplication, QWidget,QLabel
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400,400,800,800)
        self.setWindowTitle("FADEC")
        '''
        label = QLabel("Python GUI Development", self)
        label.setText("New Label")
        label.move(100,100)
        label.setFont(QFont("Sanserif",25))
        label.setStyleSheet('color:red')
        #label.setText(str(12))
        label.setNum(123)
        label.clear()
        '''
        staticFigure = QLabel(self)
        figure = QPixmap("Section_2/Icons/py_logo.png")
        staticFigure.setPixmap(figure)
        
        '''
        animatedFigure = QLabel(self)
        movie = QMovie("Section_2/Icons/200.gif")
        animatedFigure.setMovie(movie)
        movie.start()
        '''

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("Section_2/Icons/py_logo.png"))
window = Window()

window.show()

sys.exit(app.exec())