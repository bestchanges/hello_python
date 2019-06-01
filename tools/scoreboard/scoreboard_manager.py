import logging

from google_api_connector import get_sheet_data, set_sheet_data
from githubscores import GithubScores
from collections import Counter

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1

logger = logging.getLogger(__name__)

SPREADSHEET_ID = '1iyS40VZfcHgirbZSmfjvhTeR4B0xCerU2-bvO6iekZc'
COLUMN_NAME = 'a'
COLUMN_GITHUB = 'f'
COLUMN_SCORE = 'g'
LINES = 300
RANGE_NAME = f'{COLUMN_NAME}2:{COLUMN_NAME}{LINES+1}'
RANGE_GITHUB = f'{COLUMN_GITHUB}2:{COLUMN_GITHUB}{LINES+1}'
RANGE_SCORE = f'{COLUMN_SCORE}2:{COLUMN_SCORE}{LINES+1}'


if __name__ == '__main__':
    users = get_sheet_data(SPREADSHEET_ID, RANGE_NAME)
    github_accounts = get_sheet_data(SPREADSHEET_ID, RANGE_GITHUB)

    github_to_user = {github_accounts[i][0]: users[i][0] for i in range(len(github_accounts)) if github_accounts[i]}

    gh = GithubScores()
    task_scores = gh.get_task_scores()
    comment_scores_github_accounts = gh.get_comment_scores()
    comment_scores = {github_to_user[github_account]: score for github_account, score in comment_scores_github_accounts.items() if github_account in github_to_user}
    total_scores = Counter(comment_scores) + Counter(task_scores)

    users_set = {user[0] for user in users if user}
    scores_set = {user for user in total_scores}
    diff = scores_set - users_set
    logger.warning(f"Missing names for users: {diff}")

    scores = [total_scores.get(user[0] if user else None, 0) for user in users]

    set_sheet_data(SPREADSHEET_ID, RANGE_SCORE, scores)
