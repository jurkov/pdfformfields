"""
Demo for pdfformfields.
For more details, go to https://github.com/Balonger/pdfformfields
"""
from pdfformfields import fill_form_fields, generate_dictionary


# Example pdf containing two fields with ids: first_name, last_name
example_input_pdf = "example_input.pdf"

# Use generate_dictionary() with verbose=True to understand the structure
# generate_dictionary(example_input_pdf, verbose=True)

# Use generate_dictionary() without verbose=True to generate a copiable code for the field dictionary onto the console
generate_dictionary(example_input_pdf)

""" The output should be:
rename_me = {
    "first_name": ,
    "last_name": ,
}
"""

# Paste code, rename dictionary, and fill in the values however you like
form_field_dictionary = {
    "first_name": "John",
    "last_name": "Doe",
}

# Output filled in dictionary with the fill_form_fields() function
example_output_pdf = r"example_output.pdf"
fill_form_fields(example_input_pdf, form_field_dictionary, example_output_pdf)

# If you don't want the output to be editable set flatten=True
example_output_pdf_flattened = r"example_output_pdf_flattened.pdf"
fill_form_fields(example_input_pdf, form_field_dictionary, example_output_pdf_flattened, flatten=True)


