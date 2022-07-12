import urllib.request
from pprint import pprint
import feedparser
# import from search_query.py
from .search_query import *

def get_json_body(start, max_results, path):
    """
    Params: query: string for the final query, derived from generate_query function.
    Returns the body of the XML response from the arxiv API.
    """
    base_url = 'http://export.arxiv.org/api/query?'
    query = generate_search_query(start, max_results, path)
    # query = 'all:brain+ORall:neuro+ORall:neural'
    query = 'search_query=%s&start=%i&max_results=%i' % (query,
                                                     start,
                                                     max_results)
    # print(query)
    response = urllib.request.urlopen(base_url + query).read()
    feed = feedparser.parse(response)

    # convert_to_json(response)
    return feed
def parse_response(feed):
    """
    Params: response: string for the XML response from the arxiv API.
    Returns: feed: dict for the XML response from the arxiv API.
    """
    output_dict = []
    for i in range(len(feed.entries)):
        output_dict.append({})

        if "title" in feed.entries[i] and feed.entries[i]["title"] != "":
            output_dict[i]["title"] = feed.entries[i].title
        else:
            output_dict[i]["title"] = ""


        if "summary" in feed.entries[i] and feed.entries[i].summary != "":
                output_dict[i]["abstract"] = feed.entries[i].summary
        
        if feed.entries[i].authors and len(feed.entries[i].authors) > 0:
            output_dict[i]["authors"] = []
            for author_index in range(len(feed.entries[i].authors)):
                output_dict[i]["authors"].append({})
                output_dict[i]["authors"][author_index]["name"] = feed.entries[i].authors[author_index].name
                output_dict[i]["authors"][author_index]["number_on_paper"] = author_index + 1
        else:
            continue

        if "arxiv_journal_ref" in feed.entries[i]:
            output_dict[i]["journal"] = feed.entries[i]["arxiv_journal_ref"]
        else:
            output_dict[i]["journal"] = ""


        if "arxiv_doi" in feed.entries[i] and feed.entries[i].arxiv_doi:
            output_dict[i]["doi"] = feed.entries[i].arxiv_doi
        else:
            continue
        
    pprint(output_dict)
    return output_dict
    
