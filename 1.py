# # from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

# # pdf_file = "2.pdf"
# # watermark = "photo.pdf"
# # merged ="10.pdf"

# # with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
# #     input_pdf = PdfFileReader(input_file)
# #     watermark_pdf = PdfFileReader(watermark_file)
# #     watermark_page = watermark_pdf.getPage(0)

# #     output = PdfFileWriter()

# #     for i in range(input_pdf.getNumPages()):
# #         pdf_page = input_pdf.getPage(i)
# #         pdf_page.merge_page(watermark_page)
# #         output.addPage(pdf_page)

# #     with open(merged, "wb") as merged_file:
# #         output.write(merged_file)

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import BooleanObject, NumberObject

def add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path, transparency=0.5):
    with open(input_pdf_path, "rb") as input_file, open(watermark_pdf_path, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]

        # Set transparency level for watermark
        watermark_page.compress_content_streams()  # Required before setting transparency
        watermark_page['/Group'] = {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': BooleanObject(True), '/K': BooleanObject(False)}
        watermark_page['/Group']['/CA'] = NumberObject(transparency)  # Set transparency level

        output = PdfWriter()

        for pdf_page in input_pdf.pages:
            # Create a new PageObject with transparency settings
            new_page = PdfWriter()
            new_page.add_page(pdf_page)
            new_page.add_page(watermark_page)

            output.add_page(new_page)

        with open(output_pdf_path, "wb") as output_file:
            output.write(output_file)

# Example usage
pdf_file = "2.pdf"
watermark = "photo.pdf"
merged = "output.pdf"

add_watermark(pdf_file, watermark, merged, transparency=0.5)
