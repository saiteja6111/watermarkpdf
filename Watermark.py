from PyPDF2 import PdfFileReader,PdfFileWriter

template = PdfFileReader(open('/Users/ramsaiteja/Downloads/PYTHON PROGRAMS/pythonpdf/super.pdf','rb'))

watermark = PdfFileReader(open('/Users/ramsaiteja/Downloads/PYTHON PROGRAMS/pythonpdf/wtr.pdf','rb'))

output = PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermark_pdf.pdf','wb') as file:
        output.write(file)
    
    



