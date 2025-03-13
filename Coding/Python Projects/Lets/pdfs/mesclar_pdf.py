import PyPDF2
import os

merger = PyPDF2.PdfFileMerger(strict=False)

lista_arquivos = os.listdir("pdfs_mesclar")
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"pdfs_mesclar/{arquivo}")

merger.write("PDF_Final.pdf")