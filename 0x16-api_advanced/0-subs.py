#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """function to display number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'User Agent 1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get['data'].get['subscribers']
    else:
        return 0
