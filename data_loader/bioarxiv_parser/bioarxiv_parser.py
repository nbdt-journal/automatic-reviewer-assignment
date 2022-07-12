import json
from urllib.request import urlopen

base_url = "https://api.biorxiv.org/details/biorxiv/"
date_range = "2015-01-01/2022-06-01/"
alldata = []

# Get batches of publication data
# Each batch contains 100 manuscripts
def main(batches):
    for i in range(0, batches):
        cursor = str(100 * i + 1)
        url = base_url + date_range + cursor
        response = urlopen(url)

        # storing the JSON response from url in data_json
        data_json = json.loads(response.read())
        parse(data_json)
    # writing the result to json
    with open("test.json", "w") as f:
        json.dump(alldata, f)


def parse(data_json):
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
                "number on Paper": i + 1,
                "institution": institution,
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


main(5)
