from PyPDF2 import PdfReader, PdfWriter
import sys

file_path = sys.argv[1]
file_pw = sys.argv[2]

reader = PdfReader(file_path)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt(file_pw)

with open(file_path, "wb") as f:
    writer.write(f)
