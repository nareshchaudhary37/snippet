from .zip_pdf import ZipResponseWithPDF
from .zip_csv import CSVResponse, ZipResponseWithCSV


# Zip with pdf

zip = ZipResponseWithPDF(filename="default")
filename = "pdf"
pdf_content = "PDF OBJECT"
zip.add_pdf_file(filename, pdf_content)

# this is httP ZIP RESPONSE
zip.get_response() # just RETURN THIS