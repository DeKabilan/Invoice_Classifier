import PyPDF2
import re

def pdfextract(path):
    text = ''
    #------------Opening the PDF_File----------
    with open(path,'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

    #------------Reading/Writing-----------------
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    #------------Converting to List--------------
    array = re.split('; |, |\n|:| |%', text)

    #------------Filtering Null Elements-----------
    return list(filter(None,array))  

