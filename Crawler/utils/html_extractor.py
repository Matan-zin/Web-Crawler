from dateutil import parser 

from parser.element import Element
from parser.attribute import Attribute



class HtmlExtractor:


  def __normalize_author_name(self, name: str):

    match name:

        case 'Anonymous':
          return ''
        
        case 'Unknown':
          return ''

        case 'Guest':
          return ''

    return name
    


   
  def get_all_recent_pastes_urls(self, html: Element) -> list[str]:

        urls : list[str] = []

        elements: list[Element] = html.find_elements('a')

        for elem in elements:
          if(elem.get_content() == 'Show paste'):
            attr: Attribute = elem.find_attribute('href')
            if(attr != None):
              urls.append(attr.get_values()[0])

        return urls




  def get_paste_title(self, html: Element) -> str:

    elements: list[Element] = html.find_elements('h4')

    return elements[0].get_content()



  
  def get_paste_author_and_date(self, html: Element) -> list[str]:

    elements: list[Element] = html.find_element_with_attribute_value('div', 'class', 'col-sm-6')
    content: list[str] = elements[0].get_content().split(' ')
    
    author = self.__normalize_author_name(content[2])
    time = content[4] + ' ' + content[5] + ' ' + content[6] + ' ' + content[7]

    return [ author, parser.parse(time).timestamp() ]





  def get_paste_raw_content_url(self, html: Element) -> str:

    elements: list[Element] = html.find_elements('a')

    for elem in elements:
      if(elem.get_content() == 'Raw'):
        return elem.find_attribute('href').get_values()[0]
 