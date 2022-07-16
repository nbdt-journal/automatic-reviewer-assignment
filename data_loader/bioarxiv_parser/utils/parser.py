def parse(data_json, alldata):
    for manuscript in data_json["collection"]:
        if manuscript["category"] != "neuroscience":
            continue 
        try:
            title = manuscript["title"]
        except:
            title = ""
        try:
            abstract = manuscript["abstract"]
        except:
            abstract = ""
        try:
            doi = manuscript["doi"]
        except:
            doi = ""
        try:
            authors = manuscript["authors"]
        except:
            authors = ""
        try:
            institution = manuscript["author_corresponding_institution"]
        except:
            institution = ""
        # slicing authors into a list
        author_list = authors.split(";")
        author_dict = []
        for i, author in enumerate(author_list):
            authors = {
                "author": author,
                "number_on_paper": i + 1,
                "affiliation": institution,
            }
            author_dict.append(authors)

        single_manuscript_data = {
            "title": title,
            "abstract": abstract,
            "doi": doi,
            "authors": author_dict,
            "source": "bioarxiv",
        }
        alldata.append(single_manuscript_data)

