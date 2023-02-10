def replace_list_char(
    list_of_strings: list, to_replace: str = " ", replacement: str = "%20"
):
    """
    Replace a substring in a list of strings with another substring.

    Example Usage
    ----
        Function call:
         ``replace_list_char(["a b c", "d e f"], " ", "%20")``

        Returns:
         ``["a%20b%20c", "d%20e%20f"]``

    Args
    ----
        ``list_of_strings``: (list)
        ``to_replace``: (str)
        ``replacement``: (str)

    Returns
    ----
        ``list_of_strings``: (list)
    """

    for index, item in enumerate(list_of_strings):
        item = item.strip()
        list_of_strings[index] = item.replace(to_replace, replacement)
    return list_of_strings


def generate_search_parameters(path):
    """
    Generate a dictionary of search parameters from files provided .
    Search parameters include the keywords to be searched, keywords to filter_out,
    and journals to search for.

    Args
    ----
        ``path``: (str) Path to the folder containing the search parameters.

    Returns
    ----
        ``search_parameters``: (dict) Dictionary of search parameters.

    """
    search_parameters = {"keywords": [], "journals": [], "filter_out": []}

    included_keywords = open(f"{path}/included_keywords.txt", "r")
    journals = open(f"{path}/journals.txt", "r")
    excluded_keywords = open(f"{path}/excluded_keywords.txt", "r")

    for line in included_keywords.read().splitlines():
        search_parameters["keywords"].append(line.strip())

    for line in journals:
        search_parameters["journals"].append(line.strip())

    for line in excluded_keywords:
        search_parameters["filter_out"].append(line.strip())

    return search_parameters


def generate_search_query(start, max_results, path):
    """
    Function to generate a search query from the search parameters using
    the boolean logic required by the arxiv API.

    Example Usage
    ----
        Function call:
            ``generate_search_query(0, 100, "./search_parameters")``

        Returns:
            ``search_query``: (str) Search query that will retrieve a maximum 100 entries starting
             from the 0th index.

    Args
    ----
        ``start``: (int) Starting index of the search.
        ``max_results``: (int) Maximum number of results to return.
        ``path``: (str) Path to the folder containing the search parameters.

    Returns
    ----
        ``search_query``: String containing the search query.
    """
    search_parameters = generate_search_parameters(path)
    search_query = "all:"

    replace_list_char(search_parameters["journals"])
    replace_list_char(search_parameters["filter_out"])
    replace_list_char(search_parameters["keywords"])

    search_query += "+OR".join(search_parameters["keywords"])

    search_query += "+ORjr:"
    search_query += "+OR".join(search_parameters["journals"])

    search_query += "+ANDNOT%28"
    search_query += "+OR".join(search_parameters["filter_out"])
    search_query += "%29"

    query = "search_query=%s&start=%i&max_results=%i" % (
        search_query,
        start,
        max_results,
    )
    return query
