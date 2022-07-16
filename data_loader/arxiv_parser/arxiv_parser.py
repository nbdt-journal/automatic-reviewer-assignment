from arxiv_parser.utils.arxiv_api_request import *

data_path = "../data/search_data"
dest_dict = []

def arxiv_parser(dest_dict: list, data_path: str, max_results: int, start: int):
    response = get_json_body(start, max_results, data_path)
    parse_response(response, dest_dict)
