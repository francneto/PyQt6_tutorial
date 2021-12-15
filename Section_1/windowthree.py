from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)

window = QDialog() #Dont have maximize button feature

# window.statusBar().showMessage("Welcome to PyQt6 Course")## only belongs to MainWindow Application
# window.menuBar().addMenu("File")## only belongs to MainWindow Application

window.show()
sys.exit(app.exec())
