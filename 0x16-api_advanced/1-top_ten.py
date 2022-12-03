#!/usr/bin/python3
'''
function that queries the Reddit API
prints the titles of the first 10 hot posts
'''
import requests


def top_ten(subreddit):
    '''print only top 10 posts for a given post
    Parameters
    ----------
    subreddit: [location]
            The path for quering the post from reddit
    redirect: allow_redirects
            always false to ensure no redirects incase of invalid post
    Returns
    -------
            if subreddit == True:
                    print out top 10 hot post
            else
                    print None for an invalid subreddit
    '''
    url = 'https://www.reddit.com/'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

    res = requests.get('{}/r/{}/hot/.json'.format(url,
                                                  subreddit), headers=headers,
                       allow_redirects=False)
    if res.status_code == 200:
        my_res = res.json()['data']['children'][:10]
        for values in my_res:
            value = values['data']['title']
            print(value)
    else:
        print(None)
