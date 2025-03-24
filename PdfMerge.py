from PyPDF2 import PdfMerger
import os
import pdfkit

# Get the path of the notebook directory
notebook_dir = os.path.dirname(os.path.abspath(__file__))
dir = input(">> ") 
target_path = os.path.join(notebook_dir, dir,"Sprawozdanie")

for file_name in os.listdir(target_path):
    if file_name.endswith('.html'):
        html_path = os.path.join(target_path, file_name) 
        pdf_path = os.path.join(target_path, file_name.removesuffix(".html") + ".pdf") 
        pdfkit.from_file(html_path,pdf_path)

# Create a new PDF file object
merged_pdf = PdfMerger()

# Loop through all PDF files in the notebook directory
pdf_files = sorted(
    [f for f in os.listdir(target_path) if f.endswith(".pdf")],
    key=lambda x: int("".join(filter(str.isdigit, x)))  # Extracts numbers for sorting
)
for file_name in pdf_files:
    if file_name.endswith('.pdf'):
        # Add the PDF file to the merger object
        merged_pdf.append(open(os.path.join(target_path, file_name), 'rb'))

# Save the merged PDF file
with open(dir+'/Sprawozdanie_1.pdf', 'wb') as output_file:
    merged_pdf.write(output_file)