# libs
from dotenv import load_dotenv; load_dotenv()
import os, datetime as dt

# module
from src.twitter.TwitterApi import TwitterApi
from src.binance.BinanceApi import BinanceApi
from src.mongo.DbConnector import DbConnector


def tw_main(text) -> None:

  tw_api = TwitterApi(os.getenv('TW_BEARER'), os.getenv('TW_CSRF'), os.getenv('TW_COOKIE'))
  tw_api.create_tweet(text) 


def bin_main() -> None:

  bin_api = BinanceApi()
  crypto_data = bin_api.get_crypto(['BTCUSDT', 'ETHUSDT', 'LTCUSDT']) 
  tweet_content = crypto_data.get_pretty_str()

  tw_main(tweet_content)
  print(tweet_content)


def mongo_main() -> None:
  
  with DbConnector(os.getenv('MONGO_URL')) as connect:
    logs = connect.db.get_collection(os.getenv('MONGO_COLL'))
    logs.insert_one()

