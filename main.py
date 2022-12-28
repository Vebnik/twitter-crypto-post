# libs
from dotenv import load_dotenv; load_dotenv()
import os

# module
from src.twitter.TwitterApi import TwitterApi
from src.binance.BinanceApi import BinanceApi

def tw_main(text):

  tw_api = TwitterApi(os.getenv('TW_BEARER'), os.getenv('TW_CSRF'), os.getenv('TW_COOKIE'))
  tw_api.create_tweet(text) 


def bin_main():

  bin_api = BinanceApi()
  crypto_data = bin_api.get_crypto(['BTCUSDT', 'ETHUSDT', 'LTCUSDT']) 
  tweet_content = crypto_data.get_pretty_str()

  # tw_main(tweet_content)
  
  print(tweet_content)