from bioarxiv_parser.bioarxiv_parser import bioarxiv_parser
from arxiv_parser.arxiv_parser import arxiv_parser
from medline_parser.eutility_automator import eutility_automator
import json
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

bioarxiv_batches = config["params"]["bioarxiv"]["batches"]
bioarxiv_paging = config["params"]["bioarxiv"]["paging"]
bioarxiv_parse = config["params"]["bioarxiv"]["parse"]
arxiv_start = config["params"]["arxiv"]["start"]
arxiv_max_results = config["params"]["arxiv"]["max_results"]
arxiv_parse = config["params"]["arxiv"]["parse"]
medline_parse = config["params"]["medline"]["parse"]
medline_start = config["params"]["medline"]["start"]
medline_max_results = config["params"]["medline"]["max_results"]

full_data = []
data_path='./data/search_data'

print('Parsing bioarxiv data...')

bioarxiv_parser(
    batches=bioarxiv_batches,
    alldata=full_data,
    paging=bioarxiv_paging
    )

print('Parsing arxiv data...')

arxiv_parser(
    dest_dict=full_data,
    data_path=data_path,
    max_results=arxiv_max_results,
    start=arxiv_start
    )


eutility_automator(
    all_abstracts=full_data,
    retmax=10,
    retstart=0,
    total_abstract_count=medline_max_results
    )

print(str(len(full_data)) + " Entries have been returned.")

with open('test.json', 'w') as f:
    json.dump(full_data, f)
