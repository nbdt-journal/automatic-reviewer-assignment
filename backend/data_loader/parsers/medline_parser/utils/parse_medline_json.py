import parsers.medline_parser.pubmed_parser.pubmed_parser.medline_parser as pp


def get_author_name(author_name: dict):
    """
    Function to get the author name from the author attribute in the manuscript dictionary

    Args
    ----
        ``author_name``: (dict)

    Returns
    ----
        ``author_name``: (str)
    """
    if "lastname" in author_name.keys():
        lastname = author_name["last_name"]
    else:
        lastname = ""
    
    if "forename" in author_name.keys():
        forename = author_name["forename"]
    else:
        forename = ""

    return forename + " " + lastname

def get_title(manuscript: dict):
    """
    Function to get the title from the manuscript dictionary

    Args
    ----
        ``manuscript``: (dict)

    Returns
    ----
        ``title``: (str)
    """
    if "title" in manuscript.keys():
        title = manuscript["title"]
    else:
        title = None
    return title

def get_abstract(manuscript: dict):
    """
    Function to get the abstract from the manuscript dictionary

    Args
    ----
        ``manuscript``: (dict)

    Returns
    ----
        ``abstract``: (str)
    """
    if "abstract" in manuscript.keys():
        abstract = manuscript["abstract"]
    else:
        abstract = None
    return abstract

def get_author_affiliation(author_name: dict):
    """
    Function to get the affiliation from the author attribute in the manuscript dictionary

    Args
    ----
        ``author_name``: (dict)

    Returns
    ----
        ``affiliation``: (str)
    """
    if "affiliation" in author_name.keys():
        affiliation = author_name["institution"]
    else:
        affiliation = ""
    return affiliation

def get_pmid(manuscript: dict):
    """
    Function to get the pmid from the manuscript dictionary

    Args
    ----
        ``manuscript``: (dict)

    Returns
    ----
        ``pmid``: (str)
    """
    if "pmid" in manuscript.keys():
        pmid = manuscript["pmid"]
    else:
        pmid = None
    return pmid

def get_authors(manuscript: dict):
    """
    Function to get the author list from the manuscript dictionary

    Args
    ----
        ``manuscript``: (dict)

    Returns
    ----
        ``author_list``: (list)
    """
    if "authors" in manuscript.keys() and len(manuscript.get("authors")) > 0:
        author_list = manuscript.get("authors")
        for author_index, author in enumerate(author_list):
            author_name = get_author_name(author)
            author_affiliation = get_author_affiliation(author)
            author["author"] = author_name
            author["affiliation"] = author_affiliation
            author["number_on_paper"] = author_index + 1
    else:
        author_list = None
    return author_list


def parse_medline_json(xml_path : str):
    """
    Parses the unprocessed XML response into the JSON format required by the recommendation system.

    Args
    ----
        ``xml_path``: (str) Path to the XML file retrieved after querying the eutility API.

    Returns
    ----
        ``json_path``: (str) Path to the JSON file containing the parsed XML response.

    """
    manuscripts = pp.parse_medline_xml(xml_path, author_list=True)
    parsed_manuscripts = []

    for index in range(len(manuscripts)):

        manuscript = manuscripts[index]
        title = get_title(manuscript)
        abstract = get_abstract(manuscript)
        pmid = get_pmid(manuscript)
        author_list = manuscript["authors"]
        source = "medline"
        single_manuscript_data = {
            "title": title,
            "authors": author_list,
            "abstract": abstract,
            "pmid": pmid,
            "source": source,
        }
        parsed_manuscripts.append(single_manuscript_data)

    return parsed_manuscripts
