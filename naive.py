#!/usr/bin/env python

import re
r_alphabet = re.compile(u'[а-яА-Я]+')
def gen(v):
    file = open(v,'r')
    for line in file:
        for word in r_alphabet.findall(line.lower()):
            yield word

if __name__ == '__main__':
    dictionary = dict()
    with open("data_1.txt",'r') as datafile:
        data = datafile.read().splitlines()
    for d in data:
        for word in gen(d):
            if dictionary.get(word) == None:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    print(sorted(dictionary.items(), key = lambda x: -x[1])[:10])