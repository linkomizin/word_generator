import sys
from PyQt5 import QtCore, QtWidgets
from datetime import datetime

data_now = datetime.now().strftime('%Y, %m, %d')



class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.hbox = QtWidgets.QHBoxLayout()
        self.setLayout(self.hbox)
        self.vbox = QtWidgets.QVBoxLayout()

        self.hbox.addLayout(self.vbox)
        self.setLayout(self.vbox)

        self.vbox_car = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.vbox_car)

        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setGeometry(QtCore.QRect(10, 10, 110, 24))
        # self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 11, 21), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.vbox.addWidget(self.dateEdit)

        self.pushButton = QtWidgets.QPushButton("Save .docx")
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 113, 32))
        self.vbox.addWidget(self.pushButton)

        self.radioButton1 = QtWidgets.QRadioButton('400')
        self.radioButton1.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.vbox_car.addWidget(self.radioButton1)

        self.radioButton2 = QtWidgets.QRadioButton('509')
        self.radioButton2.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.vbox_car.addWidget(self.radioButton2)

        self.radioButton3 = QtWidgets.QRadioButton('992')
        self.radioButton3.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.vbox_car.addWidget(self.radioButton3)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())