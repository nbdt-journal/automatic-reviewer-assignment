import urllib.request
from pprint import pprint
import feedparser
# keywords dict
def generate_keywords_dict(path):
    """
    Params: keywords: list of strings for the keywords.
    Returns: keywords_dict: dict for the keywords.
    """
    search_dict = {
        "keywords": [],
        "journals": [],
        "filter_out": []
    }
    keywords_txt = open(f'{path}/keywords.txt', 'r')
    journals_txt = open(f'{path}/journals.txt', 'r')
    filter_out_txt = open(f'{path}/filter_out.txt', 'r')
    keywords = keywords_txt.read().splitlines()
    for line in keywords:
        line = line.replace(' ', '%20')
        if line:
            search_dict["keywords"].append(line)
    
    for line in journals_txt:
        line = line.strip()
        if line:
            search_dict["journals"].append(line)
    
    for line in filter_out_txt:
        line = line.strip()
        if line:
            search_dict["filter_out"].append(line)

    return search_dict

def generate_search_query(start, max_results, path):
    """
    Params: keywords: list of strings for the keywords.
    Returns: search_query: string for the search query.
    """
    search_dict = generate_keywords_dict(path)

    search_query = 'all:'

    flag = 0
    # print(search_dict["keywords"])
    for keyword in search_dict["keywords"]:
        search_query += keyword + '+OR'
        flag = 1
    if flag == 1:
        search_query = search_query[:-3]

    flag = 0
    search_query += '+ORjr:'
    for keyword in search_dict["journals"]:
        keyword = keyword.replace(' ', '%20')
        search_query  +=  keyword + '+OR'
        flag = 1
    if flag == 1:
        search_query = search_query[:-3]
    else:
        search_query = search_query[:-6]

    flag = 0
    search_query += 'ANDNOT%28'
    for keyword in search_dict["filter_out"]:
        search_query +=  keyword + '+OR'
        flag = 1
    if flag == 1:
        search_query = search_query[:-3] + '%29'
    else:
        search_query = search_query[:-9] + '%29'

    query = 'search_query=%s&start=%i&max_results=%i' % (search_query, start, max_results)
    return query
