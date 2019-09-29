import platform
import os
from typing import Dict

from xfdfgen import Xfdf


if platform.system() == 'Windows':
    probable_pdftk_location = os.path.join(r"C:\Program Files (x86)\PDFtk Server\bin", "pdftk.exe")
    if os.path.isfile(probable_pdftk_location):
        pdftk_path = probable_pdftk_location


def fill_form_fields(input_pdf: str, form_field_dictionary: Dict[str, str], output_pdf: str) -> None:
    """
    Takes an input pdf containing form fields, and fills them in from a python dictionary.

    Args:
        input_pdf (str): path to the input pdf
        form_field_dictionary (Dict[str, str]): a python dictionary with form field ids as keys,
                                                and fill in values as values
        output_pdf (str): path to the output pdf
    """
    if not os.path.isfile(input_pdf):
        raise OSError(f"{input_pdf} does not exist.")

    if not input_pdf.endswith(".pdf"):
        raise ValueError(f"{input_pdf} is not a pdf file.")

    if not isinstance(form_field_dictionary, dict):
        raise TypeError("form_field_dictionary must be a dictionary")

    if not output_pdf.endswith(".pdf"):
        raise ValueError(f"{output_pdf} is not a pdf file.")
