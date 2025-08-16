from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 456)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #ffecd2, stop:1 #fcb69f\n"
"    );\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(300, 290, 113, 32))
        self.submitButton.setObjectName("submitButton")
        self.statusLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(260, 320, 201, 51))
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 5, 311, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(100, 10))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.attemptsEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.attemptsEdit.setObjectName("attemptsEdit")
        self.verticalLayout.addWidget(self.attemptsEdit)
        self.Scores = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.Scores.setObjectName("Scores")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.Scores)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 311, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.scoresLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.scoresLayout.setContentsMargins(0, 0, 0, 0)
        self.scoresLayout.setObjectName("scoresLayout")
        self.verticalLayout.addWidget(self.Scores)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submitButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "Student Name"))
        self.label_2.setText(_translate("MainWindow", "No of Attemps"))
        self.Scores.setTitle(_translate("MainWindow", "GroupBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
