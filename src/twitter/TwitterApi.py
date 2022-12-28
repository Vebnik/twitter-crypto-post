# module
from src.twitter.ApiCollections import ApiCollections
from src.twitter.HttpClient import HttpClient
from src.twitter.GrapyhQlConfig import Config


class TwitterApi:

  __slots__ = ('TW_BEARER', 'TW_CSRF', 'TW_COOKIE', 'api_coll', 'htttp_client', 'headers')

  def __init__(self, tw_bearer: str, tw_csrf: str, tw_cookie: str) -> None:
    self.TW_BEARER = tw_bearer
    self.TW_CSRF = tw_csrf
    self.TW_COOKIE = tw_cookie

    self.api_coll: ApiCollections = ApiCollections()
    self.htttp_client: HttpClient = HttpClient()
    self.headers = {'authorization': self.TW_BEARER, 'x-csrf-token': self.TW_CSRF, 'cookie': self.TW_COOKIE}

  def create_tweet(self, tweet_text: str) -> dict:    
    
    response = self.htttp_client.post(
      url=self.api_coll.create_tweet, 
      headers=self.headers, 
      payload=Config.get_create_tweet_payload(tweet_text)
    )

    if response:
      return response


      