from docxtpl import DocxTemplate
doc = DocxTemplate("шаблон.docx")

context = { 'date' : "24.11.1989", 'car':'К400ХН76'}
doc.render(context)
doc.save("шаблон-final.docx")