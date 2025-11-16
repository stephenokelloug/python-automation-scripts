import PyPDF2


def split_pdf(input_pdf, output_folder):
    # Open the PDF file
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

        # Iterate through each page
        for page_num in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])

            # Save each page as a new PDF file
            output_pdf = f"{output_folder}/page_{page_num + 1}.pdf"
            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)
            print(f"Page {page_num + 1} saved as {output_pdf}")


# Example usage
input_pdf = "pdfs/f896E86D59369880633A8.pdf"  # Path to your input PDF
output_folder = "output"  # Folder to store the individual pages
split_pdf(input_pdf, output_folder)
