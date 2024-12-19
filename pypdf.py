import PyPDF2

with open('/Users/ramsaiteja/Downloads/PYTHON PROGRAMS/pythonpdf/dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page =reader.getPage(0)
    page.rotateClockwise(90)
    writer =PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('title.pdf','wb') as file2:
        writer.write(file2)
