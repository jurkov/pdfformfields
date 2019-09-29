# pdfformfields

pdfformfields is a Python wrapper around 
[pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) 
that lets the user fill in forms 
from a Python dictionary.

### Prerequisites

You need to have [pdftk server](https://www.pdflabs.com/tools/pdftk-server/)
 on your computer installed.

### Installing

To install, simply run

``` bash
pip install pdfformfields
```

## Usage

```python
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
```

See complete [example](example/example_script.py).

### Bash error

The package did not manage to locate your pdftk command.

Make sure that pdftk server is installed on your system.
If it is, try setting the pdftk argument of fill_form_fields to ...

... on Linux:

```
fill_form_fields(..., pdftk_command="pdftk")
```

... on Windows:
```
pdftk_path = os.path.join("path_to_pdftk_server_folder", "bin", "pdftk.exe")
fill_form_fields(..., pdftk_command=pdftk_path)
```

## Built With

* [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) 

## Author

* **Nguyen Ba Long**

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [pypdftk](https://github.com/revolunet/pypdftk) Inspiration: another wrapper around pdftk that does not work under 
Windows and Python 3.7, which is why this package was created.

