from django.shortcuts import render,redirect
from . models import *
from docx import Document
from docx2pdf import convert

def BillPdfcreate(idb,dt,nm,ph,ml,dc,hs,gen,dtold,chi,ag,word_doc):
    docm= Document(word_doc)

    def find_replace(paragraph_keyword, draft_keyword, paragraph):
        if paragraph_keyword in paragraph.text:
            paragraph.text = paragraph.text.replace(paragraph_keyword, draft_keyword)

    for paragraph in docm.paragraphs:
        find_replace('ICR41227003543 ',idb,paragraph)
        find_replace('olddate',dtold,paragraph)
        find_replace('new date',dt,paragraph)
        find_replace('<CUSTOMER NAME>',nm,paragraph)
        find_replace('<customer email address>',ml,paragraph)
        find_replace('<DOCTOR NAME>',dc,paragraph)
        find_replace('<HOSPITAL NANE>',hs,paragraph)
        find_replace('<9876543210> ',ph,paragraph)
        find_replace('nil',chi,paragraph)
        find_replace('gene',gen,paragraph)
        find_replace('ag',ag,paragraph)


    fnm=idb+nm+'.docx'
    #pip install docx2pdf
    #from docx2pdf import convert

    x=docm.save('media\\'+fnm)

    return fnm


    