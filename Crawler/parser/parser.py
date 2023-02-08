from parser.utils import constants as const
from parser.utils import tags_without_close

from parser.element import Element
from parser.read_html import ReadHtml
from parser.attribute import Attribute


class Parser:



    def is_html_element(self) -> bool:

        char: chr = self.read.get_next_char()

        self.read.go_to_previous_char()

        if char.isalnum() or char == const.IGNORE:
            self.read.go_to_previous_char()
            return True

        return False





    def is_has_closing_element(self, element_name: str) -> bool:

        return tags_without_close.is_has_close(element_name)





    def is_end_of_element(self) -> bool:

        char: chr = self.read.get_next_char()

        self.read.go_to_previous_char()

        if char == const.FORWARD_SLASH:
            self.read.skip_until_match(const.CLOSE_TAG)
            return True


        return False





    def ignore(self) -> None:

        self.read.skip_until_match(const.CLOSE_TAG)





    def read_attribute_name(self) -> str:

        name: str = ''

        while True:

            char: chr = self.read.get_next_char()

            if char == None:
                break

            if char == const.EQUEL_SIGN:
                break
            
            name += char


        return name





    def read_attribute_values(self) -> list[str]:

        value = ''
        values = []

        self.read.get_next_char()

        while True:

            char: chr = self.read.get_next_char()

            if char == None:
                break

            if char == const.DOUBLE_QUOTE or char == const.SINGLE_QUOTE:
                if value:
                    values.append(value)
                break

            if char == const.WHITE_SPACE:
                values.append(value)
                value = ''
            else:
                value += char


        return values





    def read_attribute(self) -> Attribute:

        name: str = self.read_attribute_name()
        values: list[str] = self.read_attribute_values()

        return Attribute(name, values)





    def read_element_attributes(self) -> list[Attribute]:

        attributes: list[Attribute] = []

        while True:

            char: chr = self.read.get_next_char()

            if char == None:
                break
            
            if char == const.CLOSE_TAG:
                self.read.go_to_previous_char()
                break

            if char.isalnum():
                self.read.go_to_previous_char()
                attribute = self.read_attribute()
                attributes.append(attribute)


        return attributes





    def read_element_name_and_attributes(self) -> object:

        name = ''
        attributes = []

        while True:

            char: chr = self.read.get_next_char()

            if char == const.IGNORE:
                self.ignore()
                break

            if char == const.WHITE_SPACE:
                attributes = self.read_element_attributes()
                break
            
            if char == const.CLOSE_TAG:
                self.read.go_to_previous_char()
                break

            if char == None:
                break
            
            
            if char.isalnum():
                name += char


        return { 'name': name, 'attributes': attributes }





    def read_content(self, element: Element) -> str:

        term: str = ''
        content: str = ''

        while True:

            char: chr = self.read.get_next_char()

            if char == None:
                break

            if char == const.OPEN_TAG:
                if self.is_end_of_element():
                    break

                if self.is_html_element():
                    elem = self.read_element()
                    element.add_element(elem)
                    continue

            if char == const.WHITE_SPACE or char == const.END_LINE:
                if term:
                    content += term + const.WHITE_SPACE 
                    term = ''
            else:
                if char != const.TAB:
                    term += char

        content += term

        return content or term





    def read_element(self) -> Element:

        result: object = ''
        content: str = ''

        element = Element()

        while True:

            char = self.read.get_next_char()


            if char == const.OPEN_TAG:
                result = self.read_element_name_and_attributes()
                continue

            if char == const.CLOSE_TAG:
                if(self.is_has_closing_element(result.get('name'))):
                    content = self.read_content(element)
                break

            if char == None:
                break


        element.set_content(content)
        element.set_name(result.get('name'))
        element.set_attributes(result.get('attributes'))

        return element





    def parse(self, html_data) -> Element:

        self.read = ReadHtml( html_data )
        element: Element = self.read_element()

        return element



