from PyPDF2 import PdfWriter
merger = PdfWriter()

pdf_files = input("Enter the full paths of the PDF files to merge, separated by commas: ").split(',')

for pdf in pdf_files:
    pdf = pdf.strip()
    merger.append(pdf)
output_filename = input("Enter the full path of the output merged PDF file: ").strip()
merger.write(output_filename)

merger.close()

print(f"Merged PDF saved as {output_filename}")
