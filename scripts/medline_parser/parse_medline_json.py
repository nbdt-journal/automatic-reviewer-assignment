

import pubmed_parser.pubmed_parser.medline_parser as pp
from pprint import pprint
dict = pp.parse_medline_xml("../data/inputs/medline_small_input.xml", author_list=True)

dict_formatted = []

for item_index in range(len(dict)):
        dict_formatted.append({})
        dict_formatted[item_index]["title"] = dict[item_index]["title"]
        dict_formatted[item_index]["authors"] = []
        for author_index in range(len(dict[item_index]["authors"])):
            dict_formatted[item_index]["authors"].append({})
            dict_formatted[item_index]["authors"][author_index]["name"] = dict[item_index]["authors"][author_index]["forename"] + " " + dict[item_index]["authors"][author_index]["lastname"]
            dict_formatted[item_index]["authors"][author_index]["affiliation"] = dict[item_index]["authors"][author_index]["affiliation"] = dict[item_index]["authors"][author_index]["affiliation"]
        dict_formatted[item_index]["abstract"] = dict[item_index]["abstract"]
        dict_formatted[item_index]["journal"] = dict[item_index]["journal"]
        dict_formatted[item_index]["pmid"] = dict[item_index]["pmid"]


pprint(dict_formatted)