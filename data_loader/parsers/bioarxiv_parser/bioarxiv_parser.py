import json
from urllib.request import urlopen


def parse_single_manuscript(manuscript: dict):
    """
    Function to parse a single manuscript manuscript within a batch.
    Entries without an abstract, or authors are returned as ``NoneType`` objects.

    Args:
        ``manuscript``: (dict)

    Returns:
        ``single_manuscript_data``: ``dict`` for a valid manuscript, and ``NoneType``
        if there is no abstract or authors.
    """

    if "category" in manuscript.keys():
        if manuscript["category"] != "neuroscience":
            return None

    if "title" in manuscript.keys():
        title = manuscript.get("title")
    else:
        title = None

    if "abstract" in manuscript.keys():
        abstract = manuscript.get("abstract")
    else:
        return None

    if "authors" in manuscript.keys():
        authors = manuscript.get("authors")
    else:
        return None

    if "doi" in manuscript.keys():
        doi = manuscript.get("doi")
    else:
        doi = None

    if "institution" in manuscript.keys():
        institution = manuscript.get("institution")
    else: 
        institution = None

    author_list = authors.split(";")
    author_dict = []

    for author_index, author in enumerate(author_list):
        authors = {
            "author": author,
            "number_on_paper": author_index + 1,
            "affiliation": institution,
        }
        author_dict.append(authors)

    single_manuscript_data = {
        "title": title,
        "abstract": abstract,
        "doi": doi,
        "authors": author_dict,
        "source": "biorxiv",
    }
    return single_manuscript_data


def parse_batch(batch_data: dict):
    """
    Function to parse a batch of manuscripts.
    The function calls the ``parse_single_manuscript`` function to parse each manuscript data.

    Args:
        ``batch_data``: (dict)

    Returns:
        ``parsed_batch_data``: (list)
    """

    parsed_batch_data = []
    for manuscript in batch_data["collection"]:
        single_manuscript_data = parse_single_manuscript(manuscript)
        if single_manuscript_data:
            parsed_batch_data.append(single_manuscript_data)
    return parsed_batch_data


def biorxiv_parser(
    num_batches: int,
    all_manuscripts: list,
    page_size: int,
    start_date: str = None,
    end_date: str = None,
):
    """
    Function to parse manuscripts from bioarxiv.
    The function calls the ``parse`` function to parse each batch of manuscripts.

    Args:
        ``num_batches``: (int)
        ``all_manuscripts``: (list)
        ``page_size``: (int)
        ``start_date``: (str)
        ``end_date``: (str)

    Returns:
        Nothing. The function modifies the ``all_manuscripts`` list.
    """

    base_url = "https://api.biorxiv.org/details/biorxiv/"

    if start_date is None or end_date is None:
        print("No starting date or end date specified. Using default values.")
        start_date = "2015-01-01"
        end_date = "2022-06-01"

    date_range = f"{start_date}/{end_date}/"

    print("Parsing data from Biorxiv...")

    for i in range(0, num_batches):
        cursor = str(page_size * i + 1)
        url = base_url + date_range + cursor
        response = urlopen(url)
        data_json = json.loads(response.read())
        batch_json = parse_batch(data_json)
        all_manuscripts.extend(batch_json)
        print(f"Batch {str(i)} of biorxiv data is parsed.")

    print("All biorxiv data is parsed and filtered successfully.")
