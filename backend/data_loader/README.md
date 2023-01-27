# Data Loaders

A library for retrieving scientific data from arXiv, bioRxiv, and MEDLINE, and converting to a it format usable by the automatic reviewer recommendation algorithm.

# Usage
To run the script, simply run:


``` python3 main.py ```


To change the parameters of the function, you can simply change the values in `config.yaml`.The usage is self-described within the config file. If you wish to not use a certain data source for the parsing, set the `parse` value to `false` in the respective parser section.


