from google_api_connector import get_sheet_data, set_sheet_data
from githubscores import GithubScores
from collections import Counter

SPREADSHEET_ID = '1iyS40VZfcHgirbZSmfjvhTeR4B0xCerU2-bvO6iekZc'
RANGE_NAME = 'F2:F175'
UPDATE_RANGE_NAME = 'G2:G175'


def main():
    users_list = get_sheet_data(SPREADSHEET_ID, RANGE_NAME)

    data = get_data_for_update()
    print("The next data will be updated:")
    for username, points in data.items():
        print("{}: {}".format(username, points))
    cells_values = []
    for user_data in users_list:
        cells_values.append(data[user_data[0]] if len(user_data) > 0 and user_data[0] in data else '')

    set_sheet_data(SPREADSHEET_ID, UPDATE_RANGE_NAME, cells_values)


def get_data_for_update():
    gh = GithubScores()
    task_scores = gh.get_task_scores()
    comment_scores = gh.get_comment_scores()
    data = dict(Counter(task_scores) + Counter(comment_scores))

    return data


if __name__ == '__main__':
    main()
