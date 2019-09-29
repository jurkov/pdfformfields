""" pdfformfields

Python wrapper around pdftk to fill in pdf form fields.
See https://github.com/Balonger/pdfformfields

"""

import platform
import subprocess
from typing import Dict

from xfdfgen import Xfdf

from wrapper_runtime_tests import *


def get_pdftk_path():
    """
    Tries to infer the bash command for pdftk.

    Returns: Bash command for pdftk

    """
    # TODO add mac support
    # TODO test on linux

    if platform.system() == 'Windows':
        probable_pdftk_location = os.path.join(r"C:\Program Files (x86)\PDFtk Server\bin\pdftk.exe")
        if os.path.isfile(probable_pdftk_location):
            return probable_pdftk_location

    if platform.system() == 'Linux':
        probable_pdftk_location = '/usr/bin/pdftk'
        if os.path.isfile(probable_pdftk_location):
            return probable_pdftk_location

    return "pdftk"


def fill_form_fields(input_pdf: str, form_field_dictionary: Dict[str, str], output_pdf: str, flatten: bool = False,
                     pdftk_command: str = None):
    """
    Takes an input pdf containing form fields, and fills them in from a python dictionary.

    Args:
        input_pdf (str): path to the input pdf
        form_field_dictionary (Dict[str, str]): a python dictionary with form field ids as keys,
                                                and fill in values as values
        output_pdf (str): path to the output pdf
        flatten (Optional: bool): if set to true the output pdf won't be editable
        pdftk_command (Optional: str): if the function can't find the pdftk executable, you can set it manually here.
    """
    # Try to infer the location of pdftk
    if pdftk_command is None:
        pdftk_command = get_pdftk_path()

    # Sanity checks
    fill_form_fields_sanity_checks(input_pdf, form_field_dictionary, output_pdf, pdftk_command)

    # Create an xfdf file from the form_field directory and write it to a temporary file
    xfdf = Xfdf(input_pdf, form_field_dictionary)
    filename_of_input_pdf = os.path.basename(input_pdf)
    temp_xfdf_path = f"{filename_of_input_pdf}.xfdf"
    xfdf.write_xfdf(temp_xfdf_path)

    # Bash command to fill in the input_pdf using pdftk
    cmd = [pdftk_command, input_pdf, "fill_form", temp_xfdf_path, "output", output_pdf]
    if flatten:
        cmd.append("flatten")

    try:
        subprocess.run(cmd)
    except (FileNotFoundError, OSError):
        # Remove temporary xfdf file
        if os.path.exists(temp_xfdf_path):
            os.remove(temp_xfdf_path)

        # bash could not execute pdftk_command.
        err_msg = f"{pdftk_command} could not be executed in bash." \
                  f" See bash error at https://github.com/Balonger/pdfformfields"
        raise OSError(err_msg)

    # Remove temporary xfdf file
    if os.path.exists(temp_xfdf_path):
        os.remove(temp_xfdf_path)



