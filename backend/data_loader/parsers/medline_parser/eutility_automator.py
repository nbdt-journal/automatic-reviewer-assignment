import urllib.request
from time import sleep
from parsers.medline_parser.utils.get_search_data import *
from parsers.medline_parser.utils.parse_medline_json import *
import os
import os.path as op


def get_retmax(max_results: int):
    """
    Get the retmax from eutility. Max retmax possible is 100000. This is not being made available as a parameter.
    If ``max_results > 100000``, the ``retmax`` will be set to  ``min(100000, max_results - 100000)``.
    If ``max_results < 100000``, the ``retmax`` will be set to ``max_results``.

    Args
    ----
        ``max_results``: (int) Maximum number of results to return.

    Returns
    ----
        ``retmax``: (int) Maximum number of results to return.
    """

    if max_results < 100000:
        return max_results
    else:
        return min(100000, max_results - 100000)


def eutility_automator(
    all_abstracts: list,
    retstart: int,
    intermediates_path: str,
    max_results: int = None,
):
    """ 
    Automate the process of querying, and parsing the eutility API response based on user provided parameters.
    The process is as follows:

    1. Generate the search query.
    2. Query the eutility API.
    3. Parse the JSON response based on the required format.
    4. Append the parsed JSON response to the list of all manuscripts.
    5. Increment the ``retstart`` (cursor) parameter.
    6. Repeat steps 2-5 until the ``retstart`` is greater than the ``max_results``.

    Args
    ----
        ``all_abstracts``: (list) List containing the parsed JSON response.
        ``retstart``: (int) Starting point for the retstart parameter.
        ``intermediates_path``: (str) Path to the folder containing the search parameters.
        ``max_results``: (int) Maximum number of results to return.
    
    Returns
    ----
        Nothing is returned.
        Dictionaries of the below format are appended to the list, ``all_abstracts``:

    ```json
    {
        "title": "" ,
        "abstract": "",
        "authors":
        [{
            "name": "",
            "number_on_paper": 1
        }],
        "doi": "",
        "source": ""
    },
    ```
    
"""

    base_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    db = "db=pubmed"

    fetch_retmode = "&retmode=xml"
    fetch_rettype = "&rettype=xml"
    fetch_eutil = "efetch.fcgi?"
    fetch_webenv = "&WebEnv=" + get_web_env(db, base_url)
    fetch_querykey = "&query_key=" + get_query_key(db, base_url)
    num_matching_queries = get_num_matching_queries(db, base_url)

    if max_results is None:
        max_results = num_matching_queries

    if not os.path.exists(intermediates_path):
        os.makedirs(op.dirname(intermediates_path), exist_ok=True)

    retmax = get_retmax(max_results)

    while retstart <= max_results:
        fetch_retstart = "&retstart=" + str(retstart)
        fetch_retmax = "&retmax=" + str(retmax)
        fetch_url = (
            base_url
            + fetch_eutil
            + db
            + fetch_querykey
            + fetch_webenv
            + fetch_retstart
            + fetch_retmax
            + fetch_retmode
            + fetch_rettype
        )

        f = urllib.request.urlopen(fetch_url)
        fetch_data = f.read().decode("utf-8")

        with open(intermediates_path, "w") as file:
            file.write(fetch_data)
        abstracts = parse_medline_json(intermediates_path)
        if abstracts:      
            all_abstracts.extend(abstracts)
        sleep(2)
        retstart = retstart + retmax

    os.remove(intermediates_path)
