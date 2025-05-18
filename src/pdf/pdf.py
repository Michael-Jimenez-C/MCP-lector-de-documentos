import pdfplumber

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

if __name__ == "__main__":
    pdt_path = "../../a.pdf"
    print("npage",get_length_of_pdf(pdt_path))
    print("data",extract_data_from_pdf(pdt_path, (2,3)))
    print("tables",extract_tables_from_pdf(pdt_path, 0))