import PyPDF2
import os
import re


def merge_pdfs(input_folder, output_pdf):
    # Get a sorted list of all PDF files in the folder using numeric sorting
    pdf_files = sorted(
        [f for f in os.listdir(input_folder) if f.endswith(".pdf")],
        key=lambda x: int(re.search(r'page_(\d+).pdf', x).group(1))  # Extract numeric page number
    )

    # Initialize a PdfWriter object
    writer = PyPDF2.PdfWriter()

    # Add each PDF file to the writer
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

    print(f"Merged PDF saved as {output_pdf}")


# Example usage
input_folder = "input"  # Folder containing the split PDFs
output_pdf = "check.pdf"  # Output merged PDF file
merge_pdfs(input_folder, output_pdf)
