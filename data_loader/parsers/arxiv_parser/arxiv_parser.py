from parsers.arxiv_parser.utils.arxiv_api_request import *

def arxiv_parser(all_manuscripts: list, data_path: str, max_results: int, start: int):
    response = get_arxiv_response(
        start = start,
        max_results = max_results,
        path = data_path
    )
    parse_response(response, all_manuscripts)
