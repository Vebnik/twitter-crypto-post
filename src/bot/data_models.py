# libs
import os


class Env:

  __slots__ = ('TW_BEARER', 'TW_CSRF', 'TW_COOKIE', 'MONGO_URL', 'MONGO_COLL', 'TW_QUERI_ID', 'MONGO_DB_NAME')

  def __init__(self) -> None:
    self.TW_BEARER = os.getenv('TW_BEARER')
    self.TW_CSRF = os.getenv('TW_CSRF')
    self.TW_COOKIE = os.getenv('TW_COOKIE')
    self.TW_QUERI_ID = os.getenv('TW_QUERI_ID')
    self.MONGO_URL = os.getenv('MONGO_URL')
    self.MONGO_COLL = os.getenv('MONGO_COLL')
    self.MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')


  def get_env(self) -> list[str|None]:
    return [
      self.TW_BEARER,
      self.TW_CSRF,
      self.TW_COOKIE,
      self.TW_QUERI_ID,
      self.MONGO_URL,
      self.MONGO_COLL,
      self.MONGO_DB_NAME
    ]