from PyPDF2 import PdfMerger
import os
import pdfkit

# Get the path of the notebook directory
notebook_dir = os.path.dirname(os.path.abspath(__file__))
dir = input() 
target_path = os.path.join(notebook_dir, dir)

# Create a new PDF file object
merged_pdf = PdfMerger()

for file_name in os.listdir(target_path):
    if file_name.endswith('.html'):
        html_path = os.path.join(target_path, file_name) 
        pdf_path = os.path.join(target_path,"Sprawozdanie", file_name.removesuffix(".html") + ".pdf") 
        pdfkit.from_file(html_path,pdf_path)

target_path = os.path.join(notebook_dir, dir, "Sprawozdanie")
# Loop through all PDF files in the notebook directory
for file_name in os.listdir(target_path):
    if file_name.endswith('.pdf'):
        # Add the PDF file to the merger object
        merged_pdf.append(open(os.path.join(target_path, file_name), 'rb'))

# Save the merged PDF file
with open('Lab1/Sprawozdanie/Sprawozdanie_1.pdf', 'wb') as output_file:
    merged_pdf.write(output_file)