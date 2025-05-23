import pdfplumber
import os

def get_length_of_pdf(pdf_path: str) -> int:
    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)
    return num_pages

def extract_data_from_pdf(pdf_path: str, page: int = 0):
    with pdfplumber.open(pdf_path) as pdf:
        page_ = pdf.pages[page]
        texto = page_.extract_text()
    return texto

def extract_tables_from_pdf(pdf_path: str, page: int = 0):
    with pdfplumber.open(pdf_path) as pdf:
        page_ = pdf.pages[page]
        tables = page_.extract_tables()
    return tables

def extract_images_and_save(pdf_path: str, out_path: str, page: int = 0):
    os.makedirs(out_path, exist_ok=True)
    filename = os.path.basename(pdf_path)
    files = []
    with pdfplumber.open(pdf_path) as pdf:
        page_ = pdf.pages[page]
        images = page_.images
        ancho_pagina, alto_pagina = page_.width, page_.height
        for i, img in enumerate(images):
            x0, y0, x1, y1 = max(0, img['x0']), max(img['top'], 0), min(img['x1'], ancho_pagina), min(alto_pagina, img['bottom'])

            im = page_.within_bbox((x0,y0,x1,y1)).to_image()
            im_name = f"{out_path}/{filename.split('.')[0]}p{page}_{i}.png"
            im.save(im_name)
            files.append(im_name)
    return files

if __name__ == "__main__":
    pdf_path = "/tmp/a.pdf"
    extract_images_and_save(pdf_path, "./a",0)