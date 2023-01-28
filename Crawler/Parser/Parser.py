import Constants as const

from Element   import Element
from ReadHtml  import ReadHtml
from Attribute import Attribute

# -----------------------------------------------------------------------------------------------------------------

def validate_html_element(read: ReadHtml) -> bool:

    char: chr = read.get_next_char()

    read.go_to_previous_char()

    if char.isalnum():

        read.go_to_previous_char()

        return True

    return False


# -----------------------------------------------------------------------------------------------------------------


def validate_close_element(read: ReadHtml) -> bool:

    char: chr = read.get_next_char()

    read.go_to_previous_char()

    if char == const.FORWARD_SLASH:

        read.skip_until_match(const.CLOSE_TAG)

        return True
    
    return False


# -----------------------------------------------------------------------------------------------------------------


def ignore(read: ReadHtml) -> None:

    while True:

        char: chr = read.get_next_char()

        match char:

            case const.CLOSE_TAG:

                break


# -----------------------------------------------------------------------------------------------------------------


def read_attribute_name(read: ReadHtml) -> str:

    name: str = ''

    while True:

        char: chr = read.get_next_char()

        match char:

            case None:

                break


            case const.EQUEL_SIGN:

                break
    
        name += char


    return name


# -----------------------------------------------------------------------------------------------------------------


def read_attribute_values(read: ReadHtml) -> list[str]:
    
    read.get_next_char() # skip

    value = ''
    values = []

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



# -----------------------------------------------------------------------------------------------------------------



def read_attribute(read: ReadHtml) -> Attribute:
    
    name: str = read_attribute_name(read)

    values: list[str] = read_attribute_values(read)
    
    return Attribute(name, values)



# -----------------------------------------------------------------------------------------------------------------


def read_element_attributes(read: ReadHtml):

    attributes = []

    while True:

        char = read.get_next_char()


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



# -----------------------------------------------------------------------------------------------------------------



def read_element_name_and_attributes(read: ReadHtml):
    
    name = ''
    attributes = []
    
    while True:

        char = read.get_next_char()

        match char:

            case const.IGNORE:

                ignore(read)

                break

            
            case const.WHITE_SPACE:

                attributes = read_element_attributes(read)

                break
        
            
            case const.CLOSE_TAG:

                read.go_to_previous_char()

                break


            case None:

                break
        
        
        if char.isalnum():
            
            name += char


    return { 'name': name, 'attributes': attributes }



# -----------------------------------------------------------------------------------------------------------------


def read_contant(read: ReadHtml, element: Element) -> str:

    value = ''
    contant = ''

    while True:

        char = read.get_next_char()


        if char == None:

            break


        if char == const.OPEN_TAG:

            if validate_close_element(read):

                break
            

            if validate_html_element(read):

                elem = read_element(read)

                element.add_element(elem)

                continue



        if char == const.WHITE_SPACE or char == const.END_LINE:
            
            if value:

                contant += value + const.WHITE_SPACE

                value = ''
        else:

            value += char


    return contant or value or ''



# -----------------------------------------------------------------------------------------------------------------


def read_element(read: ReadHtml) -> Element:

    result = ''
    contant = ''

    element = Element()


    while True:

        char = read.get_next_char()
        
        match char:
            
            case const.CLOSE_TAG:
                
                contant = read_contant(read, element)
                
                break

            case const.OPEN_TAG:

                result = read_element_name_and_attributes(read)

            case None:

                break



    if result.get('name'): 
        
        element.set_name(result.get('name'))

    if result.get('attributes'): 
        
        element.add_attributes(result.get('attributes'))

    if contant: 
        
        element.add_contant(contant)

    
    return element
            

# -----------------------------------------------------------------------------------------------------------------


element: Element = None

try:
    data = open('/home/mz/Matan/WebCrawler/Crawler/Parser/test.html')

    read = ReadHtml( data.read() )

    element = read_element( read )

    element.print()

except ValueError:
    print('error')

