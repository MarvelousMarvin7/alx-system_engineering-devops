#!/usr/bin/python3
"""Query reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all
    hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list if hot_list else None
        else:
            return None

    except requests.RequestException:
        return None
