import PyPDF2 as p2
import os

merger = p2.PdfMerger()

lista_arquivos = os.listdir("pdfs")
for arquivo in lista_arquivos:
    if ".pdf" in arquivo: # evita de afetar arquivos ocultos
        merger.append(f"pdfs/{arquivo}")

merger.write("PDF_final.pdf")
