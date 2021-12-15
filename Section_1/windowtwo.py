from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()

window.statusBar().showMessage("Welcome to PyQt6 Course")
window.menuBar().addMenu("File")## only belongs to MainWindow Application

window.show()

sys.exit(app.exec())
