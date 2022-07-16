import csv
import re
import urllib
from time import sleep

# computational[All Fields] AND ("neurosciences"[MeSH Terms] OR "neurosciences"[All Fields] OR "neuroscience"[All Fields])

# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=computational+neuroscience&usehistory=y&rettype=json

query = "computational+neuroscience"

# common settings between esearch and efetch
base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
db = 'db=pubmed'

# esearch settings
search_eutil = 'esearch.fcgi?'
search_term = '&term=' + query
search_usehistory = '&usehistory=y'
search_rettype = '&rettype=json'

# call the esearch command for the query and read the web result
search_url = base_url+search_eutil+db+search_term+search_usehistory+search_rettype
print("this is the esearch command:\n" + search_url + "\n")
f = urllib.request.urlopen (search_url)
search_data = f.read().decode('utf-8')

# extract the total abstract count
total_abstract_count = int(re.findall("<Count>(\d+?)</Count>",search_data)[0])

# efetch settings
fetch_eutil = 'efetch.fcgi?'
retmax = 20
retstart = 0
fetch_retmode = "&retmode=xml"
fetch_rettype = "&rettype=abstract"

# obtain webenv and querykey settings from the esearch results
fetch_webenv = "&WebEnv=" + re.findall ("<WebEnv>(\S+)<\/WebEnv>", search_data)[0]
fetch_querykey = "&query_key=" + re.findall("<QueryKey>(\d+?)</QueryKey>",search_data)[0]

# call efetch commands using a loop until all abstracts are obtained
run = True
all_abstracts = list()
loop_counter = 1

while run:
    print("this is efetch run number " + str(loop_counter))
    loop_counter += 1
    fetch_retstart = "&retstart=" + str(retstart)
    fetch_retmax = "&retmax=" + str(retmax)
    # create the efetch url
    fetch_url = base_url+fetch_eutil+db+fetch_querykey+fetch_webenv+fetch_retstart+fetch_retmax+fetch_retmode+fetch_rettype
    print(fetch_url)
    # open the efetch url
    f = urllib.request.urlopen (fetch_url)
    fetch_data = f.read().decode('utf-8')
    # split the data into individual abstracts
    abstracts = fetch_data.split("<")
    # append to the list all_abstracts
    all_abstracts = all_abstracts+abstracts
    print("a total of " + str(len(all_abstracts)) + " abstracts have been downloaded.\n")
    # wait 2 seconds so we don't get blocked
    sleep(2)
    # update retstart to download the next chunk of abstracts
    retstart = retstart + retmax
    if retstart > 4:
        run = False