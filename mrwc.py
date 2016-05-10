#!/usr/bin/env python

import mincemeat

import sys

def mapper(k,v):
    import re
    r_alphabet = re.compile(u'[а-яА-Я]+')
    file = open(v,'r')
    for line in file:
        for word in r_alphabet.findall(line.lower()):
            yield word,1


def reducer(k, vs):
    result = sum(vs)
    return result

with open("data_1.txt",'r') as datafile:
    data = datafile.read().splitlines()
    datasource = dict(enumerate(data))

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapper
s.reducefn = reducer

results = s.run_server()

with open("res.txt",'w') as rfile:
    for r in results.items():
        print(r,file=rfile)


