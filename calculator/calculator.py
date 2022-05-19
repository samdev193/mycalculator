from gui import *
import math

class CalcMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.clearButton.clicked.connect(lambda:self.press_it("C"))
        self.delButton.clicked.connect(lambda:self.remove_it())
        self.multiplyButton.clicked.connect(lambda:self.press_it("*"))
        self.substractButton.clicked.connect(lambda:self.press_it("-"))
        self.additionButton.clicked.connect(lambda:self.press_it("+"))
        self.decimalButton.clicked.connect(lambda:self.decimal())
        self.equalButton.clicked.connect(lambda:self.evaluate())
        self.divideButton.clicked.connect(lambda:self.press_it("/"))
        self.nineButton.clicked.connect(lambda:self.press_it("9"))
        self.eightButton.clicked.connect(lambda:self.press_it("8"))
        self.sevenButton.clicked.connect(lambda:self.press_it("7"))
        self.sixButton.clicked.connect(lambda:self.press_it("6"))
        self.fiveButton.clicked.connect(lambda:self.press_it("5"))
        self.fourButton.clicked.connect(lambda:self.press_it("4"))
        self.threeButton.clicked.connect(lambda:self.press_it("3"))
        self.twoButton.clicked.connect(lambda:self.press_it("2"))
        self.oneButton.clicked.connect(lambda:self.press_it("1"))
        self.zeroButton.clicked.connect(lambda:self.press_it("0"))

    # handles math
    def evaluate(self):
        screen = self.output_label.text()
        try:
            answer = eval(screen)
            # output
            self.output_label.setText(str(answer))
        except:
            self.output_label.setText("ERROR")

    # removes character
    def remove_it(self):
        # gets whats on the screen
        screen = self.output_label.text()
        # removes last item
        screen = screen[:-1]
        self.output_label.setText(f'{screen}')

    # adds decimal
    def decimal(self):
        operation = ["+", "-", "*", "/"]
        screen = self.output_label.text()
        screen1 = ""
        screen2 = ""
        for ele in operation:
            if ele in screen:
                screen1 = screen[:screen.index(ele)]
                screen2 = screen[screen.index(ele):]
        if screen1 != "" and screen2 != "":
            if "." not in screen1:
                self.output_label.setText(f'{screen}.')
            if "." not in screen2:
                self.output_label.setText(f'{screen}.')
        elif "." not in screen:
            self.output_label.setText(f'{screen}.')

    # generic pressed
    def press_it(self, pressed):
        if pressed == "C":
            self.output_label.setText("0")
        else:
            if self.output_label.text() == "0":
                self.output_label.setText("")
            self.output_label.setText(f'{self.output_label.text()}{pressed}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CalcMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

