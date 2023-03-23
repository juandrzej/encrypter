from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("xFile.pdf")

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("blabla")

with open("xFile.pdf", "wb") as f:
    writer.write(f)
