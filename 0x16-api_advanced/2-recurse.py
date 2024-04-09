#!/usr/bin/python3
"""Reddit query"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 100, 'after': after}  # Request 100 posts per page

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            hot_list.extend([post['data']['title'] for post in posts])
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
