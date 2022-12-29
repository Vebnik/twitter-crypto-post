# libs
import os, time, datetime as dt

# module
from src.bot.data_models import Env
from src.twitter.TwitterApi import TwitterApi
from src.binance.BinanceApi import BinanceApi
from src.mongo.DbConnector import DbConnector


class Bot:

  __slots__ = ('env', 'tw_api', 'bin_api')

  def __init__(self) -> None:
    if not self._check_auth_env():
      raise Exception('ERROR: check .env auth data')
    print('All env is ok ✅')

    self._create_api_instance()
    self._start_main_loop()

    
  def _start_main_loop(self) -> None:

    while True:

      crypto_data = self.bin_api.get_crypto(['BTCUSDT', 'ETHUSDT', 'LTCUSDT'])

      if not crypto_data:
        print('Error in bin_api.get_crypto ❌')
        time.sleep(30)
        continue

      tweet_content = crypto_data.get_pretty_str()
      response_data = self.tw_api.create_tweet(tweet_content)
      tweet_metadata = response_data.get('data', {}).get('create_tweet')
      
      if not tweet_metadata:
        print('Error in tw_api.create_tweet ❌', response_data)
        time.sleep(30)
        continue

      with DbConnector(self.env.MONGO_URL) as connect:
        logs = connect.db.get_collection(self.env.MONGO_COLL)

        logs.insert_one({
          'post_date': dt.datetime.now().strftime('%d.%m.%Y %H:%M'), 
          'tweet_content': tweet_content
        })

        print('Done post and save data ✅')

      time.sleep(60)

  def _create_api_instance(self) -> None:
    self.bin_api = BinanceApi()
    self.tw_api = TwitterApi(self.env.TW_BEARER, self.env.TW_CSRF, self.env.TW_COOKIE)

  def _check_auth_env(self) -> bool:
    self.env = Env()
    return all(self.env.get_env())

