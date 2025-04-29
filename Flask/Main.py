from flask import Flask, render_template, request
import webview
from ConvertPdf2Word import converter_pdf_para_docx

app = Flask(__name__)

windows = webview.create_window('BestMeals', app, width = 1900, height=900, resizable=True, confirm_close=False)

@app.route('/')
def OOMenu():
    return render_template("Menu.html")

@app.route('/ConvertPdf2Word', methods=['POST'])
def OOConvertPdf2Word():
    Arquivo_pdf = request.files['pdffile']
    caminho_arquivo = f"./Arquivos enviados/{Arquivo_pdf.filename}"  # Define o caminho para salvar o arquivo
    Arquivo_pdf.save(caminho_arquivo)  # Salva o arquivo no servidor
    return converter_pdf_para_docx(caminho_arquivo)  # Passa o caminho do arquivo salvo para o conversor
    

if __name__ == "__main__":
    #webview.start()
    app.run(debug=True) # Executa o Flask em modo debug para desenvolvimento    