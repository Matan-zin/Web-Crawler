from parser.parser import Parser
from parser.element import Element
from http_service import HttpService
from html_extractor import HtmlExtractor


def get_all_recent_pastes_urls() -> list[str]:
    
    parser : Parser = Parser()
    extractor : HtmlExtractor = HtmlExtractor()
    http : HttpService = HttpService('127.0.0.1', 8888)

    html_page : str = http.get('http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all')
    html: Element = parser.parse( html_page )

    return extractor.get_all_recent_pastes_urls(html)


def Crawler() -> None:

    http : HttpService = HttpService()

    return

urls: list[str] = get_all_recent_pastes_urls()

for url in urls:
    print(url)