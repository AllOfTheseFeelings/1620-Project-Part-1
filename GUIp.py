# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.firstIn = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.firstIn.setGeometry(QtCore.QRect(40, 140, 381, 41))
        self.firstIn.setObjectName("firstIn")
        self.AddB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AddB.setGeometry(QtCore.QRect(60, 210, 151, 41))
        self.AddB.setObjectName("AddB")
        self.subtractB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.subtractB.setGeometry(QtCore.QRect(240, 210, 151, 41))
        self.subtractB.setObjectName("subtractB")
        self.multiplyB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.multiplyB.setGeometry(QtCore.QRect(60, 270, 151, 41))
        self.multiplyB.setObjectName("multiplyB")
        self.divideB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.divideB.setGeometry(QtCore.QRect(240, 270, 151, 41))
        self.divideB.setObjectName("divideB")
        self.chooseB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.chooseB.setGeometry(QtCore.QRect(60, 330, 151, 51))
        self.chooseB.setObjectName("chooseB")
        self.instructionlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.instructionlabel.setGeometry(QtCore.QRect(40, 20, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.instructionlabel.setFont(font)
        self.instructionlabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.instructionlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.instructionlabel.setWordWrap(True)
        self.instructionlabel.setObjectName("instructionlabel")
        self.textOut = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textOut.setGeometry(QtCore.QRect(60, 390, 331, 192))
        self.textOut.setObjectName("textOut")
        self.ClearB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ClearB.setGeometry(QtCore.QRect(240, 330, 151, 51))
        self.ClearB.setObjectName("ClearB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
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
        self.AddB.setText(_translate("MainWindow", "Add List"))
        self.subtractB.setText(_translate("MainWindow", "Subtract List"))
        self.multiplyB.setText(_translate("MainWindow", "Multiply List"))
        self.divideB.setText(_translate("MainWindow", "Divide List"))
        self.chooseB.setText(_translate("MainWindow", "Choose Random\n"
"Number From List"))
        self.instructionlabel.setText(_translate("MainWindow", "Enter a list of numbers with spaces as a seperator"))
        self.ClearB.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
