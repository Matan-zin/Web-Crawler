from Attribute import Attribute

class Element:

    def __init__(self):

        self.__name: str = ''

        self.__contant: str = ''

        self.__elements: list[Element] = []

        self.__attributes: list[Attribute] = []




    def set_name(self, name: str) -> None:

        self.__name = name
        


    def add_contant(self, contant: str) -> None:

        self.__contant = contant



    def add_element(self, element) -> None:

        self.__elements.append( element )


    
    def add_attribute(self, attr: Attribute) -> None:

        self.__attributes.append( attr )


       
    def add_attributes(self, attributes: list[Attribute]) -> None:

        self.__attributes = attributes



    def print(self):
        print('Element: ' + self.__name)
        print('Attributes:')
        for attr in self.__attributes:
            print(attr)
        print('contant:')
        print(self.__contant)
        print('Elements:')
        for elem in self.__elements:
            elem.print()