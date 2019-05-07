#!/usr/bin/env python3

import requests


# ideally we can use set but we don't want to lose the original order because it's important
def remove_duplicates(dup_list):
    unique_list = []
    for elem in dup_list:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list


def fetch_items_from_github():
    response_raw = requests\
        .get('https://api.github.com/search/repositories?sort=stars&q=stars:%3E500&page=1&per_page=100')
    if response_raw.status_code == 200:
        response_json = response_raw.json()
        items = response_json['items']
        return items
    return []


def main():
    items = fetch_items_from_github()
    languages = remove_duplicates([item['language'] for item in items])
    print('Top 10 popular languages on github from most to least popular: ')
    print(languages[:10])


main()
