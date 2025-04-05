from PyPDF2 import PdfMerger
import os
import pdfkit
import nbformat
from nbconvert import HTMLExporter

# Get the path of the notebook directory
current_dir = os.path.dirname(os.path.abspath(__file__))
dir = input(">> ") 
target_path = os.path.join(current_dir, dir,"Sprawozdanie")
notebook_dir =  os.path.join(current_dir,dir)

# Generate .html files for all notebooks
for file_name in os.listdir(notebook_dir):
    if file_name.endswith('.ipynb'):
        output_filename = os.path.join( target_path,file_name.removesuffix('.ipynb')+".html" )
        notebook_path = os.path.join(notebook_dir, file_name)
        print(f"Reading notebook: {notebook_path}")

        if os.path.getsize(notebook_path) == 0:
            print(f"Skipping empty file: {file_name}")
            continue

        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook_node = nbformat.read(f, as_version=4)
            html_exporter = HTMLExporter()
            (body, resources) = html_exporter.from_notebook_node(notebook_node)

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(body)

# Generate pdf files for all .html files generated in previous step
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