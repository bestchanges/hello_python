#!python3

import requests
import json
import operator

stat = {}  # collect counts - statistic here


def add_language(lang):
    """Add into dictionary regarlless if such key is there already or not"""
    ref = lang if lang is not None else "N/A"  # reference to handle None etc
    stat[ref] = stat.setdefault(ref, 0) + 1


#  TODO:
#   1) find out the proper request. 'git' is just POC
#   2) from language usage counting - ensure project is valuable
#           (matching "наиболее ценимые сейчас сообщством проекты")

r = requests.get('https://api.github.com/search/repositories?q=git')
j = json.loads(r.text)

for i in j["items"]:
    add_language(i["language"])

# Finding max in dict values
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
result = max(stat.items(), key=operator.itemgetter(1))

print("language={} count={}".format(result[0], result[1]))
