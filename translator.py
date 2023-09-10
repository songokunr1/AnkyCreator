from credentials import config
import requests
import sys

from local_translator import LocalTranslator


class OnlineTranslator:
    auth_key = config['deepl-api']['key']
    url = 'https://api-free.deepl.com/v2/translate'
    headers = {
        'Authorization': f'DeepL-Auth-Key {auth_key}',
        'Content-Type': 'application/json',
    }

    def __init__(self, src_language, target_language):
        self.src_language = src_language
        self.target_language = target_language

    def translate(self, text):
        data = {
            'text': [
                text
            ],
            "detected_source_language": self.src_language,
            'target_lang': self.target_language,  # Change target language to Polish
        }

        response = requests.post(self.url, headers=self.headers, json=data)
        if response.status_code == 200:
            translated_text = response.json()['translations'][0]['text']
            # Set the encoding of stdout to UTF-8
            sys.stdout.reconfigure(encoding='utf-8')
            return translated_text if translated_text != text else None
        else:
            print("Error:", response.status_code, response.text)
            return response.text if response.text != text else None


class Translator:
    def __init__(self):
        self.local_translator = LocalTranslator("PL")
        self.online_translator = OnlineTranslator('EN', 'PL')

    def translate(self, word):
        translated = self.local_translator.translate(word)
        if translated:
            return translated
        translated = self.online_translator.translate(word)
        if not translated:
            return
        meaning = self.local_translator.add_meaning(word)
        full_output = f"{translated} \n {meaning}"
        return full_output

    def collect(self, words):
        collection = {}
        for word in words:
            collection[word] = {'name': word,
                                'translation': self.translate(word),
                                'audio_name': word}

translator = Translator()
translator.translate('blee')

# word = 'support'
# word_translated = translator.translate(word)
# print(word_translated)
