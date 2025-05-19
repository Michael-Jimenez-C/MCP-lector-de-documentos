import easyocr

def extract_text_from_image(image_path: str, lang: str = 'es') -> str:
    """
    Extrae texto de una imagen utilizando EasyOCR.
    :param image_path: Ruta de la imagen de entrada.
    """
    try:
        reader = easyocr.Reader([lang])
        result = reader.readtext(image_path)
        extracted_text = ' '.join([text[1] for text in result])
        return extracted_text
    except Exception as e:
        return str(e)