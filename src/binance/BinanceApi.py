# libs
from urllib.parse import quote_plus, quote
import json

# module
from src.binance.HttpClient import HttpClient
from src.binance.models import CryptoStore
from src.binance.ApiCollections import ApiCollections
from src.binance.utils import Utils


class BinanceApi:

  __slots__ = ('http_client', 'bin_api')

  def __init__(self) -> None:
    self.http_client = HttpClient()
    self.bin_api = ApiCollections()

  def get_crypto(self, crypto_list: list[str]) -> CryptoStore:
    url = f'{self.bin_api.get_price_by_symbols}{Utils.url_prettier(crypto_list)}'

    response = self.http_client.get(url)

    if response:
      return CryptoStore(response)

