import platform
import os
import subprocess
import tempfile
from typing import Dict

from xfdfgen import Xfdf

from wrapper_runtime_tests import *


if platform.system() == 'Windows':
    probable_pdftk_location = os.path.join(r"C:\Program Files (x86)\PDFtk Server\bin", "pdftk.exe")
    if os.path.isfile(probable_pdftk_location):
        pdftk_path = probable_pdftk_location


def fill_form_fields(input_pdf: str, form_field_dictionary: Dict[str, str], output_pdf: str, flatten: bool = False):
    """
    Takes an input pdf containing form fields, and fills them in from a python dictionary.

    Args:
        input_pdf (str): path to the input pdf
        form_field_dictionary (Dict[str, str]): a python dictionary with form field ids as keys,
                                                and fill in values as values
        output_pdf (str): path to the output pdf
        flatten: if set to true the output pdf won't be editable
    """
    fill_form_fields_sanity_checks(input_pdf, form_field_dictionary, output_pdf)

    xfdf = Xfdf(input_pdf, form_field_dictionary)
    temp_xfdf_path = f"this.xfdf"
    xfdf.write_xfdf(temp_xfdf_path)

    cmd = [pdftk_path, input_pdf, "fill_form", temp_xfdf_path, "output", output_pdf]

    if flatten:
        cmd.append("flatten")

    subprocess.run(cmd)


example_dict = {
    "first_name": "john",
    "last_name": "doe"
}

example_pdf = os.path.join(r"F:\Github_projects\pdfformfields\example\example_pdf.pdf")
output_pdf = os.path.join(r"F:\Github_projects\pdfformfields\example\output2.pdf")

fill_form_fields(example_pdf, example_dict, output_pdf)
