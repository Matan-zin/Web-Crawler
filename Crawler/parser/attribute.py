class Attribute:

    def __init__(self, name: str, values: list[str]) -> None:

        self.__name  = name
        self.__values = values



    def get_name(self) -> str:

        return self.__name



    def get_values(self) -> list[str]:

        return self.__values



    def __str__(self) -> None:

        return 'Name: {0}\n Values: {1}\n'.format(self.__name, self.__values)