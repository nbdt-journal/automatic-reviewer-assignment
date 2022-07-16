import medline_parser.pubmed_parser.pubmed_parser.medline_parser as pp


def parse_medline_json(json_path):
    dict = pp.parse_medline_xml(json_path, author_list=True)
    dict_formatted = []

    for item_index in range(len(dict)):
        temp_dict = {}
        if dict[item_index]["title"] is not None:
            temp_dict["title"] = dict[item_index]["title"]
        if dict[item_index]["authors"] is not None:
            temp_dict["authors"] = []
        else:
            continue
        if len(dict[item_index]["authors"]) != 0:
            for author_index in range(len(dict[item_index]["authors"])):
                temp_dict["authors"].append({})
                temp_dict["authors"][author_index]["name"] = (
                    dict[item_index]["authors"][author_index]["forename"]
                    + " "
                    + dict[item_index]["authors"][author_index]["lastname"]
                )
                temp_dict["authors"][author_index]["affiliation"] = dict[item_index][
                    "authors"
                ][author_index]["affiliation"] = dict[item_index]["authors"][
                    author_index
                ][
                    "affiliation"
                ]
                temp_dict["authors"][author_index]["number_on_paper"] = author_index + 1
        else:
            continue
        if (
            dict[item_index]["abstract"] is not None
            and dict[item_index]["abstract"] != ""
        ):
            temp_dict["abstract"] = dict[item_index]["abstract"]
        else:
            continue
        if dict[item_index]["journal"] is not None:
            temp_dict["journal"] = dict[item_index]["journal"]
        if dict[item_index]["pmid"] is not None:
            temp_dict["pmid"] = dict[item_index]["pmid"]
        else:
            continue
        temp_dict["source"] = "medline"
        dict_formatted.append(temp_dict)

    return dict_formatted
