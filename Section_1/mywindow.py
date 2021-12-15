from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()

# window.statusBar().showMessage("Welcome to PyQt6 Course") ##only belongs to QMainWindow

window.show()

sys.exit(app.exec())
