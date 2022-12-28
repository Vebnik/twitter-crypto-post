# libs
import os


class ApiCollections:
  # api config
  QUERI_ID = os.getenv('TW_QUERI_ID')
  API_URL = 'https://api.twitter.com/graphql'

  # api sample
  @property
  def create_tweet(self) -> str:
    return f'{self.API_URL}/{self.QUERI_ID}/CreateTweet'

  @property
  def delete_tweet(self) -> str:
    return f'{self.API_URL}/{self.QUERI_ID}/DeleteTweet'

