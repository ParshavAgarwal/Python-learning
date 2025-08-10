import PyPDF2

pdf1_path = r"C:\Users\Manoj Agarwal\OneDrive\Documents\Foundation Exam Form.pdf"
pdf2_path = r"C:\Users\Manoj Agarwal\OneDrive\Documents\Secondary School Examination (Class X) 2022.pdf"
pdfs = [pdf1_path, pdf2_path]

merger = PyPDF2.PdfMerger()

for file in pdfs:
    with open(file, "rb") as pdfFile:  # ✅ Auto-closes the file
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
    

merger.write("Merged.pdf")
merger.close()
print(f"✅ PDFs Merged Successfully!")