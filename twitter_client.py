import requests
import requests_oauthlib

# change twitter_auth_keys_sample.py file to twitter_auth_keys.py
from twitter_auth_keys import *

auth = requests_oauthlib.OAuth1(CONSUMER_KEY,
                                CONSUMER_API_SECRET,
                                ACCESS_TOKEN,
                                ACCESS_TOKEN_SECRET,
                                signature_type='auth_header')


def get_tweets_filter(track='', locations=None):
    url = 'https://stream.twitter.com/1.1/statuses/filter.json?'
    data = f'track={track}'
    query_url = url + data
    response = requests.get(query_url, auth=auth, stream=True)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(decoded_line)


def get_tweets_sample():
    """
    getting twit stream in real-time
    :return:
    """
    url = 'https://stream.twitter.com/1.1/statuses/sample.json'
    response = requests.get(url, auth=auth, stream=True)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(decoded_line)


if __name__ == '__main__':
    get_tweets_filter(track='toronto')
