from pdf2docx import Converter

# Specify the path to your PDF file inside the 'pdfs' folder
pdf_file = 'pdfs/janet cv.pdf'

# Specify the path for the output DOCX file inside the 'output' folder
docx_file = 'output/janetcv.docx'

# Create a PDF to DOCX converter object
cv = Converter(pdf_file)

# Convert the PDF to DOCX
cv.convert(docx_file)

# Close the converter object
cv.close()

print("Conversion completed successfully!")
