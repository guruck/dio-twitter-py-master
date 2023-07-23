import tweepy
from fastapi import FastAPI
from requests_oauthlib import OAuth1Session
from src.constants import BRAZIL_WOE_ID
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_KEY_SECRET, BEARER_TOKEN


def get_trends(woe_id: int):
    auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    print(api)
    tweets = api.get_lists(user_id=woe_id)
    print('aqui: ', tweets)


app = FastAPI()


@app.get("/trends")
def get_trends_route():
    return get_trends(BRAZIL_WOE_ID)
