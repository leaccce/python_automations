from pypdf import PdfWriter
from pypdf import PdfReader
l=["Power_Lab_3.pdf","Power_Lab_2.pdf",
"Power_Lab_1.pdf"]
l.sort()
m=PdfWriter()
for pdf in l:
    with open(pdf,"rb") as f:
        r=PdfReader(f)
        m.append(r)

with open("merged_pdf.pdf","wb") as f:
    m.write(f)