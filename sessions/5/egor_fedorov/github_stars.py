"""
Refer to: 
https://developer.github.com/v3/#pagination
https://developer.github.com/v3/search/#search-repositories
https://help.github.com/en/articles/searching-for-repositories#search-by-number-of-stars
https://help.github.com/en/articles/searching-for-repositories#search-by-number-of-forks


"""
import json
from collections import defaultdict

import requests


def cached_data():
    with open('r1.json') as f:
        return json.load(f)


def request_data():
    params = {
        'sort': 'stars',
        'q': 'stars: > 500',
        'page': '1',
        'per_page': '100',
    }
    response = requests.get('https://api.github.com/search/repositories', params)
    return response.json()

if __name__ == '__main__':
    # data = request_data()
    data = cached_data()
    language_stars = defaultdict(lambda: 0)
    language_forks = {}
    for repository in data['items']:
        language = repository['language']
        language_stars[language] += 1
    for language in sorted(language_stars, key=language_stars.get, reverse=True):
        print(f'{language} : {language_stars[language]}')