from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(363, 583)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    background-color:white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.output_label.setFont(font)
        self.output_label.setAutoFillBackground(False)
        self.output_label.setStyleSheet("color: white;\n"
"")
        self.output_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_label.setLineWidth(2)
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(10, 110, 125, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(150, 110, 115, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.delButton.setFont(font)
        self.delButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.delButton.setObjectName("delButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: white\n"
"}")
        self.divideButton.setObjectName("divideButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.sevenButton.setObjectName("sevenButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyButton.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: white\n"
"}")
        self.multiplyButton.setObjectName("multiplyButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.fourButton.setObjectName("fourButton")
        self.substractButton = QtWidgets.QPushButton(self.centralwidget)
        self.substractButton.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.substractButton.setFont(font)
        self.substractButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: white\n"
"}")
        self.substractButton.setObjectName("substractButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.twoButton.setObjectName("twoButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.oneButton.setObjectName("oneButton")
        self.additionButton = QtWidgets.QPushButton(self.centralwidget)
        self.additionButton.setGeometry(QtCore.QRect(280, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.additionButton.setFont(font)
        self.additionButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: white\n"
"}")
        self.additionButton.setObjectName("additionButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget)
        self.decimalButton.setGeometry(QtCore.QRect(150, 470, 115, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(10, 470, 125, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(36, 36, 36)\n"
"}")
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(280, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: white\n"
"}")
        self.equalButton.setObjectName("equalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 363, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.delButton.setText(_translate("MainWindow", "DEL"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.substractButton.setText(_translate("MainWindow", "-"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.additionButton.setText(_translate("MainWindow", "+"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))
