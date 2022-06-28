

import json, xmltodict
import urllib
import urllib.request
from urllib.request import urlopen
import pandas as pd

url = 'https://api.biorxiv.org/details/biorxiv/100'

response = urlopen(url)
  
#storing the JSON response 
#from url in data_json
data_json = json.loads(response.read())

#print the json response
#print(data_json['collection'])

alldata = []

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
            'Author': author,
            'Number on Paper': i+1,
            'Institution': institution
        }
        author_dict.append(a_dict)
        
    all_dict = {
        'Title': title,
        'Abstract': abstract,
        'doi': doi,
        'Authors': author_dict,
        'Source': 'bioarxiv',
    }
    alldata.append(all_dict)
    
print(json.dumps(alldata, indent = 4))