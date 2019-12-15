from io import StringIO
import json
import requests
import sys
import logging
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr,  laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        print("kek")
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

if __name__ == "__main__":
    path = "C:\\keks\\books\\Unity_v_deystvii.pdf"#sys.argv[1]
    file = "text_form_pdf.txt"#sys.argv[2]

    #logging.getLogger("pdfminer").propagate = False
    #logging.getLogger("pdfminer").setLevel(logging.ERROR)
    
    myFile = open(file,"w+",encoding='utf-8')
    myFile.write(convert_pdf_to_txt(path).strip())

