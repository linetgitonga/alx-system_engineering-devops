#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            datt = get_data.get("data")
            title = datt.get("title")
            print(title)
    else:
        print(None)
