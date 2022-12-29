# libs
from pymongo import MongoClient
from typing import Any


class DbConnector:

  __slots__ = ('client', 'db')

  def __init__(self, mongo_url: str) -> None:
    self.client: MongoClient = MongoClient(mongo_url)

  def __enter__(self):
    self.db = self.client.twitter_bot_log
    return self

  def __exit__(self, *args) -> bool|None:
    self.client.close()

    if any(args):
      raise Exception(args)
    return True


