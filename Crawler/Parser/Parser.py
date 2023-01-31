import Constants as const

from Element   import Element
from ReadHtml  import ReadHtml
from Attribute import Attribute





def is_html_element(read: ReadHtml) -> bool:

    char: chr = read.get_next_char()

    read.go_to_previous_char()

    if char.isalnum() or char == const.IGNORE:
        read.go_to_previous_char()
        return True

    return False





def is_close_element(read: ReadHtml) -> bool:
    
    char: chr = read.get_next_char()

    read.go_to_previous_char()

    if char == const.FORWARD_SLASH:
        read.skip_until_match(const.CLOSE_TAG)
        return True

    
    return False





def ignore(read: ReadHtml) -> None:

    read.skip_until_match(const.CLOSE_TAG)





def read_attribute_name(read: ReadHtml) -> str:

    name: str = ''

    while True:

        char: chr = read.get_next_char()

        if char == None:
            break

        if char == const.EQUEL_SIGN:
            break
    
        name += char


    return name





def read_attribute_values(read: ReadHtml) -> list[str]:
    
    value = ''
    values = []

    read.get_next_char()

    while True:

        char: chr = read.get_next_char()
        
        if char == None:
            break

        if char == const.DOUBLE_QUOTE:
            if value:
                values.append(value)
            break

        if char == const.WHITE_SPACE:
            values.append(value)
            value = ''
        else:
            value += char
           

    return values





def read_attribute(read: ReadHtml) -> Attribute:
    
    name: str = read_attribute_name(read)
    values: list[str] = read_attribute_values(read)
    
    return Attribute(name, values)





def read_element_attributes(read: ReadHtml) -> list[Attribute]:

    attributes: list[Attribute] = []

    while True:

        char: chr = read.get_next_char()

        if char == None:
            break
        
        if char == const.CLOSE_TAG:
            read.go_to_previous_char()
            break

        if char.isalnum():
            read.go_to_previous_char()
            attribute = read_attribute(read)
            attributes.append( attribute )
    
    
    return attributes





def read_element_name_and_attributes(read: ReadHtml) -> object:
    
    name = ''
    attributes = []
    
    while True:

        char: chr = read.get_next_char()

        if char == const.IGNORE:
            ignore(read)
            break

        if char == const.WHITE_SPACE:
            attributes = read_element_attributes(read)
            break
    
        if char == const.CLOSE_TAG:
            read.go_to_previous_char()
            break

        if char == None:
            break
        
        
        if char.isalnum():
            name += char


    return { 'name': name, 'attributes': attributes }





def read_content(read: ReadHtml, element: Element) -> str:

    term: str = ''
    content: str = ''

    while True:

        char: chr = read.get_next_char()

        if char == None:
            break

        if char == const.OPEN_TAG:
            if is_close_element(read):
                break

            if is_html_element(read):
                elem = read_element(read)
                element.add_element(elem)
                continue

        if char == const.WHITE_SPACE or char == const.END_LINE:
            if term:
                content += term + const.WHITE_SPACE
                term = ''
        else:
            term += char

    return content or term





def read_element(read: ReadHtml) -> Element:

    result: object = ''
    content: str = ''

    element = Element()

    while True:

        char = read.get_next_char()
        
        match char:

            case const.OPEN_TAG:
                result = read_element_name_and_attributes(read)
                continue

            case const.CLOSE_TAG:
                content = read_content(read, element)
                break

            case None:
                break


    if result.get('name'): 
        element.set_name(result.get('name'))

    if result.get('attributes'): 
        element.set_attributes(result.get('attributes'))

    if content: 
        element.set_content(content)

    
    return element
            



element: Element = None

try:
    data = open('/home/mz/Matan/WebCrawler/Crawler/Parser/text.html')

    read = ReadHtml( data.read() )

    element = read_element( read )

    element.print()

except ValueError:
    print('error')

