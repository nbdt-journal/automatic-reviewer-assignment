import importlib.resources as pkg_resources
from utils.arxiv_api_request import *
data_path='../data/search_data'

response = get_json_body(0, 10, data_path)
parse_response(response)
