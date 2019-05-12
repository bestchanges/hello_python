import requests

TOP_LIMIT = 5


def get_top_github_repositories() -> dict:
    languages = {}
    r = requests.get(f'https://api.github.com/search/repositories?sort=stars&q=stars:%3E500&page=1&per_page=100')
    if r.status_code == 200:
        for value in r.json()['items']:
            language = str(value['language'])
            if language != 'None':
                languages[language] = 1 if language not in languages else languages[language] + 1

    return dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))


if __name__ == '__main__':
    repositories = get_top_github_repositories()
    print(f"Top {TOP_LIMIT if len(repositories) >= TOP_LIMIT else len(repositories)} most rated languages on GitHub")
    for rank, language in enumerate(repositories, 1):
        if rank > TOP_LIMIT:
            break
        print(f'{rank}: {language}')

    print(f'Total repositories: {sum(repositories.values())}')

