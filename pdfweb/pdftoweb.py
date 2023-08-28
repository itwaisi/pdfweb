import base64, os, typing
from io import BytesIO
from pathlib import Path
import mammoth
from PIL import Image
import pythoncom
import win32com.client
from .defaults import DEFAULTS


# CONVERT IMAGES TO JPG
def convert_image(image):
    
    with image.open() as image_bytes:
        filename = image_bytes.name.split('/')[-1]
        encoded_src = base64.b64encode(image_bytes.read()).decode('ascii')
        
        img_temp = Image.open(BytesIO(base64.b64decode(encoded_src)))
        img_size = img_temp.size
        img_temp = img_temp.save(f'./output_html/{filename}')
    
    img = {
        'src': filename
    }
    
    if img_size:
        img['width'] = str(img_size[0])
        img['height'] = str(img_size[1])
        img['alt'] = f'Test: {filename}'
    
    return img


# CONVERT LIST OF PDFS TO DOCX
def pdf_to_docx(output: typing.Union[str, os.PathLike], pdfs: typing.Union[typing.List[str], typing.List[os.PathLike]]) -> None:
    
    program = DEFAULTS["program"]
    
    # CREATE HTML FILE FROM EXTRACTED CONTENT
    if not os.path.exists(output):
        os.mkdir(output)
    
    # OPEN MICROSOFT WORD
    word = win32com.client.Dispatch('Word.Application', pythoncom.CoInitialize())
    word.visible = 0
    
    # SAVE PDF AS WORD DOCX
    for pdf in pdfs:
        temp_pdf = Path(pdf)
        temp_filename = temp_pdf.stem
        temp_docx = os.path.join(output, f'{temp_filename}.docx')

        wb = word.Documents.Open(os.path.abspath(temp_pdf))
        wb.SaveAs(os.path.abspath(temp_docx), FileFormat=16)
        wb.Close()
        print(f'[{program}] :: DOCX File Created ::', temp_docx)
    
    # CLOSE WORD
    word.Quit()
    
    print(f'[{program}] :: DOCX File Creation Completed')
    
    return None


# CONVERT LIST OF DOCX TO HTML
def docx_to_html(output: typing.Union[str, os.PathLike], docx: typing.Union[typing.List[str], typing.List[os.PathLike]]) -> None:
    
    program = DEFAULTS["program"]
    
    # CREATE HTML FILE FROM EXTRACTED CONTENT
    if not os.path.exists(output):
        os.mkdir(output)
    
    # EXTRACT CONTENT FROM DOCUMENT
    for doc in docx:
        temp_docx = Path(doc)
        temp_filename = temp_docx.stem
        temp_html = os.path.join(output, f'{temp_filename}.html')
        
        # CONVERT CONTENT OF DOCX TO HTML STRING
        with open(temp_docx, 'rb') as docx_file:
            result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_image))
            html_text = result.value
        
        # WRITE HTML STRING TO HTML FILE
        with open(temp_html, 'w') as html_file:
            html_file.write(html_text)
            print(f'[{program}] :: HTML File Created ::', temp_html)
    
    print(f'[{program}] :: HTML File Creation Completed')
    
    return None
