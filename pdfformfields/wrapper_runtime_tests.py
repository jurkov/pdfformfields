import os

from typing import Dict


def fill_form_fields_sanity_checks(input_pdf: str, form_field_dictionary: Dict[str, str], output_pdf: str):
    # if not os.path.isfile(input_pdf):
    #     raise OSError(f"{input_pdf} does not exist.")

    if not input_pdf.endswith(".pdf"):
        raise ValueError(f"{input_pdf} is not a pdf file.")

    if not isinstance(form_field_dictionary, dict):
        raise TypeError("form_field_dictionary must be a dictionary")

    if not output_pdf.endswith(".pdf"):
        raise ValueError(f"{output_pdf} is not a pdf file.")