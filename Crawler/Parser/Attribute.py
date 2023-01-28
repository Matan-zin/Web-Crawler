class Attribute:

    def __init__(self, name: str, values: list[str]) -> None:
        self.__name  = name
        self.__values = values


    def __str__(self) -> None:
        return ("Attribute:\nName: %s\nValues: %s"%(self.__name, self.__values))