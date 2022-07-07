

import json
from urllib.request import urlopen

base_url = 'https://api.biorxiv.org/details/biorxiv/'
date_range = '2018-01-01/2022-06-01/'
alldata = []

def helper (data_json):
    for x in data_json['collection']:
        if (x['category'] != 'neuroscience'):
            continue
        try:
            title = x['title']
        except:
            title = ''
        try:
            abstract = x['abstract']
        except: 
            abstract = ''
        try: 
            doi = x['doi']
        except:
            doi = ''
        try:
            authors = x['authors']
        except:
            authors = ''
        try:
            institution = x['author_corresponding_institution']
        except:
            institution = ''
        #slicing authors into a list
        author_list = authors.split(';')
        author_dict = []
        for i, author in enumerate(author_list):
            a_dict = {
                'author': author,
                'number on Paper': i+1,
                'institution': institution
            }
            author_dict.append(a_dict)
            
        all_dict = {
            'title': title,
            'abstract': abstract,
            'doi': doi,
            'authors': author_dict,
            'source': 'bioarxiv',
        }
        alldata.append(all_dict)
    

#print(json.dumps(alldata, indent = 4))
    
for i in range(0, 200):
    cursor = str(100*i+1)
    url = base_url + date_range + cursor
    response = urlopen(url)
  
#storing the JSON response 
#from url in data_json
    data_json = json.loads(response.read())
    helper(data_json)


print(len(alldata))
with open('bioarxiv_parsed.json', 'w') as f:
    json.dump(alldata, f)
    

