#!/usr/bin/python3
"""
 recursive function that queries the Reddit API,
 parses the title of all hot articles, and prints a
 sorted count of given keywords(case-insensitive,
 delimited by spaces. Javascript should count as javascript,
 but java should not).
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    # Base case: if after is None, print the counts
    if after is None:
        if counts:
            for word, count in sorted(counts.
                                      items(), key=lambda x: (-x[1], x[0])):
                print(f"{word}: {count}")
        return

    # Reddit API endpoint for hot articles in a subreddit with pagination
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format
    (subreddit, after)

    # Custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    try:
        # Make GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()

            # Initialize counts dictionary if not already initialized
            if counts is None:
                counts = Counter()

            # Extract and count words in titles
            for post in data['data']['children']:
                title_words = post['data']['title'].lower().split()
                for word in word_list:
                    # Ensure word is not a substring of a larger word
                    if any(title_word == word for title_word in title_words):
                        counts[word] += title_words.count(word)

            # Recursive call with the next 'after' value
            count_words(subreddit, word_list,
                        after=data['data']['after'], counts=counts)
        elif response.status_code == 404:
            # Subreddit not found
            print("Invalid subreddit")
        else:
            # Other error occurred
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
