from mcp.server.fastmcp import FastMCP
from .pdf.pdf import extract_data_from_pdf, get_length_of_pdf, extract_tables_from_pdf
import os


mcp = FastMCP("Extractor")

#PDF
@mcp.tool()
async def pdf_length(path:str) -> int:
    """
    Devuelve el número de páginas de un PDF.
    path debe ser la ruta absoluta al archivo PDF
    """
    return get_length_of_pdf(path)

@mcp.tool()
async def pdf_tables(path:str, page: int = 0) -> list:
    """
    Extrae tablas de un PDF.
    path debe ser la ruta absoluta al archivo PDF
    page: número de página a extraer, 0 por defecto
    """
    return extract_tables_from_pdf(path, page = page)

@mcp.tool()
async def pdf_read(path:str, page: int = 0) -> str:
    """
    Extrae texto de un PDF.
    path: debe ser la ruta absoluta al archivo PDF
    page: número de página a extraer, 0 por defecto
    """
    return extract_data_from_pdf(path, page = page)

#plain
@mcp.tool()
async def get_size(path: str) -> int:
    """
    Devuelve el tamaño de un fichero en bytes
    path: debe ser la ruta absoluta al archivo
    """
    try:
        if os.path.exists(path):
            return os.path.getsize(path)
        else:
            return -1
    except Exception as e:
        return -1
    
@mcp.tool()
async def read_file(path: str):
    """
    Extrae texto de un fichero
    path: debe ser la ruta absoluta al archivo
    """
    try:
        if os.path.exists(path):
            return open(path).read()
        else:
            return "El fichero no existe"
    except Exception as e:
        return "No fue posible abrir el fichero" + str(e)
    
@mcp.tool()
async def read_chunk(path: str, chunk: int=0, chunk_size: int = 1024) -> str:
    """
    Extrae texto de un fichero sobre un chunk
    """
    try:
        if os.path.exists(path):
            with open(path, 'r') as f:
                f.seek(chunk * chunk_size)
                return f.read(chunk_size)
        else:
            return "El fichero no existe"
    except Exception as e:
        return "No fue posible abrir el fichero" + str(e)

#EXCEL

#imagenes

#Extracción de texto

#Audio STT
