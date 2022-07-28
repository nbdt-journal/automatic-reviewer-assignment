import re
import urllib.request


def get_search_url(db, base_url):
    query = "computational+AND+(neuroscience+OR+neuro+OR+brain+OR+imaging+OR+deep+OR+learning+OR+machine)"
    search_eutil = "esearch.fcgi?"
    search_term = "&term=" + query
    search_usehistory = "&usehistory=y"
    search_rettype = "&rettype=json"
    search_url = (
        base_url + search_eutil + db + search_term + search_usehistory + search_rettype
    )
    return search_url


def get_search_data(db, base_url):
    search_url = get_search_url(db, base_url)
    f = urllib.request.urlopen(search_url)
    search_data = f.read().decode("utf-8")
    return search_data


def get_web_env(db, base_url):
    search_data = get_search_data(db, base_url)
    web_env = re.findall("<WebEnv>(\S+)<\/WebEnv>", search_data)[0]
    return web_env


def get_query_key(db, base_url):
    search_data = get_search_data(db, base_url)
    query_key = re.findall("<QueryKey>(\d+?)</QueryKey>", search_data)[0]
    return query_key

def get_num_matching_queries(db, base_url):
    search_data = get_search_data(db, base_url)
    num_matching_queries = int(re.findall("<Count>(\d+?)</Count>", search_data)[0])
    return num_matching_queries


def get_fetch_url(
    db,
    base_url,
    fetch_retstart,
    fetch_retmax,
    fetch_retmode="&retmode=xml",
    fetch_rettype="&rettype=xml",
):
    fetch_eutil = "efetch.fcgi?"
    fetch_querykey = "&query_key=" + get_query_key(db, base_url)
    fetch_webenv = "&WebEnv=" + get_web_env(db, base_url)

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
    return fetch_url
