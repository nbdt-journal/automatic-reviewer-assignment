import urllib.request
import feedparser
from .search_query import *


def get_arxiv_response(start, max_results, path):
    """
    Send a request to the arxiv API server and retrieves the XML response.
    The XML response is then converted into a JSON format using feedparser.

    Args
    ----
        ``start``: (int) The starting index.
        ``max_results``: (int) Maximum number of results to return.
        ``path``: (str) Path to the folder containing the search parameters.

    Returns
    ----
        ``feed``: (dict) Dictionary containing the XML response from the arxiv API.
    """

    base_url = "http://export.arxiv.org/api/query?"
    query = generate_search_query(start, max_results, path)
    query = "search_query=%s&start=%i&max_results=%i" % (query, start, max_results)
    response = urllib.request.urlopen(base_url + query).read()
    feed = feedparser.parse(response)

    return feed


def parse_response(feed: dict, all_manuscripts: list):
    """
    Parses the unprocessed JSON response into the format required by the recommendation system.
    The format is as follows:

    Args
    ----
        ``feed``: (dict) Dictionary containing the unprocessed JSON response.
        ``all_manuscripts``: (list) List containing the parsed JSON response.

    Returns
    ----
        Nothing is returned. 
        Dictionaries of the below format are appended to the list, ``all_manuscripts``:

    ```json
    {
        "title": "" ,
        "abstract": "",
        "authors":
        [{
            "name": "",
            "number_on_paper": 1
        }],
        "journal": "",
        "doi": "",
        "source": ""
    },
    ```
    """
    # Feed contains a list of entries, each of which is a dictionary
    # which can provide us information about the article.
    for manuscript in feed["entries"]:
        parsed_manuscript_data = {}

        if "title" in manuscript.keys() and manuscript.get("title") != "":
            title = manuscript.get("title")
        else:
            title = None

        if "summary" in manuscript.keys() and manuscript.get("summary") != "":
            abstract = manuscript.get("summary")

        if manuscript.authors and len(manuscript.authors) > 0:
            authors = []
            for author_index in range(len(manuscript.authors)):
                authors.append({})
                authors[author_index]["name"] = (
                    manuscript.authors[author_index].get("name")
                )
                authors[author_index]["number_on_paper"] = (
                    author_index + 1
                )
        else:
            continue

        if "arxiv_journal_ref" in manuscript.keys():
            journal = manuscript.get("arxiv_journal_ref")
        else:
            journal = ""

        if "arxiv_doi" in manuscript.keys() and manuscript.arxiv_doi != "":
            doi = manuscript.arxiv_doi
        else:
            doi = None

        source = "arxiv"

        parsed_manuscript_data = {

            "title": title,
            "abstract": abstract,
            "authors": authors,
            "journal": journal,
            "doi": doi,
            "source": source,
        }

        all_manuscripts.append(parsed_manuscript_data)

    print(f"There are {len(all_manuscripts)} papers in the list.")
