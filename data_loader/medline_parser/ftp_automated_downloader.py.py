import gzip
import os
import requests
from bs4 import BeautifulSoup
import re
    
def download_file(url):
    filename = url.split("/")[-1]
    create_zip_from_filename(url, filename)
    unzip_and_save(filename)
    os.remove(filename)
    print("""Do you want to delete the XML file too? (Just for testing purposes., 
    This file will automatically be deleted once the parsed XML file is created, and saved) (y/n)""")
    delete_xml = input()
    if delete_xml == "y":
        os.remove(filename[:-3])


def create_zip_from_filename(url, filename):
    # Create a filename from the url
    with open(filename, "wb") as f:
        r = requests.get(url)
        f.write(r.content)

def unzip_and_save(filename):
    f_in = gzip.open(filename, 'r')
    f_out = open(filename[:-3], 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()

url = "https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/"
urls = []

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, features="lxml")

for link in soup.find_all('a', href=re.compile('.*\.gz$')):
    urls.append(url + link.get('href'))

for url in urls:
    download_file(url)
    print("Downloaded: " + url)
    print("Unzipped: " + url[:-3])
    print("Deleted: " + url)
    print("\n")
