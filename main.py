import os
from pathlib import Path
from pdfweb.defaults import DEFAULTS
from pdfweb.pdftoweb import pdf_to_docx, docx_to_html
from pdfweb.webtopdf import web_to_pdf


if __name__ == "__main__":

    program = DEFAULTS['program']
    
    # HTML TO PDF
    
    urls = [
        {
            'url': 'https://www.kscourts.org/Cases-Decisions/Decisions/Published/10th-Street-Medical-v-State',
            'slug': '',
            'title': '10th Street Medical v. State',
            'author': 'Kansas Judicial Branch'
        },
        {
            'url': 'https://www.kscourts.org/Cases-Decisions/Decisions/Published/143rd-Street-Investors-v-Board-of-Johnson-C',
            'slug': '102350',
            'title': '143rd Street Investors v. Board of Johnson County Commissioners',
            'author': 'Kansas Judicial Branch'
        } 
    ]

    css = '''
    * {
        font-family: "Times New Roman", Times, serif !important;
        font-size: 16px !important;
        line-height: 32px !important;
        margin: 0 0 0 0 !important;
        padding: 0 0 0 0 !important;
    }

    p {
        margin-bottom: 32px !important;
    }

    p[align="center"] {
        margin-bottom: 0px !important;
    }

    .aspNetHidden,
    #ctxM,
    .no-print,
    .top-container,
    .additional-info,
    .location-area,
    .footer {
        display: none !important;
    }
    '''

    web_to_pdf(urls=urls, css=css)


















    # PDF TO HTML


    # output_docx = Path(r'D:\Default\Documents\Business\projects\pdfweb\output_docx')
    # output_html = Path(r'D:\Default\Documents\Business\projects\pdfweb\output_html')
    
    # pdfs = [
    #     r'D:\Default\Documents\Business\projects\pdfweb\.temp\bpd_test.pdf',
    #     r'D:\Default\Documents\Business\projects\pdfweb\.temp\unicode.pdf',
    #     r'D:\Default\Documents\Business\projects\pdfweb\.temp\121467_1.pdf',
    #     r'D:\Default\Documents\Business\projects\pdfweb\.temp\123930.pdf'
    # ]
    
    # pdf_to_docx(output_docx, pdfs)

    # docs = []
    
    # for file_path in os.listdir(output_docx):
    #     if Path(file_path).suffix == '.docx':
    #         docs.append(os.path.join(output_docx, file_path))
    
    # docx_to_html(output_html, docs)
    