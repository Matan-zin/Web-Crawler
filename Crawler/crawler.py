import os

from model.paste import Paste
from parser.parser import Parser
from crawler_dal import CrawlerDal
from parser.element import Element
from utils.http_service import HttpService
from utils.html_extractor import HtmlExtractor
from concurrent.futures import ThreadPoolExecutor



def _parse_html_page(html_page: str) -> Element:

    parser : Parser = Parser()
    return parser.parse(html_page)





def http_get(url) -> str:

    http : HttpService = HttpService('127.0.0.1', 8888)

    return http.get(url)





def _get_html_page_data(url: str) -> Element:

    html_page : str = http_get(url)
    html_data: Element = _parse_html_page(html_page)
    
    return html_data




def get_all_recent_pastes_urls() -> list[str]:
    
    html: Element = _get_html_page_data('http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all')

    extractor: HtmlExtractor = HtmlExtractor()
    return extractor.get_all_recent_pastes_urls(html)





def get_all_recent_pastes_pages(urls: list[str]) -> list[Element]:

    elements: list[Element] = []

    with ThreadPoolExecutor(os.cpu_count()) as executer1:
        elements = executer1.map(_get_html_page_data, urls)


    return elements





def get_paste_raw_content(url: str) -> str:
    content : str = ''
    raw : str = http_get(url)

    for word in raw.split():
        content += (word + ' ')
    
    return content




def get_paste(element: Element) -> Paste:

    paste : Paste = Paste()
    extractor : HtmlExtractor = HtmlExtractor()

    title : str = extractor.get_paste_title(element)
    author_and_date: list[str] = extractor.get_paste_author_and_date(element)
    raw_url : str = extractor.get_paste_raw_content_url(element)
    content: str = get_paste_raw_content(raw_url)

    paste.set_title(title)
    paste.set_author(author_and_date[0])
    paste.set_date(author_and_date[1])
    paste.set_content(content)

    return paste





def crawl() -> None:
    
    pastes: list[Paste] = []
    crawler_dal : CrawlerDal = CrawlerDal()

    urls: list[str] = get_all_recent_pastes_urls()
    elements: list[Element] = get_all_recent_pastes_pages(urls)

    with ThreadPoolExecutor(os.cpu_count()) as executer:
        pastes = executer.map(get_paste, elements)


    for paste in pastes:
        crawler_dal.save_paste(paste)





crawl()