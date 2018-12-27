#Author: Austin Hoyle
#Markov Chain Sentence Generator
# -*- coding: utf-8 -*-

import json
import random
import re

class Markov:

    file = None
    output_json = {}
    starting_strings = []


    def __init__(self, file):
        self.file = file


    def parse_file(self):
        text = open(self.file,'r')
        return text.read().split()


    def generate_chain(self):
        strings = self.parse_file()
        self.add_values(strings)

        with open("chain.json", 'w') as out:
            json.dump(self.output_json, out)
        return self.output_json


    def retrieve_chains(self, filename):
        with open(filename, 'r') as chains:
            self.output_json = json.loads(chains.read())


    def check_periods(self, string):
        if ("." in string and string.endswith(".")) or "." not in string:
            return True
        else:
            return False


    def includes_period(self, string):
        if "." in string:
            return True
        else:
            return False


    def create_sentence(self):
        sentence = ""
        current_fragment = random.choice(self.starting_strings)
        sentence = sentence+" "+current_fragment

        while not self.includes_period(current_fragment):
            random_value = random.choice(self.output_json.get(current_fragment))
            sentence = sentence + " " + random_value
            current_fragment = current_fragment.split()[1] + " " + random_value

        print(sentence)


    def add_values(self, strings):

        for i, word in enumerate(strings):
            if i+2 < len(strings) and word+" "+strings[i+1] in self.output_json:
                self.output_json[word+" "+strings[i+1]].append(strings[i+2])

            elif i+2 < len(strings) and not self.includes_period(word+" "+strings[i+1]):
                self.output_json[word+" "+strings[i+1]] = [strings[i+2]]

                if word[0].isupper():
                    self.starting_strings.append(word+" "+strings[i+1])
