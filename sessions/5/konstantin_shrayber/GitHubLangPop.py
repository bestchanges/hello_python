from github import Github

g = Github("Kastyl", "chicago1984")

popular_repos_by_lang = {}
temp_repos_list = []

repos_stars = g.search_repositories("stars:>17000")
print("stars>17000 repos count:", repos_stars.totalCount)

repos_forks = g.search_repositories("forks:>5000")
print("forks>5000 repos count:", repos_forks.totalCount)

for repo in repos_forks:
    if repo.language is not None:
        temp_repos_list.append(repo.name)

print(len(temp_repos_list))

for repo in repos_stars:
    if repo.language is not None and repo.name in temp_repos_list:
        popular_repos_by_lang.setdefault(repo.language, 0)
        popular_repos_by_lang[repo.language] += 1

for langs in sorted(popular_repos_by_lang, key=popular_repos_by_lang.get, reverse=True):
    print(f'{langs} : {popular_repos_by_lang[langs]}')