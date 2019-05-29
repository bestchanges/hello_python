"""
Implements logic for calculating scores for completing session tasks and writing commit and review comments.

Scores for tasks are assigned to "FirstName LastName" user entity.
Scores for comments are assigned to Github login.
"""
import json
import requests
import requests.exceptions
import string
from typing import Dict
from collections import Counter


class GithubScores:
    # init
    def __init__(self, config_path: str = 'github.config.json'):
        self._load_config(config_path)
        self._create_session()

    # static
    @staticmethod
    def _slash_join(*args):
        return "/".join(arg.strip("/") for arg in args)

    @staticmethod
    def _convert_folders_to_names(folders):
        return [string.capwords(f.split('/')[-1].replace('_', ' ')) for f in folders]

    @staticmethod
    def _parse_comments(comments):
        return list(map(lambda c: (c['user']['login'], c['body']), comments))

    @staticmethod
    def _merge_dictionaries(dict1, dict2):
        return dict(Counter(dict1) + Counter(dict2))

    # private
    def _load_config(self, config_path):
        with open(config_path, 'r') as cfg:
            self._config = json.load(cfg)

    def _create_session(self):
        self._session = requests.session()
        self._session.headers.update({'Authorization': 'token ' + self._config['auth_token']})

    def _get_sessions(self):
        url = GithubScores._slash_join(self._get_repo_api_url(),
                                       'contents',
                                       self._config['repo']['path'])
        res = self._session.get(url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        sessions = res.json()
        sessions = list(filter(lambda f: f['type'] == 'dir', sessions))
        skip_sessions = [GithubScores._slash_join(self._config['repo']['path'], s)
                         for s in self._config['repo']['skip']]
        sessions = list(filter(lambda s: s['path'] not in skip_sessions, sessions))
        return list(map(lambda s: s['path'], sessions))

    def _get_session_folders(self, path):
        url = GithubScores._slash_join(self._get_repo_api_url(),
                                       'contents',
                                       path)
        res = self._session.get(url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        content = res.json()
        folders = list(filter(lambda f: f['type'] == 'dir', content))
        return list(map(lambda f: f['path'], folders))

    def _get_repo_api_url(self):
        return GithubScores._slash_join(self._config['base_api_url'],
                                        'repos',
                                        self._config['repo']['owner'],
                                        self._config['repo']['name'])

    def _get_commit_authors(self, path):
        url = GithubScores._slash_join(self._get_repo_api_url(),
                                       'commits')
        res = self._session.get(url, params={'path': path})
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        commits = res.json()
        return list(map(lambda c: c['author']['login'] if c['author']
                        else c['commit']['author']['name'], commits))

    def _get_commit_comments(self):
        url = GithubScores._slash_join(self._get_repo_api_url(),
                                       'comments')
        res = self._session.get(url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        comments = res.json()
        comments = GithubScores._parse_comments(comments)
        return comments

    def _get_pull_requests(self):
        url = GithubScores._slash_join(self._get_repo_api_url(),
                                       'pulls')
        res = self._session.get(url, params={'state': 'all'})
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        pulls = res.json()
        pulls = list(map(lambda p: p['url'], pulls))
        return pulls

    def _get_review_comments_url(self, pr_url):
        res = self._session.get(pr_url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        pr = res.json()
        return pr['comments_url']

    def _get_pr_comments(self, comments_url):
        res = self._session.get(comments_url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        comments = res.json()
        comments = GithubScores._parse_comments(comments)
        return comments

    # public
    def get_task_scores(self) -> Dict[str, int]:
        """
        :return: Dictionary like {'First Last': score} containing person's scores for all sessions tasks.
        """
        sessions = self._get_sessions()
        result = dict()
        for path in sessions:
            folders = self._get_session_folders(path)
            names = GithubScores._convert_folders_to_names(folders)
            for name in names:
                if name in result:
                    result[name] += self._config['scores']['task']
                else:
                    result[name] = self._config['scores']['task']
        return result

    def get_task_scores_for_session(self, path: str) -> Dict[str, int]:
        """
        :param path: Session folder path in github.
        :return: Dictionary like {'First Last': score} containing person's scores for specified session tasks.
        """
        result = dict()
        folders = self._get_session_folders(path)
        names = GithubScores._convert_folders_to_names(folders)
        for name in names:
            if name in result:
                result[name] += self._config['scores']['task']
            else:
                result[name] = self._config['scores']['task']
        return result

    def get_commit_comments_scores(self) -> Dict[str, int]:
        """
        :return: Dictionary like {'login': score} containing person's scores for commit comments.
        """
        comments = self._get_commit_comments()
        authors = [c[0] for c in comments]
        result = {a: authors.count(a) * self._config['scores']['comment'] for a in authors}
        return result

    def get_review_scores(self) -> Dict[str, int]:
        """
        :return: Dictionary like {'login': score} containing person's scores for PR review comments.
        """
        result = dict()
        prs = self._get_pull_requests()
        for pr in prs:
            comment_url = self._get_review_comments_url(pr)
            comments = self._get_pr_comments(comment_url)
            for comment in comments:
                author = comment[0]
                if author in result:
                    result[author] += self._config['scores']['comment']
                else:
                    result[author] = self._config['scores']['comment']
        return result

    def get_comment_scores(self) -> Dict[str, int]:
        """
        :return: Dictionary like {'login': score} containing person's scores for all comments.
        """
        commit_comment_scores = self.get_commit_comments_scores()
        pr_comment_scores = self.get_review_scores()
        return GithubScores._merge_dictionaries(commit_comment_scores, pr_comment_scores)


if __name__ == '__main__':
    # Sample usage
    gh = GithubScores()
    task_scores = gh.get_task_scores()
    print(task_scores)
    comment_scores = gh.get_comment_scores()
    print(comment_scores)
