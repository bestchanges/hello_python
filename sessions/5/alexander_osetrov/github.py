import requests
from collections import defaultdict


def get_repositories(stars=30000):
    request = requests.get(f"https://api.github.com/search/repositories?q=stars:>={stars}&order=desc")
    return request.json()


def get_languages(repositories):
    languages = defaultdict(list)
    for repo in repositories['items']:
        languages[repo['language']] += [repo['name']]
    sorted_languages = dict(sorted(languages.items(), key=lambda k: (len(k[1]), k[0]), reverse=True))
    return sorted_languages


def print_statistics():
    repositories = get_repositories()
    languages = get_languages(repositories)
    print(f"Top Project Languages:")
    for language, project_list in languages.items():
        project_count = len(project_list)
        projects = ", ".join(project_list)
        print(f"Language: {language} ({project_count}). Projects: {projects}")


if __name__ == "__main__":
    print_statistics()
