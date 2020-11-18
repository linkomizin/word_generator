import sys
from PyQt5 import QtCore, QtWidgets
from docxtpl import DocxTemplate
doc = DocxTemplate('templates/fuel.docx')

context = { 'date' : '','car_name': '',
	 'car_number':'', 'km_a': '', 'km_b': '',
	 'fuel': '45,67', 'km': '29'}
cars = {'К400ХН76': 'CHEVROLET NIVA',
        'А509КО76': 'Toyota RAV4',
        'В992РО76': 'UAZ Pickup'}

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.hbox = QtWidgets.QHBoxLayout()
        self.setLayout(self.hbox)

        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)
        self.hbox.addLayout(self.vbox)

        # блок выбора машины
        self.vbox_car = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.vbox_car)

        # блок ввода данных
        self.vbox_text = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.vbox_text)

        self.date_calendar = QtWidgets.QLabel('Дата:')
        self.vbox.addWidget(self.date_calendar)


        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setGeometry(QtCore.QRect(10, 10, 110, 24))
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.vbox.addWidget(self.dateEdit)
        self.dateEdit.dateChanged.connect(self.date_add)

        self.label = QtWidgets.QLabel()
        self.vbox.addWidget(self.label)


        self.pushButton = QtWidgets.QPushButton("Save .docx")
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 113, 32))
        self.vbox.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.write_template)

        self.car = QtWidgets.QLabel('TC: ')
        self.vbox_car.addWidget(self.car)

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

        self.label_km_a = QtWidgets.QLabel('Перед выездом, км')
        self.vbox_text.addWidget(self.label_km_a)

        self.kilomter_a = QtWidgets.QLineEdit()
        self.kilomter_a.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.kilomter_a.setMaxLength(6)
        self.vbox_text.addWidget(self.kilomter_a)
        self.kilomter_a.textEdited.connect(self.add_km_a)

        self.label_km_b = QtWidgets.QLabel('При заезде, км')
        self.vbox_text.addWidget(self.label_km_b)

        self.kilomter_b = QtWidgets.QLineEdit()
        self.kilomter_b.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.kilomter_b.setMaxLength(6)
        self.vbox_text.addWidget(self.kilomter_b)
        self.kilomter_b.textEdited.connect(self.add_km_b)

        self.hbox_fuel = QtWidgets.QHBoxLayout()
        self.vbox_fuel = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.hbox_fuel)
        self.hbox_fuel.addLayout(self.vbox_fuel)

        self.label_km_tdu = QtWidgets.QLabel('ТДУ, км')
        self.vbox_fuel.addWidget(self.label_km_tdu)

        self.kilomter_tdu = QtWidgets.QLineEdit()
        self.kilomter_tdu.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.kilomter_tdu.setMaxLength(6)
        self.vbox_fuel.addWidget(self.kilomter_tdu)
        self.kilomter_tdu.textEdited.connect(self.add_km_tdu)

        self.label_fuel = QtWidgets.QLabel('Литры')
        self.vbox_fuel.addWidget(self.label_fuel)

        self.litres = QtWidgets.QLineEdit()
        self.litres.setGeometry(QtCore.QRect(130, 10, 100, 20))
        self.litres.setMaxLength(6)
        self.vbox_fuel.addWidget(self.litres)
        self.litres.textEdited.connect(self.add_km_tdu)

        


    def add_km_a(self, km):
        context['km_a'] = km
    
    def add_km_b(self, km):
        context['km_b'] = km

    def add_km_tdu(self, km):
        context['km'] = km


    def date_add(self, a):
        date = a.toString('dd.MM.yyyy')
        self.label.setText(date)
        context['date'] = date

    def on_clicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.label.setText(radioButton.value)
            context['car_number'] = radioButton.value
            context['car_name'] = cars[radioButton.value]

    # def f_write(self):
    #     a = ('tmp/tmp.txt')
    #     with open(a, 'w') as f:
    #         f.write(str(val))

    def write_template(self):
        doc.render(context)
        doc.save("final.docx")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())