from src.item import Item


class KeyBoard(Item):

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang != "EN" or "RU":
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        self.language = lang

    def change_lang(self):
        if self.__language == "EN":
            self.__language = 'RU'
        elif self.__language == "RU":
            self.__language = "EN"


