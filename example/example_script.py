from pdfformfields import fill_form_fields

example_dict = {
    "first_name": "john",
    "last_name": "doe"
}

example_pdf = "example_input.pdf"
output = r"example_output.pdf"

fill_form_fields(example_pdf, example_dict, output)

# To get an that can't be edited, set flatten to True.
fill_form_fields(example_pdf, example_dict, output, flatten=True)
