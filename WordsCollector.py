import nltk
from nltk.stem.lancaster import LancasterStemmer

from local_translator import LocalTranslator
from srtWordsCollector import read_srt_file

nltk.download('stopwords')


class WordsCollector:
    pass

def read_top_english_words(top_x):
    return set([line.strip() for line in open('10000-english.txt')][:top_x])

def read_names():
    return set([line.strip() for line in open('names_big.txt')])

def remove_duplicates(words):
    filtered_words = set(words.split())
    return ' '.join(filtered_words)
def removing_plural(words):
    st = LancasterStemmer()
    print(set(words.split()))
    words = [st.stem(word) for word in set(words.split())]
    print(words)

    words = set(words)
    return ' '.join(words)

def remove_numbers(words):
    filtered_words = words.split()
    words_without_numbers = []
    for word in filtered_words:
        try:
            str(int(word))
        except ValueError as e:
            words_without_numbers.append(word)
    return ' '.join(words_without_numbers)


def remove_shorter_words(words, length=4):
    filtered_words = words.split()
    filtered_words = [word for word in filtered_words if len(word) >= length]
    return ' '.join(filtered_words)

def remove_names(words):
        words = words.split()
        # print(words)
        names = read_names()
        filtered_words = [word for word in words if word not in names]
        return ' '.join(filtered_words)


class srtWordsCollector:
    def __init__(self, words):
        self.words = words


class strWordsCollector:
    def __init__(self, words):
        self.words = words

    @staticmethod
    def remove_stop_words(words):
        stopwords = nltk.corpus.stopwords.words('english')

        words = words.split()
        filtered_words = [word for word in words if word not in stopwords]
        return ' '.join(filtered_words)

    @staticmethod
    def remove_top1000_words(words):
        # print(words)
        words = words.split()
        # print(words)
        top1000 = read_top_english_words(4000)
        filtered_words = [word for word in words if word not in top1000]
        return ' '.join(filtered_words)
    @staticmethod
    def clean_up(words):
        chars = ",./:;?!♪_"
        for char in chars:
            words = words.replace(char, '')
        forbiden_text = "'s,'ll,'re,'d,'m,'ve".split(",")
        for text in forbiden_text:
            words = words.replace(text, '')

        words = words.replace("\"", '').lower()

        return words

    def get_words(self):
        self.words = self.clean_up(self.words)
        # self.words = removing_plural(self.words)
        self.words = remove_duplicates(self.words)
        self.words = remove_numbers(self.words)
        self.words = remove_shorter_words(self.words)
        self.words = remove_names(self.words)
        # print(self.words)
        self.words = self.remove_stop_words(self.words)
        self.words = self.remove_top1000_words(self.words)
        # print(self.words)
        return self.words


# WordsCollector(path, "")
words = """
Mr. Dursley was the director of a firm called Grunnings, which made
drills. He was a big, beefy man with hardly any neck, although he did
have a very large mustache. Mrs. Dursley was thin and blonde and had
nearly twice the usual amount of neck, which came in very useful as she
spent so much of her time craning over garden fences, spying on the
neighbors. The Dursleys had a small son called Dudley and in their
opinion there was no finer boy anywhere.

The Dursleys had everything they wanted, but they also had a secret, and
their greatest fear was that somebody would discover it. They didn't
think they could bear it if anyone found out about the Potters. Mrs.
Potter was Mrs. Dursley's sister, but they hadn't met for several years;
in fact, Mrs. Dursley pretended she didn't have a sister, because her
sister and her good-for-nothing husband were as unDursleyish as it was
possible to be. The Dursleys shuddered to think what the neighbors would
say if the Potters arrived in the street. The Dursleys knew that the
Potters had a small son, too, but they had never even seen him. This boy
was another good reason for keeping the Potters away; they didn't want
Dudley mixing with a child like that.

When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday our story
starts, there was nothing about the cloudy sky outside to suggest that
strange and mysterious things would soon be happening all over the
country. Mr. Dursley hummed as he picked out his most boring tie for
work, and Mrs. Dursley gossiped away happily as she wrestled a screaming
Dudley into his high chair.
"""

test = """
There exists a fascinating phenomenon where the presence of an attractive group amplifies the perceived attractiveness of each individual within it. An illustrative instance of this concept can be gleaned from its nomenclature: the Cheerleader Effect. This effect postulates that the allure of every member of a cheerleading group is elevated when they are collectively present, endowing them with an enhanced sense of prettiness and beauty.

Curiously, the genesis of this term can be attributed to the popular television series "How I Met Your Mother," an unlikely source for a psychological concept. Yet, the impact of the term was so substantial that it warranted scientific examination in 2013.

Researchers undertook a study involving participants, capturing both individual and group photographs of each. The outcomes consistently unveiled a recurring pattern: individuals appeared more attractive when part of a group. This phenomenon extends an intriguing perspective on the interplay of group dynamics and the perception of physical attractiveness.

In my viewpoint, this social effect is remarkably captivating, shedding light on the intricate ways in which human perception is influenced by collective contexts.


"""





# print(len(words)) #264
srt_file_path = r'C:\Users\Administrator\Downloads\The.srt'
subtitles = read_srt_file(srt_file_path)

# collector = strWordsCollector(test)
collector = strWordsCollector(subtitles)
new_words = collector.get_words()
# print(len(new_words)) #161

print(new_words)
print(len(new_words.split(' ')))

local_translator = LocalTranslator("PL")

translated_word = local_translator.translate(new_words.split()[0])

print(translated_word)
# print(len(top1000))
# print(top1000)
