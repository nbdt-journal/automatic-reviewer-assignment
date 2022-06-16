from Bio import Medline # pip3 install biopython
import pandas as pd
from tqdm import tqdm # pip install tqdm

# run in conda --. python parser.py 

alldata = []
with open('pubmed-neuroscien-set.txt', encoding='utf-8') as f:
    pmids = Medline.parse(f)
    for pmid in tqdm(pmids):
        try:
            pid = pmid['PMID']
        except:
            pid = ''
        try:
            title = pmid['TI']
        except:
            title = ''
        try:
            Abstract = pmid['AB']
        except:
            Abstract = ''
        try:
            date_published = pmid['DP']
        except:
            date_published = ''
        try:
            doi = pmid['LID']
        except:
            doi = ''
        try:
            author = pmid['FAU']
        except:
            author = ''
        try:
            author_department = pmid['AD']
        except:
            author_department = ''
        dic = {
            'PMID': pid,
            'Title': title,
            'Abstract':Abstract,
            'date_published': date_published,
            'doi': doi,
            'author': author,
            'author_department': author_department

        }
        alldata.append(dic)

df = pd.DataFrame(alldata)
df.to_csv('output.csv', index=False) # convert this to csv to json using online converter.

# Note if you create json without create the csv first the output is weird in the sense it outputs horizontally instead of vertically.
#df.to_json('output_json.json', index=False)
print('finished')