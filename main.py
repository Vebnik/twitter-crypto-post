# libs
from dotenv import load_dotenv; load_dotenv()
import os

# module
from src.twitter.TwitterApi import TwitterApi


def tw_main():

  tw_api = TwitterApi(os.getenv('TW_BEARER'), os.getenv('TW_CSRF'), os.getenv('TW_COOKIE'))
  tw_api.create_tweet('Hello from main')

