import os, typing
from pathlib import Path
import mammoth
import pythoncom
import win32com.client
from .defaults import DEFAULTS


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
            result = mammoth.convert_to_html(docx_file)
            html_text = result.value

        # WRITE HTML STRING TO HTML FILE
        with open(temp_html, 'w') as html_file:
            html_file.write(html_text)
            print(f'[{program}] :: HTML File Created ::', temp_html)
    
    print(f'[{program}] :: HTML File Creation Completed')
    
    return None
    






































'''

import base64, shutil
from os import path, mkdir
from glob import glob
from datetime import datetime
from xml.sax.saxutils import escape, unescape
import win32com.client
import mammoth
from mammoth.cli import ImageWriter, _write_output


# CONVERT PDF TO DOCX

def pdf_to_docx(pdf, docx):
    word = win32com.client.Dispatch('Word.Application')
    word.visible = 0
    wb1 = word.Documents.Open(path.abspath(pdf))
    try:
        wb1.SaveAs(path.abspath(docx), FileFormat=16)
    except Exception as error:
        print('an execption has happened:', error)
    else:
        wb1.Close()
        word.Quit()

    print('[PDF TO HTML]: DOCX Created.')
    return False




# CONVERT DOCX TO HTML

def convert_image(image):

    print('[DEBUG] :: 01 ::', image, type(image))

    with image.open() as image_bytes:
        img_encoded = base64.b64encode(image_bytes.read()).decode('ascii')
        img_bytes = bytes(img_encoded, 'utf-8')

        dt = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        img_fn = f'image-{dt}.jpg'
        with open(path.join(FILE_DIR, img_fn), 'wb') as fh:
            fh.write(base64.decodebytes(img_bytes))

    return { 'src': img_fn }



def convert_image2(dir, image):
    print('DIR:', dir)
    print('IMAGE SRC:', mammoth.images.img_element(image))
    return image



def convert_image3(dir, image):
    print('DIR:', dir)
    print('IMAGE SRC:', mammoth.images.img_element(image))

    with image.open() as image_bytes:
        img_encoded = base64.b64encode(image_bytes.read()).decode('ascii')
        img_bytes = bytes(img_encoded, 'utf-8')

        dt = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        img_fn = f'image-{dt}.jpg'
        img_path = path.join(dir, img_fn)

        with open(img_path, 'wb') as fh:
            fh.write(base64.decodebytes(img_bytes))

    return { 'src': img_fn }



def replace_unicode(string, custom_unicode_map={}):
    
    unicode_map = { u'\u2010': '-' }

    unicode_map_merge = unicode_map.copy()
    unicode_map_merge.update(custom_unicode_map)

    esc_string = escape(string, unicode_map_merge)
    unesc_string = unescape(esc_string)
    
    print('[PDF TO HTML]: Unicode Characters Replaced.')
    
    return unesc_string
    


def docx_to_html(dir, docx, html):


    with open(docx, 'rb') as docx_file:

        # result = mammoth.convert_to_html(docx_file, convert_image=convert_image2(dir, mammoth.images.img_element(convert_image)))
        result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_image({'alt':'test alt'})))
        text = result.value
        new_text = replace_unicode(text)
        with open(html, 'w') as html_file:
            html_file.write(new_text)
            print('[PDF TO HTML]: HTML Created.')
    


# def docx_to_html2(dir, docx, html):


#     with open(docx, "rb") as docx_file:
#         convert_image = mammoth.images.img_element(ImageWriter(output_dir))
#         output_filename = "{0}.html".format(os.path.basename(filename).rpartition(".")[0])
#         output_path = os.path.join(output_dir, output_filename)
        
#         result = mammoth.convert(
#             docx_file,
#             convert_image=convert_image,
#             output_format='html',
#         )
#         _write_output(output_path, result.value)




# CONVERT PDF TO HTML

def get_files_by_type(dir, ext):
    return glob(path.join(dir, f'*.{ext}'))


def pdf_to_html(dir ):
    
    pdfs_to_convert = get_files_by_type(dir, 'pdf')

    for pdf in pdfs_to_convert:

        full_filename = path.basename(pdf)
        filename = path.splitext(full_filename)[0]
        new_folder = path.join(dir, filename)

        # print('dir:', dir)
        # print('pdf:', pdf)
        # print('full_filename:', full_filename)
        # print('filename:', filename)
        # print('new_folder', new_folder)

        if not path.exists(new_folder):
            
            # CREATE DIRECTORY BASED ON PDF NAME
            mkdir(new_folder)
            print(f'[PDF TO HTML]: Created PDF Folder, {new_folder}')

            # MOVE PDF TO NEW FOLDER
            shutil.move(pdf, path.join(dir, new_folder))
            print(f'[PDF TO HTML]: Moved {full_filename} to {new_folder}')

            # CONVERT PDF TO HTML
            pdf_to_docx(path.join(new_folder, full_filename), path.join(new_folder, f'{filename}.docx'))
            docx_to_html(dir, path.join(new_folder, f'{filename}.docx'), path.join(new_folder, f'{filename}.html'))

        else:
            print(f'[PDF TO HTML]: PDF has been parsed already: {new_folder}')
        
        
        











# file_pdf = 'bpd_test.pdf'
# file_docx = 'bpd_test.docx'
# file_html = 'bpd_test.html'


# pdf_to_docx(file_pdf, file_docx)
# docx_to_html(file_docx, file_html)









# from os import path



FILE_DIR = 'D:\Default\Documents\Business\projects\pdf-to-html'
file_ext = 'pdf'


test = get_files_by_type(FILE_DIR, file_ext)
print('TEST:', test)

print('GLOB:', glob('*.pdf'))


pdf_to_html(FILE_DIR)

'''
