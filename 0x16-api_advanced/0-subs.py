#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    Returns 0 If an invalid subreddit is given.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/Flask)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    # print(response)
    if response.status_code == 200:
        # print(response)
        data = response.json()
        # print(data)
        return data['data']['subcribers']
    else:
        return 0
        # print('Error: ', response.status_code)
