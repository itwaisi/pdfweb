import os
from pathlib import Path
from pdfweb.defaults import DEFAULTS
from pdfweb.pdftoweb import pdf_to_docx, docx_to_html


if __name__ == "__main__":

    program = DEFAULTS['program']

    output_docx = Path(r'D:\Default\Documents\Business\projects\pdfweb\output_docx')
    output_html = Path(r'D:\Default\Documents\Business\projects\pdfweb\output_html')
    
    pdfs = [
        r'D:\Default\Documents\Business\projects\pdfweb\.temp\bpd_test.pdf',
        r'D:\Default\Documents\Business\projects\pdfweb\.temp\unicode.pdf',
        r'D:\Default\Documents\Business\projects\pdfweb\.temp\121467_1.pdf',
        r'D:\Default\Documents\Business\projects\pdfweb\.temp\123930.pdf'
    ]
    
    pdf_to_docx(output_docx, pdfs)

    docs = []
    
    for file_path in os.listdir(output_docx):
        if Path(file_path).suffix == '.docx':
            docs.append(os.path.join(output_docx, file_path))
    
    docx_to_html(output_html, docs)