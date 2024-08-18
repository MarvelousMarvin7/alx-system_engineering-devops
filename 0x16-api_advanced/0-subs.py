#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers (not active users,
    total subscribers) for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}

    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            return data['data']['subscribers']
        else:
            return 0

    except requests.RequestException:
        return 0
