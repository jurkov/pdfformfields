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

### Filling forms

```python
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
```

The dictionary containing the form fields has
* keys: Form field ids from the document
* values: The value you want to fill it with

To get an output with no editable form fields, set flattened to True.

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

