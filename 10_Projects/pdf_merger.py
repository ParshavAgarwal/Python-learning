#pip install PyPDF2

import PyPDF2

#define paths of the PDF files to be merged
pdf1_path = r"C:\Users\Manoj Agarwal\OneDrive\Documents\Foundation Exam Form.pdf"
pdf2_path = r"C:\Users\Manoj Agarwal\OneDrive\Documents\Secondary School Examination (Class X) 2022.pdf"
pdfs = [pdf1_path, pdf2_path]

# Creating a PDF merger object
merger = PyPDF2.PdfMerger()

# Loop through each PDF and append it to the merger
for file in pdfs:
    with open(file, "rb") as pdfFile:  # Auto-closes the file
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
    
# Write the merged PDF to a new file
merger.write("Merged.pdf")
merger.close()

# Confirmation message
print(f"PDFs Merged Successfully!")
