# Fakes are useful when you need to replace a real implementation with a lightweight
# alternative that simulates the behavior of the real implementation but is simpler
# and faster to execute.
# Code forked from: https://pythonspeed.com/articles/verified-fakes/

import sys

import pytest


class TwitterClient:
    """A client for interacting with Twitter API"""

    def tweet(self, message):
        # External API call to post a tweet
        pass

    def list_tweets(self):
        # External API call to list tweets
        pass


class FakeTwitterClient:
    def __init__(self, tweets=None):
        if tweets is None:
            self.tweets = []
        else:
            self.tweets = tweets

    def tweet(self, message):
        self.tweets.append(message)

    def list_tweets(self):
        return self.tweets


@pytest.mark.parametrize(
    "client, expected",
    [
        pytest.param(TwitterClient(), [4, 5, 6], marks=pytest.mark.real),
        (FakeTwitterClient([1, 2, 3]), [1, 2, 3]),
    ],
)
def test_list_tweets(client, expected):
    assert client.list_tweets() == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-vv", "-m 'not real'"]))
