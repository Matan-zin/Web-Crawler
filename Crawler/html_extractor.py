from parser.element import Element
from parser.attribute import Attribute


class HtmlExtractor:
    
   
  def get_all_recent_pastes_urls(self, html: Element) -> list[str]:

        urls : list[str] = []

        elements: list[Element] = html.find_elements('a')

        for elem in elements:
          if(elem.get_content() == 'Show paste'):
            attr: Attribute = elem.find__attribute('href')
            if(attr != None):
              urls.append(attr.get_values()[0])

        return urls