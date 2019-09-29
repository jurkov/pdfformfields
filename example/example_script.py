"""
Demo for pdfformfields.
For more details, go to https://github.com/Balonger/pdfformfields
"""
from pdfformfields import fill_form_fields

example_dict = {
    "first_name": "john",
    "last_name": "doe"
}

example_input_pdf = "example_input.pdf"

example_output_pdf = r"example_output.pdf"
fill_form_fields(example_input_pdf, example_dict, example_output_pdf)

example_output_pdf_flattened = r"example_output_pdf_flattened.pdf"
fill_form_fields(example_input_pdf, example_dict, example_output_pdf_flattened, flatten=True)
