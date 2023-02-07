import os
from parser.parser import Parser
from parser.element import Element
from http_service import HttpService
from html_extractor import HtmlExtractor
from concurrent.futures import ThreadPoolExecutor



def _parse_html_page(html_page: str) -> Element:

    parser : Parser = Parser()
    return parser.parse(html_page)



def _get_html_page_data(url: str) -> Element:

    http : HttpService = HttpService('127.0.0.1', 8888)
    html_page : str = http.get(url)
    html_data: Element = _parse_html_page(html_page)
    
    return html_data




def get_all_recent_pastes_urls() -> list[str]:
    
    html: Element = _get_html_page_data('http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all')

    extractor: HtmlExtractor = HtmlExtractor()
    return extractor.get_all_recent_pastes_urls(html)




def parse_html_page(html_page: str) -> Element:

    parser : Parser = Parser()
    return parser.parse( html_page )




def get_all_recent_pastes(urls: list[str]) -> list[Element]:

    results: list[str] = []
    elements: list[Element] = []

    with ThreadPoolExecutor(os.cpu_count()) as executer1:
        results = executer1.map(_get_html_page_data, urls)

    with ThreadPoolExecutor(os.cpu_count()) as executer2:
        elements = executer2.map(_parse_html_page, results)

    return elements


def Crawler() -> None:

    http : HttpService = HttpService()

    return

