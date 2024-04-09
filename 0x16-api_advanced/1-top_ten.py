#!/usr/bin/python3
""" Query subreddit"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 2.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response)
        data = response.json()
        posts = data['data']['children'][:10]
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
        print("Error:", response.status_code)


if __name__ == "__main__":
    top_ten("python3")
