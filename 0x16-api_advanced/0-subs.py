#!/usr/bin/python3
"""Return the number of Reddit API subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Find number of subscribers from reddit.
        If invalid subreddit return 0
        Parameters
        ----------
        subredit: [location]
                The location as call to about subscribers
        Returns
        -------
        Integer
                if subscribers:
                        number of subscribers for a valid group in reddit
                else:
                        Zero for invalid reddit group
    """
    URL = 'https://www.reddit.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) G\
                ecko/20100101 Firefox/91.0'}

    res = requests.get("{}r/{}/about/.json".format(URL, subreddit),
                       headers=headers, allow_redirects=False)
    if res.status_code == 200:
        json_res = res.json()['data']['subscribers']
        return json_res
    return 0
