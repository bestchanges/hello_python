import requests
import json

URL = "https://api.github.com/search/repositories"
PARAMS = dict(q="forks>1", per_page="3000")
REPOS_FILE_PATH = r"repos.json"
# change the list of criteria if you like
CRITERIA = ["count",
            "stargazers_count",
            "forks_count",
            "score"]


def get_repos() -> dict:
    """getting search results from github and storing into local file"""
    try:
        with open(REPOS_FILE_PATH, "r") as repos_file:
            repos = json.load(repos_file)

    except IOError:
        repos_obj = requests.get(URL, PARAMS)
        repos = repos_obj.json()
        repos["URL"] = repos_obj.url
        with open(REPOS_FILE_PATH, "w") as repos_file:
            json.dump(repos, repos_file)

    return repos


def collect_stats(raw_github_response) -> dict:
    """collecting basic info from "items" list on the response"""
    stats = {}

    for repo in raw_github_response["items"]:
        lang = repo["language"]
        if lang:
            for crit in CRITERIA:
                adding_value = 1 if crit == "count" else repo[crit]
                stats[crit] = stats.get(crit, {})
                stats[crit][lang] = stats[crit].get(lang, 0) + adding_value

    return stats


def normalize_stats(raw_stats) -> dict:
    """each value is divided by MAX in the criteria to get the data normalized"""
    normal_stats = {}

    for crit, lang_data in raw_stats.items():
        max_val = max(lang_data.values())
        normal_stats[crit] = {}
        for lang_name, value in lang_data.items():
            normal_stats[crit][lang_name] = round(raw_stats[crit][lang_name] / max_val, 2)

    return normal_stats


def integrate_criteria(normal_stats) -> dict:
    """adding integrated criterium as a simple sum of all normalized values for each language"""
    global CRITERIA

    new_crit = "integrated_criteria"
    CRITERIA = [new_crit] + CRITERIA
    integrated_crit = {}

    for lang_data in normal_stats.values():
        for lang, val in lang_data.items():
            integrated_crit[lang] = round(integrated_crit.get(lang, 0) + val, 2)
    normal_stats[new_crit] = integrated_crit

    return normal_stats


def sorted_stats(stats_final) -> dict:
    """sorting values in each criteria from largest to smallest"""
    for crit, lang_data in stats_final.items():
        stats_final[crit] = sorted([(val, lang) for lang, val in lang_data.items()], reverse=True)

    return stats_final


def __main__():
    github_data = get_repos()
    raw_statistics = collect_stats(github_data)
    normal_stats = normalize_stats(raw_statistics)
    final_stats = sorted_stats(integrate_criteria(normal_stats))

    for crit in CRITERIA:
        print(crit)
        print(*final_stats[crit], sep="\n")
        print()


__main__()
