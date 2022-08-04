from parsers.bioarxiv_parser.bioarxiv_parser import biorxiv_parser
from parsers.arxiv_parser.arxiv_parser import arxiv_parser
from parsers.medline_parser.eutility_automator import eutility_automator
import json
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)
destination_path = config["destination_path"]
bioarxiv_batches = config["params"]["bioarxiv"]["batches"]
bioarxiv_paging = config["params"]["bioarxiv"]["paging"]
bioarxiv_parse = config["params"]["bioarxiv"]["parse"]
arxiv_start = config["params"]["arxiv"]["start"]
arxiv_max_results = config["params"]["arxiv"]["max_results"]
arxiv_parse = config["params"]["arxiv"]["parse"]
medline_parse = config["params"]["medline"]["parse"]
medline_max_results = config["params"]["medline"]["max_results"]
medline_ret_start = config["params"]["medline"]["ret_start"]
intermediates_path = config["intermediates_path"]
data_path = "./data/search_parameters"
full_data = []

print("Parsing bioarxiv data...")

biorxiv_parser(num_batches=bioarxiv_batches, all_manuscripts=full_data, page_size=bioarxiv_paging)

print("Parsing arxiv data...")

print(str(len(full_data)) + " Entries have been returned.")
arxiv_parser(
    all_manuscripts=full_data,
    data_path=data_path,
    max_results=arxiv_max_results,
    start=arxiv_start,
)
print(str(len(full_data)) + " Entries have been returned.")
eutility_automator(
    intermediates_path=intermediates_path,
    all_abstracts=full_data,
    retstart=medline_ret_start,
    max_results=medline_max_results,
)

print(str(len(full_data)) + " Entries have been returned.")

with open(destination_path, "w") as f:
    json.dump(full_data, f)
