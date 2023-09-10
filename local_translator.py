from PyDictionary import PyDictionary


class LocalTranslator:
    def __init__(self, target):
        self.dictionary = PyDictionary()
        self.target = target

    def translate(self, word):
        translated = self.dictionary.translate(word, self.target)
        return translated if not None else None

    def add_meaning(self, word):
        output = ""
        try:
            for key, value in self.dictionary.meaning(word).items():
                output += f"{key}: {value[0]} \n"
        except AttributeError as e:
            return None
        return output




