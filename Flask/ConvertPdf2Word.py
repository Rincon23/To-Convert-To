from pdf2docx import Converter #pip install pdf2docx
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

Arquivo_docx = 'exemplo.docx'

def converter_pdf_para_docx(Arquivo_pdf):
    converter = Converter(Arquivo_pdf)
    converter.convert(Arquivo_docx)
    converter.close()
    return redirect("/")


# Converter PDF para DOCX com opções avançadas
# converter = Converter(Arquivo_pdf, start=0, end=None, pages=None, keep_image=True, keep_table=True)
# converter.convert(Arquivo_docx)
# converter.close()