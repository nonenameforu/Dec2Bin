from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget { background-color: rgb(26, 26, 40); }")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(19, 19, 19, 19)
        self.gridLayout.setSpacing(7)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setStyleSheet("QLineEdit { background-color: rgb(60, 82, 103); color: white; font-family: Inter; font-size: 30pt; font-weight: normal; border-radius: 25px; }")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 3)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setStyleSheet("QLineEdit { background-color: rgb(60, 82, 103); color: white; font-family; Inter; font-size: 30pt; font-weight: normal; border-radius: 25px; }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 0, 1, 3)

        buttons = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "Del", "<-"]
        button_style = "QPushButton { background-color: rgb(65, 60, 98); color: white; font-family: Inter; font-size: 30pt; font-weight: normal; border-radius: 25px; }"

        for i, button_text in enumerate(buttons):
            button = QtWidgets.QPushButton(button_text, self.centralwidget)
            button.setMinimumSize(70, 70)
            button.setStyleSheet(button_style)
            button.setObjectName(f"Button{button_text}")
            shortcut = QKeySequence(button_text)
            if button_text == "<-":
                shortcut = QKeySequence("Backspace")
            button.setShortcut(shortcut)
            button.clicked.connect(lambda _, text=button_text: self.button_clicked(text))
            self.gridLayout.addWidget(button, i // 3 + 3, i % 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

    def button_clicked(self, text):
        if text in ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]:
            self.append(text)
            num = int(self.lineEdit.text() or "0")
            self.lineEdit_2.setText(self.decimal_to_binary32(num))
        elif text == "Del":
            self.clear()
        elif text == "<-":
            self.delete()

    def append(self, text):
        self.lineEdit.insert(text)

    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def delete(self):
        self.lineEdit.backspace()
        if self.lineEdit.text() != "":
            num = int(self.lineEdit.text())
            self.lineEdit_2.setText(self.decimal_to_binary32(num))
        else:
            self.lineEdit_2.clear()

    def decimal_to_binary32(self, decimal):
        if decimal <= 4294967295:
            binary = bin(decimal)[2:]
            while len(binary) < 32:
                binary = "0" + binary
            return binary
        else:
            return "Число слишком большое"

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
