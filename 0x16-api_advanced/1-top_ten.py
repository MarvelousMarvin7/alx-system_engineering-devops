#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Get and prints the titles of the first 10 hot
    posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}

    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)

    except requests.RequestException:
        print(None)
