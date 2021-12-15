from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)

window = QDialog() #Dont have maximize button feature

window.show()
sys.exit(app.exec())
