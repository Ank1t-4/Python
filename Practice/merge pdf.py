import pypdf

merger = pypdf.PdfWriter()
print(isinstance(merger, pypdf.PdfWriter))
print(merger)

no_of_pdf_to_merge = int(input("Enter the number of pdf files to merge: "))
pdf_files = []
for i in range(no_of_pdf_to_merge):
    pdf_files.append(input("Enter the path of the pdf file: "))

for pdf in pdf_files:#["E://MCA AI&CI and NP.pdf", "E://Network Programming Notes.pdf"]
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()