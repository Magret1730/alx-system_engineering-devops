#!/usr/bin/python3
"""Reddit"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 100, 'after': after}  # Request 100 posts per page

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                title = post['data']['title']
                words_in_title = title.lower().split()
                for word in word_list:
                    if word.lower() in words_in_title:
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            after = data['data']['after']
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no posts match.")
