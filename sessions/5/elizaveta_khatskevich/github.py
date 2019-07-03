import requests
from tabulate import tabulate


def get_repositories(value):
    url = f'https://api.github.com/search/repositories?q={value}:>=100+fork:false&sort={value}&order=desc'
    response = requests.get(url).json()
    table = []
    if value == 'stars':
        type_name = 'stargazers_count'
    else:
        type_name = 'forks_count'
    for count, i in enumerate(response['items'], 1):
        table.append([count, i['name'], i[type_name], i['language']])
    return table


def calculate_languages(count_type):
    """Check language against most popular repos (by stars and by forks).

    :param count_type:      forks or stars
    :return:
    """
    repo_table = get_repositories(count_type)
    final_dic = {}
    table = []
    for each in repo_table:
        if each[3] not in final_dic.keys() and each[3]:   # verifying that language is not in dict yet
            final_dic[each[3]] = [each[1], each[2]]       # language as a key and project name + forks/stars as value
    for i, v in final_dic.items():                        # creating table for final pretty print
        table.append([i, v[0], v[1]])
    print(tabulate(table, headers=['Language', 'Project Name', count_type], tablefmt="fancy_grid"))


def create_tables():
    print('Languages of the most popular projects by stars:\n')
    calculate_languages('stars')
    print('\nLanguages of the most popular projects by forks:\n')
    calculate_languages('forks')


if __name__ == "__main__":
    create_tables()
