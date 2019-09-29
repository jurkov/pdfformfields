import os

from typing import Dict


def fill_form_fields_sanity_checks(input_pdf: str, form_field_dictionary: Dict[str, str], output_pdf: str):

    # input_pdf checks #################################################################################################
    if not os.path.isfile(input_pdf):
        raise OSError(f"{input_pdf} does not exist.")

    if not input_pdf.endswith(".pdf"):
        raise ValueError(f"{input_pdf} is not a pdf file.")

    # form_field_dictionary checks #####################################################################################
    if not isinstance(form_field_dictionary, dict):
        raise TypeError("form_field_dictionary must be a dictionary")

    # output_pdf checks ################################################################################################
    if not output_pdf.endswith(".pdf"):
        raise ValueError(f"{output_pdf} is not a pdf file.")


def get_form_field_ids_sanity_checks(input_pdf: str, output: str):
    # input_pdf checks #################################################################################################
    if not os.path.isfile(input_pdf):
        raise OSError(f"{input_pdf} does not exist.")

    if not input_pdf.endswith(".pdf"):
        raise ValueError(f"{input_pdf} is not a pdf file.")

    # output checks ####################################################################################################
    if not output.endswith(".txt"):
        raise ValueError("Output file must be a .txt file")


def bash_error_message(pdftk_command: str) -> str:
    return f"{pdftk_command} could not be executed in bash. See bash error at https://github.com/Balonger/pdfformfields"
