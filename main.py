from docxtpl import DocxTemplate
doc = DocxTemplate('templates/fuel.docx')


def write_template():
	context = { 'date' : "24.11.1989",'car_name': 'CHEVROLET NIVA',
	 'car_number':'К400ХН76', 'km_a': '150000', 'km_b': '150324',
	 'fuel': '45,67', 'km': '29'}
	doc.render(context)
	doc.save("шаблон-final.docx")

write_template()