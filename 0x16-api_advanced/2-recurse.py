#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returnsa list
containing the titles of all hot articles for a givensubreddit.
If no results are found for the given subreddit, the function should
return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "CustomUserAgent/3.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
