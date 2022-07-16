import json
from urllib.request import urlopen
from bioarxiv_parser.utils.parser import *

base_url = "https://api.biorxiv.org/details/biorxiv/"
date_range = "2015-01-01/2022-06-01/"

def bioarxiv_parser(batches: int, alldata: list, paging: int):
    for i in range(0, batches):
        cursor = str(paging * i + 1)
        url = base_url + date_range + cursor
        response = urlopen(url)
        data_json = json.loads(response.read())
        parse(data_json, alldata)
        print("Batch " + str(i) + " done.")
    print("Done parsing bioarxiv data.")

