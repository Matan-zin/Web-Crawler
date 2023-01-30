from Attribute import Attribute

class Element:

    def __init__(self):

        self.__name: str = ''
        self.__content: str = ''
        self.__elements: list[Element] = []
        self.__attributes: list[Attribute] = []




    def set_name(self, name: str) -> None:

        self.__name = name
        


    def add_content(self, content: str) -> None:

        self.__content = content



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
        print('content:')
        print(self.__content)
        print('Elements:')
        for elem in self.__elements:
            elem.print()