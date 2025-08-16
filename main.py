import sys
from PyQt6.QtWidgets import QApplication
from logic import GradesApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GradesApp()
    w.show()
    sys.exit(app.exec())
