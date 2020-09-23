import os.path
import re
import random
import pickle


class Model:

    def __init__(self, data_path='data.txt'):
        if os.path.exists(data_path):
            self.dictionary = pickle.load(data_path)
        else:
            self.dictionary = {}

    def fit(self, path):
        with open(path, 'r', encoding='utf8') as file:
            word = ''
            for new_word in file.read().split():
                new_word = re.sub(r'\W*',
                                  '',
                                  new_word.lower())
                if word in self.dictionary:
                    if new_word in self.dictionary[word]:
                        self.dictionary[word][new_word] += 1
                    else:
                        self.dictionary[word][new_word] = 1
                else:
                    self.dictionary[word] = {new_word: 1}
                word = new_word

    def generate(self, num_words_to_generate=3, prefix_path=''):
        res = ''
        if prefix_path != '':
            self.fit(prefix_path)
        word = random.choice(list(self.dictionary.keys()))
        res += word
        for i in range(num_words_to_generate):
            word = random.choices(list(self.dictionary[word].keys()),
                                  weights=self.dictionary[word].values())[0]
            res += ' ' + word
        return res
