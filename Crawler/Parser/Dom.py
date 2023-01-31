from Element import Element

class Dom:
    
    def __init__(self) -> None:

        self.__elements = []

    
    def add(self, element: Element) -> None:

        self.__elements.append(element)

    
    def print( self ) -> None:

        for elem in self.__elements:
            elem.print()