import os, typing
from pathlib import Path
from playwright.sync_api import sync_playwright
from PyPDF2 import PdfReader, PdfWriter
from .defaults import DEFAULTS


def update_metadata(output:typing.Union[str, os.PathLike]=None, pdf:typing.Union[str, os.PathLike]=None, author:str=None, title:str=None) -> None:

    pdf = os.path.abspath(pdf)
    slug = Path(pdf).stem

    # SET PDF OUTPUT PATH
    if output is None:
        output = os.path.abspath(os.path.join(DEFAULTS['folders']['output_webtopdf_final'], f'{slug}.pdf'))

    # SET METADATA AUTHOR
    if author is None:
        author = 'itwaisi'

    # SET METADATA TITLE
    if title is None:
        title = 'itwaisi'

    reader = PdfReader(pdf)
    writer = PdfWriter()

    # ADD PAGES TO PDFWRITER
    for page in reader.pages:
        writer.add_page(page)

    # UPDATE METADATA
    writer.add_metadata({
        '/Title': title,
        '/Author': author,
        '/Producer': 'itwaisi PDFWeb'
    })

    # SAVE UPDATED PDF
    with open(output, 'wb') as f:
        writer.write(f)

    return None


def web_to_pdf(output:typing.Union[str, os.PathLike]=None, urls:list=None, css:str=None) -> None:
    
    program = DEFAULTS["program"]

    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            ignore_https_errors=True,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'
        )

        for url in urls:

            # SET PDF OUTPUT PATH
            if output is None:
                output = os.path.abspath(DEFAULTS['folders']['output_webtopdf_temp'])
            
            # SET PDF FILENAME
            filename = url['url'].split('/')[-1] if url['slug'] == '' else url['slug']

            # SET PDF PATH
            pdf_path = os.path.abspath(os.path.join(output, f'{filename}.pdf'))

            # CREATE PDF FROM WEB PAGE
            page = context.new_page()
            page.goto(
                url=url['url'],
                referer='https://www.google.com'
            )
            page.add_style_tag(content=css)
            page.wait_for_load_state( state='domcontentloaded' )
            page.pdf(path=pdf_path, format='Letter', margin={'top': '100', 'right': '100', 'bottom': '100', 'left': '100'})
            print(f'[{program}] :: PDF Created')

            # ADD METADATA TO PDF: TITLE AND AUTHOR
            update_metadata(pdf=pdf_path, author=url['author'], title=url['title'])
            print(f'[{program}] :: PDF Metadata Updated')
            
            # KEEP PAGE OPEN FOR SPECIFIED TIMEOUT
            page.wait_for_timeout( 0 )
        
        browser.close()
    
    return None
