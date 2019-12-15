from io import StringIO
import json
import requests
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

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

myFile = open("1.txt","w",encoding='utf-8')
myFile.write(convert_pdf_to_txt("C:\\keks\\books\\JavaScript.pdf").strip())
thermsFile=open("therms1.txt","w+",encoding='utf-8')
textOfPDF=myFile.read()
listOfPDF=list(textOfPDF.strip().split('\n'))
newList=list(map(lambda x: x.split(' '), listOfPDF))
flatSet = set([item for sublist in newList for item in sublist])
newSet=set()
therms=set()
for word in flatSet:
    for x in word:
        if not x.isalpha():
            word=word.replace(x,"")
    newSet.add(word.lower())
for word in newSet:
    if requests.get('http://www.serelex.org/find/ru-patternsim-ruwac-wiki/'+ word).text.find('relations')!=-1:
        thermsFile.write(word+'\n')
        print('1')
#list1 = convert_pdf_to_txt('C:\\Users\\Sergesama\\source\\repos\\searcher\\searcher\\Documents\\1.pdf').strip().split('\n')
#new_list=list(map(lambda x: x.split(' '), list1))
#flat_list = [item for sublist in new_list for item in sublist]
#therms=list(filter(lambda x:requests.get('http://www.serelex.org/find/ru-patternsim-ruwac-wiki/'+ x).text.find('relations')!=-1,flat_list))
print (therms)
