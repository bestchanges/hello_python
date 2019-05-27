import requests
import json


URL_example = r"https://raw.githubusercontent.com/bestchanges/hello_python/master/sessions/2/dict.txt"
URL = "https://api.github.com/search/repositories"
REPOS_FILE_PATH = r"E:\python\Hello Python\repos.json"

PARAMS = dict(q="forks>1", per_page="500")


def get_repos():
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


resp = get_repos()
total_reps = resp["total_count"]

stats = {} #change structure to criteria - language - value
for i in resp["items"]:
    lang = i["language"]
    if lang:
        lang_stats = stats.get(lang, {})

        count = lang_stats.get("count", 0) + 1
        stars = lang_stats.get("stars", 0) + i["stargazers_count"]
        forks = lang_stats.get("forks", 0) + i["forks_count"]
        scores = lang_stats.get("scores", 0.0) + i["score"]

        lang_stats = dict(count=count,
                          stars=stars,
                          forks=forks,
                          scores=scores
                          )
        stats[lang] = lang_stats
    else:
        total_reps -= 1

print("Total repositories: ", total_reps)


count = 0
for k, v in stats.items():
    print(k)
    for p, val in v.items():
        print(p, val)
        if p == "count":
            count += val
    print()
print(count)
