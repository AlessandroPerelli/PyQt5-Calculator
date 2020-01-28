from PyQt5 import QtCore, QtGui, QtWidgets
import operator
4  # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.answer_display = QtWidgets.QLCDNumber(self.centralwidget)
        self.answer_display.setGeometry(QtCore.QRect(0, 50, 390, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.answer_display.setFont(font)
        self.answer_display.setObjectName("answer_display")
        self.calculation = QtWidgets.QLabel(self.centralwidget)
        self.calculation.setGeometry(QtCore.QRect(280, 0, 105, 50))
        self.calculation.setObjectName("calculation")
        self.number_placeholder = QtWidgets.QLabel(self.centralwidget)
        self.number_placeholder.setGeometry(QtCore.QRect(280, 20, 105, 40))
        self.number_placeholder.setObjectName("numberplaceholder")
        self.percent = QtWidgets.QPushButton(self.centralwidget)
        self.percent.setGeometry(QtCore.QRect(0, 120, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percent.setFont(font)
        self.percent.setObjectName("percent")
        self.cancelall = QtWidgets.QPushButton(self.centralwidget)
        self.cancelall.setGeometry(QtCore.QRect(97, 120, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cancelall.setFont(font)
        self.cancelall.setObjectName("cancelall")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(194, 120, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(97, 198, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 198, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(291, 198, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(194, 198, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(97, 276, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 276, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(194, 276, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(291, 276, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 354, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(194, 354, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(291, 354, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(97, 354, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(97, 432, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.plusminus = QtWidgets.QPushButton(self.centralwidget)
        self.plusminus.setGeometry(QtCore.QRect(0, 432, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusminus.setFont(font)
        self.plusminus.setObjectName("plusminus")
        self.equals = QtWidgets.QPushButton(self.centralwidget)
        self.equals.setGeometry(QtCore.QRect(291, 432, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equals.setFont(font)
        self.equals.setObjectName("equals")
        self.decimal = QtWidgets.QPushButton(self.centralwidget)
        self.decimal.setGeometry(QtCore.QRect(194, 432, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.decimal.setFont(font)
        self.decimal.setObjectName("decimal")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(291, 120, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.divide.setFont(font)
        self.divide.setObjectName("divide")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 26))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.zero.clicked.connect(lambda: self.write_to_temp_num(0))
        self.one.clicked.connect(lambda: self.write_to_temp_num(1))
        self.two.clicked.connect(lambda: self.write_to_temp_num(2))
        self.three.clicked.connect(lambda: self.write_to_temp_num(3))
        self.four.clicked.connect(lambda: self.write_to_temp_num(4))
        self.five.clicked.connect(lambda: self.write_to_temp_num(5))
        self.six.clicked.connect(lambda: self.write_to_temp_num(6))
        self.seven.clicked.connect(lambda: self.write_to_temp_num(7))
        self.eight.clicked.connect(lambda: self.write_to_temp_num(8))
        self.nine.clicked.connect(lambda: self.write_to_temp_num(9))
        self.decimal.clicked.connect(lambda: self.write_to_temp_num("."))
        self.plus.clicked.connect(lambda: self.write_to_calc_label("+"))
        self.minus.clicked.connect(lambda: self.write_to_calc_label("-"))
        self.multiply.clicked.connect(lambda: self.write_to_calc_label("*"))
        self.divide.clicked.connect(lambda: self.write_to_calc_label("/"))
        self.percent.clicked.connect(lambda: self.percentage())
        self.plusminus.clicked.connect(lambda: self.change_sign())
        self.equals.clicked.connect(lambda: self.execute_command())
        self.cancel.clicked.connect(lambda: self.remove_one())
        self.cancelall.clicked.connect(lambda: self.remove_all())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculation.setText(_translate("MainWindow", "Calculation"))
        self.number_placeholder.setText(
            _translate("MainWindow", "numberplaceholder"))
        self.percent.setText(_translate("MainWindow", "%"))
        self.cancelall.setText(_translate("MainWindow", "CE"))
        self.cancel.setText(_translate("MainWindow", "C"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))
        self.six.setText(_translate("MainWindow", "6"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.one.setText(_translate("MainWindow", "1"))
        self.three.setText(_translate("MainWindow", "3"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.two.setText(_translate("MainWindow", "2"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.plusminus.setText(_translate("MainWindow", "+/-"))
        self.equals.setText(_translate("MainWindow", "="))
        self.decimal.setText(_translate("MainWindow", "."))
        self.divide.setText(_translate("MainWindow", "/"))
        self.menuCalculator.setTitle(_translate("MainWindow", "Calculator"))

    # puts number in temp_num label
    def write_to_temp_num(self, number):
        current_text = self.number_placeholder.text()
        if current_text == "numberplaceholder":
            self.number_placeholder.setText(str(number))
        else:
            self.number_placeholder.setText(current_text + str(number))

    # puts number in calc label
    def write_to_calc_label(self, number):
        global number_count_tracker
        current_text = self.calculation.text()
        if current_text == "Calculation":
            self.calculation.setText(
                self.number_placeholder.text() + str(number))
            calc_list.append(self.number_placeholder.text())
            calc_list.append(number)
            number_count_tracker += 1
            print(number_count_tracker)
            self.number_placeholder.setText("")
        else:
            self.calculation.setText(self.calculation.text(
            ) + self.number_placeholder.text() + str(number))
            calc_list.append(self.number_placeholder.text())
            calc_list.append(number)
            number_count_tracker += 1
            print(number_count_tracker)
            self.number_placeholder.setText("")

    # perform percentage function
    def percentage(self):
        current_value_of_answer = self.answer_display.value()
        percent_value = int(current_value_of_answer)/100
        self.answer_display.display(percent_value)

    def execute_command(self):
        global calc_list
        global answer
        global number_count_tracker
        self.calculation.setText(
            self.calculation.text() + self.number_placeholder.text())
        text_calc = self.calculation.text()
        calc_list.append(self.number_placeholder.text())
        print(text_calc)
        print(calc_list)

        # splits list into numbers and operators
        for i in range(len(calc_list)):
            if float(i) == 0 or float(i % 2) == 0:
                number_list.append(calc_list[i])
            else:
                operators_list.append(calc_list[i])
        print(number_list, operators_list)

        # executes the command
        try:
            for i in range(number_count_tracker):
                if i == 0:
                    answer += ops[operators_list[0]](
                        float(number_list[0]), float(number_list[1]))
                else:
                    answer = ops[operators_list[i]](
                        float(answer), float(number_list[i+1]))
        except:
            print("Error, invalid operation")
        self.number_placeholder.setText("")
        self.calculation.setText("")
        # adapts display based on answer size
        if len(str(answer)) > 9:
            self.answer_display.setDigitCount(18)
        else:
            self.answer_display.setDigitCount(9)
        self.answer_display.display(answer)

    def remove_all(self):
        # resets the calculator
        global number_count_tracker
        global answer
        self.calculation.setText("Calculation")
        self.number_placeholder.setText("numberplaceholder")
        self.answer_display.display(0)
        calc_list.clear()
        operators_list.clear()
        number_list.clear()
        number_count_tracker = 0
        answer = 0

    def remove_one(self):
        current_placeholder_text = self.number_placeholder.text()

        # seperates and removes latest entry
        try:
            broken_current_placeholder_text = [
                i for i in current_placeholder_text]
            print(current_placeholder_text)
            broken_current_placeholder_text.remove(
                broken_current_placeholder_text[len(broken_current_placeholder_text) - 1])
        except:
            pass
        print(broken_current_placeholder_text)

        # reconstructs and changes label
        reconstructed_placeholder_text = "".join(
            broken_current_placeholder_text)
        self.number_placeholder.setText(reconstructed_placeholder_text)

    # changes sign of the label

    def change_sign(self):
        current_placeholder_text = self.number_placeholder.text()
        if "-" in current_placeholder_text:
            removed_minus = current_placeholder_text.replace("-", "")
            self.number_placeholder.setText(removed_minus)
        else:
            current_placeholder_text = "-{}".format(current_placeholder_text)
            self.number_placeholder.setText(current_placeholder_text)


if __name__ == "__main__":
    # initialises global varibles and ops
    import sys
    global calc_list
    calc_list = []
    global number_list
    number_list = []
    global operators_list
    operators_list = []
    global number_count_tracker
    number_count_tracker = 0
    global answer
    answer = 0

    global ops
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
