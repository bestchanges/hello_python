"""
Collects and prints data about most used languages for most popular github public repositories.
"""
import requests
from collections import Counter


TOP_LANGUAGES_COUNT = 10


def get_top_repos(feature, count):
    """Returns top n repositories sorted by feature (stars or forks)."""
    assert feature in ["stars", "forks"], "Feature must be 'forks' or 'stars'."
    response = requests.get(f"https://api.github.com/search/repositories?sort={feature}&order=desc&q={feature}:>=100+fork:false")
    data = response.json()
    top_repos = data["items"][:count]
    return top_repos


def get_languages_info(repo):
    """Returns collection of repository languages with number of lines."""
    assert "languages_url" in repo, "Languages URL is missing."
    response = requests.get(repo["languages_url"])
    data = response.json()
    return data


def merge_dicts(dict1, dict2):
    """Return merged dictionaries with sum value for matching keys."""
    return dict(Counter(dict1) + Counter(dict2))


def sort_dict_by_values(d):
    """Returns list of tuples which are dictionary's key-value pairs sorted by value by descending."""
    return sorted({(value, key) for (key, value) in d.items()}, reverse=True)


def main():
    """Prints top languages for most popular github repos."""
    for feature in ["stars", "forks"]:
        top_repos = get_top_repos(feature, 100)
        languages = dict()
        for repo in top_repos:
            repo_lang = get_languages_info(repo)
            languages = merge_dicts(repo_lang, languages)
        languages = sort_dict_by_values(languages)
        languages = languages[:TOP_LANGUAGES_COUNT]
        print(f"\n\nTop {TOP_LANGUAGES_COUNT} languages within most {feature[:-1]}ed repositories:")
        for lang in languages:
            print(lang[1])


if __name__ == "__main__":
    main()
