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

        # блок выбора машины
        self.vbox_car = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.vbox_car)

        # блок вывода
        self.vbox_text = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.vbox_text)


        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setGeometry(QtCore.QRect(10, 10, 110, 24))
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.vbox.addWidget(self.dateEdit)

        self.pushButton = QtWidgets.QPushButton("Save .docx")
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 113, 32))
        self.vbox.addWidget(self.pushButton)

        self.radioButton = QtWidgets.QRadioButton('400')
        self.radioButton.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.vbox_car.addWidget(self.radioButton)
        self.radioButton.value = 'К400ХН76'
        self.radioButton.toggled.connect(self.on_clicked)

        self.radioButton = QtWidgets.QRadioButton('509')
        self.radioButton.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.vbox_car.addWidget(self.radioButton)
        self.radioButton.value = 'А509КО76'
        self.radioButton.toggled.connect(self.on_clicked)

        self.radioButton = QtWidgets.QRadioButton('992')
        self.radioButton.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.vbox_car.addWidget(self.radioButton)
        self.radioButton.value = 'В992РО76'
        self.radioButton.toggled.connect(self.on_clicked)

        self.label = QtWidgets.QLabel()
        self.vbox_text.addWidget(self.label)


    def on_clicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.label.setText(radioButton.value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())