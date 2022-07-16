import re
import urllib.request
from time import sleep
from medline_parser.utils.get_search_data import *
from medline_parser.utils.parse_medline_json import *
import os
all_abstracts = list()

def eutility_automator(all_abstracts: list,
    retmax: int, 
    retstart: int, 
    total_abstract_count:int = None
    ):
    """
    This function automates the process of getting the abstracts from eutility.
    """

    base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    db = 'db=pubmed'

    search_data = get_search_data(db, base_url)
    retmax = 20
    retstart = 0
    fetch_retmode = "&retmode=xml"
    fetch_rettype = "&rettype=xml"
    fetch_eutil = 'efetch.fcgi?'
    fetch_webenv = "&WebEnv=" + re.findall ("<WebEnv>(\S+)<\/WebEnv>", search_data)[0]
    fetch_querykey = "&query_key=" + re.findall("<QueryKey>(\d+?)</QueryKey>",search_data)[0]
    if total_abstract_count is None:
        total_abstract_count = int(re.findall("<Count>(\d+?)</Count>",search_data)[0])

    while retstart <= 100:
        fetch_retstart = "&retstart=" + str(retstart)
        fetch_retmax = "&retmax=" + str(retmax)
        fetch_url = base_url+fetch_eutil+db+fetch_querykey+fetch_webenv+fetch_retstart+fetch_retmax+fetch_retmode+fetch_rettype
        f = urllib.request.urlopen (fetch_url)
        fetch_data = f.read().decode('utf-8')
        with open("./data/intermediates/fetch_data.xml", "w") as f:
            f.write(fetch_data)
        abstracts = parse_medline_json("fetch_data.xml")
        if abstracts:
            all_abstracts.extend(abstracts)
        sleep(2)
        retstart = retstart + retmax
    
    # delete the fetch_data file
    os.remove("./data/intermediates/fetch_data.xml")
