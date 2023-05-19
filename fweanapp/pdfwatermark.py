from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

def pdf_watermark(self,pdf_file):


    watermark = 'media/watermark/watermark.pdf'
    merged = pdf_file

    with open(watermark, "rb") as watermark_file:
        input_pdf = PdfFileReader(pdf_file)
        watermark_pdf = PdfFileReader(watermark_file)
        watermark_page = watermark_pdf.getPage(0)
        output = PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            pdf_page = input_pdf.getPage(i)
            pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)

        # with open(merged, "wb") as merged_file:
        output.write(merged) 
        # print(merged)



    return merged