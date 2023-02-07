from parser.attribute import Attribute

class Element:

    def __init__(self):

        self.__name: str = ''
        self.__content: str = ''
        self.__elements: list[Element] = []
        self.__attributes: list[Attribute] = []



    def set_name(self, name: str) -> None:

        self.__name = name



    def get_name(self) -> str:

        return self.__name
        


    def set_content(self, content: str) -> None:

        self.__content = content


    
    def get_content(self) -> str:

        return self.__content



    def add_element(self, element) -> None:

        self.__elements.append(element)


    
    def add_attribute(self, attr: Attribute) -> None:

        self.__attributes.append(attr)



    def set_attributes(self, attributes: list[Attribute]) -> None:

        self.__attributes = attributes


    
    def find__attribute(self, name: str) -> Attribute:
        
        for attr in self.__attributes:
            if attr.get_name() == name:
                return attr



    def find_elements(self, name):
        result = []
        elements = []

        if(self.__name == name):
            elements.append(self)

        for elem in self.__elements:
            result += elem.find_elements(name)

        return elements + result



    def __str__(self):
        to_string : str = ''
        to_string += ('Element: ' + self.__name + '\n')
        to_string += ('Attributes:\n')
        for attr in self.__attributes:
            to_string += str(attr)
        to_string += ('content:\n')
        to_string += (self.__content + '\n')
        to_string += ('Elements:\n')
        to_string += ('{\n')
        for elem in self.__elements:
            to_string += (str(elem))
        to_string += ('}\n')

        return to_string